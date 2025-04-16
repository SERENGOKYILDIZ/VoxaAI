import json
import os

MEMORY_FILE = "./data/memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def process_message(message):
    memory = load_memory()
    if message.startswith("/learn"):
        try:
            _, question, answer = message.split("::", 2)
            memory[question.strip().lower()] = answer.strip()
            save_memory(memory)
            return "Öğrendim! ✅"
        except ValueError:
            return "Hatalı öğrenme formatı. Doğru kullanım: /learn::soru::cevap"
    else:
        return memory.get(message.strip().lower(), "Bunu bilmiyorum. 🤖 /learn komutuyla öğretebilirsin.")
