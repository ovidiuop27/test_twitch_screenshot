# Twitch Test Automation Project
This project automates a series of interactions on Twitch's website using Selenium and pytest.
It runs a test to search for StarCraft II streamers, navigate to a stream page, handle any pop-ups, and take a screenshot once the page has fully loaded.

## Overview
The automated test performs the following steps:
- Launches the Twitch homepage in a Google Chrome mobile emulator.
- Searches for "StarCraft II"
- Navigates to a stream, handles potential pop-ups, and captures a screenshot of the loaded streamer page.

## Prerequisites
- Google Chrome (for browser automation)
- ChromeDriver compatible with your Chrome version
- Python 3.x
    - Selenium
    - Pytest

## Python Packages
The required packages are listed in requirements.txt. Install them with:
<br>```bash: pip install -r requirements.txt```

## Project Structure
```
.
├── conftest.py                # Setup and session management for pytest
├── requirements.txt           # Python dependencies
├── test_twitch_screenshot.py   # Main test script for Twitch interactions
└── utils.py                   # Utility functions for handling elements and scrolling
```
## Running the test
```bash: pytest -v```

## Test Workflow
1. Navigate to Twitch: The test opens https://www.twitch.tv/.
2. Handle Elements on the Page:
    - If an overlay element blocks the page, it is removed to ensure accessibility to the search icon.
3. Search for a `"StarCraft II"` in the search field and submits the query.
4. Scroll Down: Scrolls down twice to load more search results.
5. Select a Stream: Clicks on the first stream displaying the word `"viewers"` that is fully visible.
6. Handle Optional Pop-ups: Detects and clicks a `"Start Watching"` button if it appears.
7. Take Screenshot: After ensuring the stream page has fully loaded, it captures a screenshot of the page.

## Notes and Known Issues
- Pop-ups: Some streamers may display a modal or pop-up before the stream loads. The test script attempts to handle this by clicking the `"Start Watching"` button if it appears.
- Blocking Elements: Twitch's dynamic interface may include elements that obscure the search icon, in our case the Cookie confirm pop-up can't be closed when the browser is in mobile mode. The test script removes this element if detected, enabling the search function.
- Execution Environment: The test is designed for Chrome’s mobile emulator (iPhone XR).