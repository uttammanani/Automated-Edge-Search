"""
Core search functionality for Windows search automation
"""

import time
import string
import random
import pyautogui
from src.browser_handler import EdgeBrowserHandler
from src.utils import generate_random_search_term

class WindowsSearchAutomation:
    """Class to handle Windows search automation"""
    
    def __init__(self, search_count=35, delay_between_searches=6, min_term_length=10, max_term_length=15):
        """
        Initialize the search automation
        
        Args:
            search_count (int): Number of searches to perform
            delay_between_searches (int): Delay in seconds between searches
            min_term_length (int): Minimum length of search terms
            max_term_length (int): Maximum length of search terms
        """
        self.search_count = search_count
        self.delay = delay_between_searches
        self.min_term_length = min_term_length
        self.max_term_length = max_term_length
        self.search_terms = []
        self.browser_handler = EdgeBrowserHandler()
        self.tabs_opened = 0
        
    def _generate_search_terms(self):
        """Generate random search terms for all searches"""
        print("Generating random search terms...")
        self.search_terms = [
            generate_random_search_term(self.min_term_length, self.max_term_length) 
            for _ in range(self.search_count)
        ]
        
    def _press_windows_key(self):
        """Simulate pressing the Windows key"""
        print("Opening Windows search bar...")
        pyautogui.press('win')
        time.sleep(0.8)  # Wait for search to appear
        
    def _type_search_term(self, term):
        """Type the search term and press Enter"""
        print(f"Typing search term: '{term}'")
        pyautogui.write(term)
        time.sleep(0.8)  # Wait a moment after typing
        
    def _auto_click_search_result(self):
        """Automatically click on the first search result"""
        print("Automatically clicking on the search result...")
        
        # Wait a moment for search results to appear
        time.sleep(1)
        
        # Press down arrow to select the first search result
        pyautogui.press('down')
        time.sleep(0.5)
        
        # Press Enter to select it
        pyautogui.press('enter')
        time.sleep(0.5)
        
        # Increment the tabs opened counter
        self.tabs_opened += 1
        
    def run(self):
        """Run the full search automation process"""
        try:
            # Generate search terms
            self._generate_search_terms()
            
            # Initialize browser handler (but don't open the browser directly)
            # Edge will be launched automatically by Windows search
            self.browser_handler.initialize_tracking()
            
            # Perform searches through Windows search
            for i, term in enumerate(self.search_terms):
                current_num = i + 1
                print(f"Search {current_num}/{self.search_count}: '{term}'")
                
                # Method via Windows search - this is the requested workflow
                self._press_windows_key()  # Open Windows search bar
                time.sleep(1)  # Wait for search to fully appear
                self._type_search_term(term)  # Type the search term
                
                # Automatically click on the search result
                self._auto_click_search_result()
                
                # Wait for Edge to open and load the search
                time.sleep(2)
                
                # Wait between searches if not the last one
                if i < self.search_count - 1:
                    print(f"Waiting {self.delay} seconds...")
                    time.sleep(self.delay)
            
            # Complete
            print(f"\nAll {self.search_count} searches completed!")
            print("Waiting 5 seconds before closing tabs...")
            time.sleep(5)
            
            try:
                # Close tabs one by one instead of closing all Edge windows at once
                self.browser_handler.close_tabs_one_by_one(self.tabs_opened)
                print("All Microsoft Edge tabs have been closed.")
            except Exception as e:
                print(f"Error when closing tabs one by one: {e}")
                print("Falling back to closing all Edge windows...")
                self.browser_handler.close_all_edge_windows()
            
        except Exception as e:
            print(f"Error during automation: {e}")
            # Attempt to close browser even if there was an error
            self.browser_handler.close_browser()
            raise