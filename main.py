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

# Open Microsoft Edge
subprocess.Popen([edge_path])

# Allow some time for the browser to open
time.sleep(5)

# Perform 30 searches with random queries using the Windows button for input
for _ in range(30):
    random_query = generate_random_query()
    
    # Press Windows key to open search
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    
    # Type the random query
    pyautogui.write(random_query)
    time.sleep(1)
    
    # Press Enter to perform the search
    pyautogui.press('enter')
    
    # Allow some time for the search to complete and open a new tab
    time.sleep(30)

# Close all tabs using Ctrl+W
for _ in range(30):
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

# Close Microsoft Edge
os.system("taskkill /IM msedge.exe /F")
