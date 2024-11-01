# Twitch Screenshot Test

Automated tests for Twitch streamer search using Selenium.

## Requirements

- Python 3.x
- Selenium
- Pytest

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ovidiuop27/test_twitch_screenshot.git
    cd test_twitch_screenshot

2. Install the required packages:
    pip install -r requirements.txt

3. Run the tests:
    To run the test, execute the following command in your terminal:
    pytest test_twitch_screenshot.py

## Test Steps for Twitch Streamer Automation

1. Go to Twitch:
   - Use the Selenium WebDriver to navigate to the Twitch homepage.

2. Remove the Blocking Element:
   - Identify and remove any blocking elements that may prevent interaction with the page.

3. Click on the Search Icon:
   - Locate and click on the search icon in the Twitch navigation.

4. Input Search Term:
   - Enter "StarCraft II" into the search input field and submit the search.

5. Scroll Down Twice:
   - Scroll down the page twice to load more content using JavaScript.

6. Identify Live Streams Using Viewers Text:
   - Check all elements containing the word "viewers" to determine which streams are live, and select one to click on.

7. Handle the "Start Watching" Pop-Up (Optional):
   - Wait for the "Start Watching" button to appear. If it appears, click on the button to proceed. If not, continue to the next step.

8. Wait Until the Page is Fully Loaded:
   - Wait for the "LIVE" logo to become visible, ensuring the streamer’s page has fully loaded.

9. Take a Screenshot:
   - Capture a screenshot of the streamer’s page for verification.
