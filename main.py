import subprocess
import time
import random
import string
import os
import pyautogui

# Function to generate a random query
def generate_random_query(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Path to Microsoft Edge executable
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# URL of Microsoft Bing
bing_url = "https://www.bing.com/search?q="

# Open Microsoft Edge
subprocess.Popen([edge_path])

# Allow some time for the browser to open
time.sleep(5)

# Perform 30 searches with random queries
for _ in range(30):
    random_query = generate_random_query()
    search_url = bing_url + random_query
    subprocess.Popen([edge_path, search_url])
    time.sleep(30)

# Close all tabs using Ctrl+W
for _ in range(31):
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

# Close Microsoft Edge
os.system("taskkill /IM msedge.exe /F")
