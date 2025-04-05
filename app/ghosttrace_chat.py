import requests
import json

def chat_with_llm(prompt):
    payload = {
        "model": "ghosttrace-llm",
        "prompt": prompt
    }
    r = requests.post("http://localhost:11434/api/generate", json=payload)
    return r.text
