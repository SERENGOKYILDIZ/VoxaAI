import tkinter as tk
from brain import process_message

def run_app():
    def send_message():
        msg = entry.get()
        if not msg.strip():
            return
        chat.config(state="normal")
        chat.insert(tk.END, f"Sen: {msg}\n")
        response = process_message(msg)
        chat.insert(tk.END, f"AI: {response}\n\n")
        chat.config(state="disabled")
        entry.delete(0, tk.END)

    window = tk.Tk()
    window.title("Arkadaş AI")
    window.geometry("500x500")

    chat = tk.Text(window, state="disabled", wrap="word")
    chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(window)
    entry.pack(padx=10, pady=(0,10), fill=tk.X)
    entry.bind("<Return>", lambda e: send_message())

    send_btn = tk.Button(window, text="Gönder", command=send_message)
    send_btn.pack(pady=(0, 10))

    window.mainloop()
