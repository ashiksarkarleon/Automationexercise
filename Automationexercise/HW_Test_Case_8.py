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

        # Click View Product button
        try:
            view_products_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .choose > .nav.nav-justified.nav-pills  a")))
            view_products_button.click()
            print("Click 'View Product' of first product Successfully")

        except Exception as e:
            print("View Products button Exception: ", type(e).__name__)

        # product detail page
        try:
            assert "Automation Exercise - Product Details" in driver.title, f"It's not product detail page. Title Mismatch"
            print("Product detail page visible successfully")

        except Exception as e:
            print("Product detail page Exception: ", type(e).__name__)

        # product name field
        try:
            product_name_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-information h2")))
            v_1 = f"{'Blue Top'}"
            v_2 = f"{product_name_field.text}"
            assert v_1 in v_2, f"Product Name Field failed."
            print("Product Name Field Successfully")

        except Exception as e:
            print("Product Name Field Exception: ", type(e).__name__)

        # category field
        try:
            category_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-information p:nth-child(3)")))
            v_1 = f"{'Category: Women > Tops'}"
            v_2 = f"{category_field.text}"
            assert v_1 in v_2, f"Category Field failed."
            print("Category Field Successfully")

        except Exception as e:
            print("Category Field Exception: ", type(e).__name__)

        # Price field
        try:
            price_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span > span")))
            v_1 = f"{'Rs. 500'}"
            v_2 = f"{price_field.text}"
            assert v_1 in v_2, f"Price Field failed."
            print("Price Field Successfully")

        except Exception as e:
            print("Price Field Exception: ", type(e).__name__)

        # Availability field
        try:
            availability_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-information p:nth-child(6)")))
            v_1 = f"{'Availability: In Stock'}"
            v_2 = f"{availability_field.text}"
            assert v_1 in v_2, f"Availability Field failed."
            print("Availability Field Successfully")

        except Exception as e:
            print("Availability Field Exception: ", type(e).__name__)

        # Condition field
        try:
            condition_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-information p:nth-child(7)")))
            v_1 = f"{'Condition: New'}"
            v_2 = f"{condition_field.text}"
            assert v_1 in v_2, f"Condition Field failed."
            print("Condition Field Successfully")

        except Exception as e:
            print("Condition Field Exception: ", type(e).__name__)

        # Brand field
        try:
            brand_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-information p:nth-child(8)")))
            v_1 = f"{'Brand: Polo'}"
            v_2 = f"{brand_field.text}"
            assert v_1 in v_2, f"Brand Field failed."
            print("Brand Field Successfully")

        except Exception as e:
            print("Brand Field Exception: ", type(e).__name__)

        time.sleep(3)

        print("Exit Code")

    except Exception as e:
        print("Home page Exception: ", type(e).__name__)


hw_test_case_8()
