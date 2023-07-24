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

        # Cart button
        try:
            cart_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > a")))
            cart_button.click()
            print("Cart button clicked successfully")

        except Exception as e:
            print("Cart button Exception: ", type(e).__name__)

        # Scroll Down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scroll Down successfully")

        # Subscription field
        try:
            subscription_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))
            v_1 = f"{'Subscription'}"
            v_2 = f"{subscription_field.text}"
            assert v_1 in v_2, f"Subscription Field failed."
            print("Subscription Field Verify Successfully")

        except Exception as e:
            print("Subscription Field Exception: ", type(e).__name__)

        # Email Input Field
        try:
            email_input_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input#susbscribe_email")))
            email_input_field.send_keys("a@gmail.com")
            print("Email Field Successfully")

        except Exception as e:
            print("Search Input Field Exception: ", type(e).__name__)

        # Arrow button
        try:
            arrow_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#subscribe")))
            arrow_button.click()
            print("Arrow button clicked successfully")

            # Verify success message
            try:
                message_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
                v_1 = f"{'You have been successfully subscribed!'}"
                v_2 = f"{message_field.text}"
                assert v_1 in v_2, f"Verify success message Field failed."
                print("Verify Done, You have been successfully subscribed!")

            except Exception as e:
                print("Verify success message Exception: ", type(e).__name__)

        except Exception as e:
            print("Arrow button Exception: ", type(e).__name__)

        time.sleep(3)

        print("Exit Code")

    except Exception as e:
        print("Home page Exception: ", type(e).__name__)


hw_test_case_8()
