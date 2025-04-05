import time
import os

def ghosttrace_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(r"""
 ██████╗  ██████╗  ██████╗ ███████╗████████╗████████╗██████╗  █████╗  ██████╗███████╗
██╔════╝ ██╔═══██╗██╔════╝ ██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ███╗██║   ██║██║  ███╗█████╗     ██║      ██║   ██████╔╝███████║██║     █████╗  
██║   ██║██║   ██║██║   ██║██╔══╝     ██║      ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝███████╗   ██║      ██║   ██║  ██║██║  ██║╚██████╗███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

                   GhostTrace LLM Recon Platform · DarkGPT Ops Ready 🧠💻⚔️
    """)
    print("🕵️  Initializing darknet recon tools...")
    time.sleep(1)
    print("🔧 TOR routing established...")
    time.sleep(1)
    print("🧠 WormGPT LLM loaded into memory.")
    time.sleep(1)
    print("🕷️  Scanning .onion targets...\n")

# Call the banner at the top of your script
ghosttrace_banner()

import socks
import socket
import requests
from bs4 import BeautifulSoup

# Route traffic through TOR
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# List of .onion targets (examples, replace with real ones)
targets = [
    "http://dnj6totzep26bvgv.onion",
    "http://darkmarketxyzxyz.onion",
]

for url in targets:
    try:
        print(f"🕵️ Crawling {url} ...")
        res = requests.get(url, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.get_text()[:1000]
        print(f"\n🧠 Preview: \n{content}\n")
    except Exception as e:
        print(f"[!] Failed to fetch {url}: {e}")
import json
import subprocess

# Pipe scraped text into WormGPT
def summarize_with_llm(text):
    payload = {
        "model": "wormgpt",
        "prompt": f"Summarize this darknet post and classify its intent:\n{text}"
    }
    response = subprocess.check_output([
        "curl", "-s", "-X", "POST",
        "http://localhost:11434/api/generate",
        "-d", json.dumps(payload)
    ])
    print("\n🧠 WormGPT Analysis:\n", response.decode())

# After parsing the page...
summarize_with_llm(content)
