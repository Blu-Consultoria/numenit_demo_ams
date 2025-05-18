"use server"

export async function loginUser(formData) {
  const username = formData.get("email");
  const password = formData.get("password");

  try {
    const res = await fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
    
    if (!res.ok) throw new Error("Login failed");
    
    // Retorne os dados se necessário
    return { success: true, data: await res.json() };
  } catch (error) {
    return { success: false, error: "Erro ao fazer login" };
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
    return { success: false, error: "Erro ao verificar status da sessão" };
  }
}
