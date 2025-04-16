import tkinter as tk
from tkinter import PhotoImage
from scripts.brain import process_message
import os
from PIL import Image, ImageTk

def run_app():
    def send_message():
        msg = entry.get().strip()
        if not msg:
            return
        chat.configure(state="normal")
        chat.insert(tk.END, f"\n🧍 Sen: {msg}\n", "user")
        response = process_message(msg)
        chat.insert(tk.END, f"🤖 VoxaAI: {response}\n", "ai")
        chat.configure(state="disabled")
        chat.see(tk.END)
        entry.delete(0, tk.END)

    # Pencere
    window = tk.Tk()
    window.title("VoxaAI - Dijital Arkadaşın")
    window.geometry("600x650")
    window.configure(bg="#1e1e1e")
    window.resizable(False, False)

    # Frame (üstte avatar + isim için)
    top_frame = tk.Frame(window, bg="#1e1e1e")
    top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Avatar yükle
    # Avatar yükle (Pillow ile yeniden boyutlandır)
    avatar_path = os.path.join("assets", "avatar_normal.png")
    avatar_image = Image.open(avatar_path).resize((100, 150), Image.LANCZOS)
    avatar_img = ImageTk.PhotoImage(avatar_image)
    window.avatar_img = avatar_img  # referans tutulmalı

    avatar_label = tk.Label(top_frame, image=avatar_img, bg="#1e1e1e")
    avatar_label.pack(side=tk.LEFT, padx=(0, 10))

    # Başlık yazısı
    title_label = tk.Label(top_frame, text="🌟 VoxaAI", font=("Segoe UI", 18, "bold"), fg="#6c9eff", bg="#1e1e1e")
    title_label.pack(side=tk.LEFT, anchor="center")

    # Chat alanı
    chat = tk.Text(window, state="disabled", wrap="word", bg="#2e2e2e", fg="#eeeeee",
                   font=("Segoe UI", 11), padx=10, pady=10, relief="flat")
    chat.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=False)
    chat.config(height=18)

    chat.tag_config("user", foreground="#8bdfff")
    chat.tag_config("ai", foreground="#aaffaa")

    # Giriş alanı
    entry = tk.Entry(window, font=("Segoe UI", 11), bg="#3c3f41", fg="white",
                     insertbackground="white", relief="flat")
    entry.pack(padx=10, pady=(0, 5), fill=tk.X)
    entry.bind("<Return>", lambda e: send_message())

    # Gönder butonu
    send_btn = tk.Button(window, text="Gönder", command=send_message,
                         font=("Segoe UI", 10, "bold"),
                         bg="#5c5cff", fg="white", relief="flat",
                         activebackground="#6e6eff", activeforeground="white", padx=10, pady=5)
    send_btn.pack(pady=(0, 10))

    window.mainloop()
