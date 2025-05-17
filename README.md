# Windows Search Automation

An automated tool that simulates Windows search and performs multiple searches that open in Microsoft Edge browser.

## Features

- Simulates pressing the Windows key to open Windows search
- Types random search terms (10+ characters) in the Windows search bar
- Press Enter to open each search in Microsoft Edge
- Performs 35 searches with 7-second intervals
- Automatically closes all Edge windows when complete

## How It Works

1. The script presses the Windows key to open the Windows search bar
2. It types a random search term directly in the Windows search bar
3. It presses Enter, which launches the search in Microsoft Edge
4. It waits 10 seconds before repeating with a new search term
5. After 35 searches, it closes all Edge windows

## Folder Structure

```
Automated-Edge-Search/
├── main.py                  # Main script to run
├── requirements.txt         # Dependencies
├── README.md                # Documentation
└── src/
    ├── __init__.py          # Makes the folder a package
    ├── search_engine.py     # Core search functionality 
    ├── browser_handler.py   # Browser management
    └── utils.py             # Utility functions
```

## Requirements

- Windows operating system
- Microsoft Edge browser (set as default browser for searches)
- Python 3.7 or higher
- PyAutoGUI package

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```
   cd Automated-Edge-Search
   ```
3. Create a virtual environment with custom name:
   ```
   python -m venv auto_edge_search_venv
   auto_edge_search_venv\Scripts\activate
   ```
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Make sure Microsoft Edge is installed on your system
2. Activate the virtual environment:
   ```
   auto_edge_search_venv\Scripts\activate
   ```
3. Run the script from the command line:
   ```
   python main.py
   ```
4. Follow the prompts to start the automation
5. The script will:
   - Initialize the Edge browser
   - Perform 35 random searches with 10-second intervals
   - Close all browser tabs when complete

## Important Notes

- Do not interact with your computer while the script is running
- You can press Ctrl+C at any time to stop the script
- If the script is interrupted, it will attempt to close any open browser instances
- For the searches to count properly, ensure you are logged into your Microsoft/Bing account in Edge

## Troubleshooting

- If the script cannot find Edge, make sure it's installed in the default location
- If you encounter WebDriver errors, try updating the selenium package:
  ```
  pip install --upgrade selenium
  ```
- If the Windows key simulation doesn't work, try running the script as Administrator
- If you encounter permission issues with the virtual environment:
  ```
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
