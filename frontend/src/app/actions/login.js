"use server"

function getCookie(name) {
  if (typeof document === "undefined") return null;
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

export async function loginUser(formData) {
  const username = formData.get("email");
  const password = formData.get("password");

  try {
    // 1. Buscar o CSRF Token
    await fetch("http://127.0.0.1:8000/csrf/", {
      method: "GET",
      credentials: "include",
    });

    const csrfToken = getCookie("csrftoken");

    // 2. Enviar o login com o token
    const res = await fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ username, password }),
    });

    if (!res.ok) {
      const data = await res.json();
      throw new Error(data?.error || "Login falhou");
    }

    return { success: true, data: await res.json() };
  } catch (error) {
    return { success: false, error: error.message || "Erro ao fazer login" };
  }
}

export async function checkUserData() {
  try {
    const res = await fetch("http://127.0.0.1:8000/session_status/", {
      method: "GET",
      credentials: "include",
    });

    if (!res.ok) throw new Error("Failed to check session status");

    return { success: true, data: await res.json() };
  } catch (error) {
    return { success: false, error: error.message || "Erro ao verificar sessão" };
  }
}

export async function logoutUser() {
  try {
    const res = await fetch("http://127.0.0.1:8000/logout/", {
      method: "POST",  // 🚨 CORREÇÃO: deve ser POST
      credentials: "include",
    });

    if (!res.ok) throw new Error("Erro ao deslogar");

    return { success: true, data: await res.json() };
  } catch (error) {
    return { success: false, error: error.message || "Erro ao deslogar" };
  }
}
