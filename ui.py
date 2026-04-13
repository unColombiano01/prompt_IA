import tkinter as tk
from main import enviar_mensaje

def enviar():
    user_input = entrada.get()
    if not user_input.strip():
        return

    entrada.delete(0, tk.END)

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"\n🧑 Tú:\n{user_input}\n", "user")

    respuesta = enviar_mensaje(user_input)

    chat_box.insert(tk.END, f"\n🤖 Bot:\n{respuesta}\n", "bot")
    chat_box.config(state=tk.DISABLED)

    chat_box.yview(tk.END)

# Ventana
ventana = tk.Tk()
ventana.title("Chat IA")
ventana.geometry("900x600")
ventana.configure(bg="#1e1e1e")

# Área de chat
chat_box = tk.Text(ventana, bg="#1e1e1e", fg="white", wrap="word")
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.tag_config("user", foreground="#00ffcc")
chat_box.tag_config("bot", foreground="#ffffff")

chat_box.config(state=tk.DISABLED)

# Entrada
entrada = tk.Entry(ventana, bg="#2e2e2e", fg="white", insertbackground="white")
entrada.pack(padx=10, pady=5, fill=tk.X)

# Botón
boton = tk.Button(ventana, text="Enviar", command=enviar, bg="#009C2A", fg="white", height=2, width=10,)
boton.pack(pady=5)

ventana.mainloop()