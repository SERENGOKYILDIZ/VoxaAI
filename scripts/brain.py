import json
import os

MEMORY_FILE = "data/memory.json"

# Geçici öğrenme için tutulacak geçici değişken
pending_question = None

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def process_message(message):
    global pending_question
    memory = load_memory()

    # Eğer bir önceki mesaj cevapsız kaldıysa, kullanıcıdan gelen yanıtı kaydeder
    if pending_question:
        memory[pending_question] = message.strip()
        save_memory(memory)
        response = f"Teşekkürler! Artık '{pending_question}' sorusunu biliyorum. ✅"
        pending_question = None
        return response

    message_lower = message.strip().lower()
    if message_lower in memory:
        return memory[message_lower]
    else:
        pending_question = message_lower
        return "Bunu bilmiyorum. Ne demek istedin? 🤔"
