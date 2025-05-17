# Project Structure:
#
# Automated-Edge-Search/
# ├── main.py                  # Main script to run
# ├── requirements.txt         # Dependencies
# ├── README.md                # Documentation
# └── src/
#     ├── __init__.py          # Makes the folder a package
#     ├── search_engine.py     # Core search functionality
#     ├── browser_handler.py   # Browser management
#     └── utils.py             # Utility functions

"""
Main script to run the Windows search automation
"""

import os
import sys
import time
from src.search_engine import WindowsSearchAutomation

def display_welcome():
    """Display welcome message with usage instructions"""
    print("\n" + "=" * 60)
    print("Windows Search Automation Tool".center(60))
    print("=" * 60)
    print("\nThis script will:")
    print("1. Simulate pressing the Windows key")
    print("2. Search for random terms (10+ characters)")
    print("3. Open each search in Microsoft Edge")
    print("4. Complete 35 searches with 10-second intervals")
    print("5. Close all tabs when finished")
    print("\nRequirements:")
    print("- Windows OS")
    print("- Microsoft Edge browser")
    print("- Required Python packages (see requirements.txt)")
    print("\nPress Ctrl+C at any time to stop the script.")
    print("=" * 60 + "\n")

def main():
    """Main function to execute the automation"""
    display_welcome()
    
    # Confirm before running
    response = input("Begin search automation? (y/n): ").lower()
    if response != 'y':
        print("Script execution cancelled.")
        return
    
    # Setup and run automation
    try:
        print("\nStarting automation in 5 seconds...")
        print("IMPORTANT: Make sure you don't move your mouse or use your keyboard during execution!")
        print("The script needs to control your keyboard to simulate Windows key presses and typing.")
        for i in range(5, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(1)
        print("\n")
        
        # Initialize and run the automation
        search_automation = WindowsSearchAutomation(
            search_count=35,
            delay_between_searches=10
        )
        search_automation.run()
        
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
    finally:
        print("\nScript execution complete.")

if __name__ == "__main__":
    # Add the project directory to the path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()