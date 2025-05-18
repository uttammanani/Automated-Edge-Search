"""
Browser handling functionality for Edge automation via Windows search
"""

import time
import os
import pyautogui

class EdgeBrowserHandler:
    """Class to handle Microsoft Edge browser automation"""
    
    def __init__(self):
        """Initialize the browser handler"""
        # No driver needed as we'll use Windows to launch Edge
    
    def initialize_tracking(self):
        """Initialize tracking of Edge browser without opening it directly"""
        try:
            print("Setting up to track Microsoft Edge windows...")
            return True
            
        except Exception as e:
            print(f"Error setting up Edge tracking: {e}")
            return False
    
    def close_all_edge_windows(self):
        """Close all Microsoft Edge windows using process management"""
        try:
            print("Attempting to close all Microsoft Edge windows...")
            # Find all Edge processes
            os.system('taskkill /f /im msedge.exe')
            return True
            
        except Exception as e:
            print(f"Error closing Edge windows: {e}")
            return False
    
    def close_tabs_one_by_one(self, tab_count):
        """Close Edge tabs one by one using Ctrl+W"""
        try:
            print(f"Closing {tab_count} Edge tabs one by one...")
            
            # Give focus to Edge browser before closing tabs
            # Wait a moment for any open Edge window to be in focus
            time.sleep(1)
            
            # Close each tab with Ctrl+W
            for i in range(tab_count):
                print(f"Closing tab {i+1}/{tab_count}...")
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(0.5)  # Brief pause between tab closures
            
            print("All tabs closed successfully.")
            return True
            
        except Exception as e:
            print(f"Error closing tabs one by one: {e}")
            return False
    
    def close_all_tabs(self):
        """Legacy method - now just an alias to close_all_edge_windows"""
        return self.close_all_edge_windows()
    
    def close_browser(self):
        """Close the browser completely - now just an alias to close_all_edge_windows"""
        return self.close_all_edge_windows()