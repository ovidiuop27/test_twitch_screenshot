import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import remove_element_by_xpath, get_position_relative_to_viewport, wait_for_element_with_text, scroll_down


@pytest.mark.parametrize("search_term", ["StarCraft II"])
def test_twitch_search_streamer(driver, search_term):
    # Step 1: Go to Twitch
    driver.get("https://www.twitch.tv/")
    wait = WebDriverWait(driver, 10)

    # Wait for the LIVE logo to appear
    wait_for_element_with_text(driver, 'LIVE')

    # Step 2: Remove the blocking element (issue explained in the readme file)
    blocking_elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div[3]')
    if len(blocking_elements) > 0:
        blocking_element_xpath = '//*[@id="root"]/div[3]'
        remove_element_by_xpath(driver, blocking_element_xpath)

    # Step 3: Click on the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/a')))
    search_icon.click()

    # Step 4: Input search term
    search_box = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="page-main-content-wrapper"]/nav/div/div/div[2]/div/div/input')))
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Step 5: Scroll down twice
    scroll_down(driver, 200, repeat=2)

    # Step 6: Select one streamer
    # Find all elements containing the word "viewers"
    viewers_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'viewers')]")
    # Iterate through the elements and click on the first one that is in the viewport
    for element in viewers_elements:
        element_position = get_position_relative_to_viewport(driver, element)
        try:
            if element_position["left"] > 10 and element_position["top"] > 100:
                element.click()
                break
        except Exception as e:
            print("Error checking element:", e)

    # Step 7: Click "Start Watching" if present
    try:
        start_watching_buttons = driver.find_elements(By.XPATH, '//*[contains(text(), "Start Watching")]')
        if start_watching_buttons:
            start_watching_button = start_watching_buttons[0]
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(start_watching_button))
            start_watching_button.click()
    except Exception as e:
        print("Error checking element:", e)

    # Step 8: Wait until the page is fully loaded (in our case, we'll wait for the LIVE logo to appear)
    wait_for_element_with_text(driver, 'LIVE')

    # Step 9: Take screenshot after page loads
    driver.save_screenshot("streamer_page.png")
