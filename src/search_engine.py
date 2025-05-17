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
    
    def __init__(self, search_count=35, delay_between_searches=7, min_term_length=10, max_term_length=15):
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
        print("Pressing Enter to search...")
        pyautogui.press('enter')
        time.sleep(2)  # Wait for search to launch in Edge
        
    def _open_edge_with_search(self, term):
        """Open Microsoft Edge with the search term"""
        return self.browser_handler.open_search_tab(term)
        
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
                self._type_search_term(term)  # Type and press Enter
                
                # Wait for Edge to open and load the search
                time.sleep(2)
                
                # Wait between searches if not the last one
                if i < self.search_count - 1:
                    print(f"Waiting {self.delay} seconds...")
                    time.sleep(self.delay)
            
            # Complete
            print(f"\nAll {self.search_count} searches completed!")
            print("Waiting 10 seconds before closing tabs...")
            time.sleep(10)
            
            # Close all Edge browser windows
            self.browser_handler.close_all_edge_windows()
            print("All Microsoft Edge windows have been closed.")
            
        except Exception as e:
            print(f"Error during automation: {e}")
            # Attempt to close browser even if there was an error
            self.browser_handler.close_browser()
            raise