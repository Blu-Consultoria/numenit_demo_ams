"use server"

import { headers } from "next/headers";
import { cookies } from 'next/headers';

const LOGIN_URL = "http://127.0.0.1:8000/login/";

export async function loginUser(formData) {
  const username = formData.get("email");
  const password = formData.get("password");
  console.log("Login attempt:", { username, password });

  const jsonData = JSON.stringify({ username, password });

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonData,
    credentials: "include",
  };

  const response = await fetch(LOGIN_URL, requestOptions);

  if (response.ok) {
    const responseData = await response.json();
    console.log("logged in");

    const authToken = responseData.access;
    if (!authToken) {
      console.error("Token ausente na resposta");
      return { success: false, error: "Token ausente" };
    }

    const cookieStore = await cookies();  // ✅ Aqui está a correção
    cookieStore.set({
      name: "auth-token",
      value: authToken,
      httpOnly: true,
      sameSite: "strict",
      secure: process.env.NODE_ENV !== "development",
      maxAge: 3600,
    });
    console.log("Auth token cookie set:", authToken);
    return { success: true };
  } else {
    console.error("Login falhou:", response.status);
    return {
      success: false,
      error: `Falha no login: ${response.status}`,
    };
  }
}



export async function checkUserData() {
  try {
    const cookieStore = await cookies();
    const authToken = cookieStore.get('auth-token')?.value;

    if (!authToken) {
      return { success: false, error: 'User not authenticated' };
    }

    const res = await fetch('http://127.0.0.1:8000/session', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${authToken}`
      },
    });

    if (!res.ok) {
      throw new Error(`Error in response: ${res.status}`);
    }

    const data = await res.json();
    return { success: true, data };
  } catch (error) {
    console.error('Error in checkUserData:', error);
    return { success: false, error: 'Error checking session status' };
  }
}

export async function logoutUser() {
  try {
    const cookieStore = await cookies();

    // Remove o cookie deletando-o com maxAge 0
    cookieStore.set({
      name: "auth-token",
      value: "",
      httpOnly: true,
      sameSite: "strict",
      secure: process.env.NODE_ENV !== "development",
      maxAge: 0, // Isso remove o cookie
    });

    console.log("Auth token removido com sucesso.");
    return { success: true };
  } catch (error) {
    console.error("Erro ao tentar remover o cookie:", error);
    return { success: false, error: "Erro ao tentar sair da sessão." };
  }
}


