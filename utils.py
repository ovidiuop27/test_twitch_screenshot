from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Removes an element from the DOM given its XPath.
def remove_element_by_xpath(driver, xpath):
    try:
        driver.execute_script(
            f"var element = document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; "
            "if (element) element.parentNode.removeChild(element);"
        )
    except Exception as e:
        print(f"Error removing element at {xpath}: {e}")


# Returns the position of an element relative to the viewport.
def get_position_relative_to_viewport(driver, element):
    position = driver.execute_script(""" 
        var elem = arguments[0];
        var rect = elem.getBoundingClientRect();
        return {
            top: rect.top,
            left: rect.left
        };
    """, element)
    return position


# Waits for an element containing the specified text to appear on the page.
def wait_for_element_with_text(driver, text, timeout=10):
    try:
        xpath = f"//*[contains(text(), '{text}')]"
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
    except Exception as e:
        print(f"Error waiting for element containing text '{text}':", e)


# Scrolls down by a specified pixel amount a set number of times with an optional delay.
def scroll_down(driver, pixels, repeat=1, delay=1):
    for _ in range(repeat):
        driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(delay)
