from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI
from django.contrib.auth import authenticate
from ninja_jwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
from ninja.errors import HttpError

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None
    
@csrf_exempt
@api.post("/login")
def login_api(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"success": False, "error": "Invalid credentials"}, status=403)

        refresh = RefreshToken.for_user(user)

        return JsonResponse({
            "success": True,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "username": user.username,
                "email": user.email
            }
        })
    except Exception as e:
        print("Login error:", str(e))
        return JsonResponse({"success": False, "error": "Internal server error"}, status=500)

@csrf_exempt
@api.post("/logout")
def logout_view(request):
    try:
        body = request.body.decode()
        data = json.loads(body)
        refresh_token = data.get("refresh")

        if not refresh_token:
            raise HttpError(400, "Refresh token não enviado")

        token = RefreshToken(refresh_token)
        token.blacklist()  # Requer blacklist ativado no ninja_jwt (igual ao rest_framework_simplejwt)

        return {"success": True, "message": "Logout realizado e refresh token revogado"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@api.get("/session", auth=JWTAuth())
def session_status(request):
    user = request.user
    return {
        "username": user.username,
        "email": user.email,
        "authenticated": True
    }

