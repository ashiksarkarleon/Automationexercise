import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def hw_test_case_8():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Launch browser successfully")
    driver.get("https://automationexercise.com")
    print("Navigate to url http://automationexercise.com successfully")

    try:
        assert "Automation Exercise" in driver.title, f"It's not Login page. Title Mismatch"
        print("Home page visible successfully")

        # Click Products button
        try:
            products_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(2) > a")))
            products_button.click()

            assert "https://automationexercise.com/products" in driver.current_url, \
                f"It's not Products page. Title Mismatch"
            print("Navigated PRODUCTS page successfully")

            # navigated to ALL PRODUCTS page
            try:
                status = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-center.title")))
                v_1 = f"{'ALL PRODUCTS'}"
                v_2 = f"Logged in as {status.text}"
                assert v_1 in v_2, f"Verify user is navigated to ALL PRODUCTS page failed."
                print("Navigated to ALL PRODUCTS page successfully")

            except Exception as e:
                print("Verify user is navigated to ALL PRODUCTS page Exception: ", type(e).__name__)

        except Exception as e:
            print("Products button Exception: ", type(e).__name__)

        # Search Input Field
        try:
            search_input_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_product")))
            search_input_field.send_keys("blue top")

        except Exception as e:
            print("Search Input Field Exception: ", type(e).__name__)

        # Search button
        try:
            search_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit_search")))
            search_button.click()

        except Exception as e:
            print("Search button Exception: ", type(e).__name__)

        # Verify SEARCHED PRODUCTS
        print(driver.current_url)
        try:
            assert "https://automationexercise.com/products?search=blue%20top" in driver.current_url, \
                f"item not found"
            print("Item Found SEARCHED PRODUCTS is visible successfully")

        except Exception as e:
            print("Verify SEARCHED PRODUCTS Exception: ", type(e).__name__)

        time.sleep(3)

        print("Exit Code")

    except Exception as e:
        print("Home page Exception: ", type(e).__name__)


hw_test_case_8()
