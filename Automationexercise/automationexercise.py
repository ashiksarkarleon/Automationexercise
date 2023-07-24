import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def test_login(name, email):
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Launch browser successfully")
    driver.get("https://automationexercise.com")
    print("Navigate to url http://automationexercise.com successfully")

    try:
        assert "Automation Exercise" in driver.title, f"It's not Login page. Title Mismatch"
        print("Home page visible successfully")

        # Click Signup_Login button
        try:
            signup_login_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")))
            signup_login_button.click()
            assert "https://automationexercise.com/login" in driver.current_url, \
                f"It's not Signup Login page. Title Mismatch"
            print("Signup Login page visible successfully")
            print("'New User Signup!' is visible Successfully")

        except Exception as e:
            print("Signup Login button Exception: ", type(e).__name__)

        # SignUp Name Field
        try:
            signup_name_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))
            signup_name_field.send_keys(name)
            print("Sign Up Name Field successfully")
        except Exception as e:
            print("signup name field field Exception: ", type(e).__name__)

        # SignUp Email Field
        try:
            signup_email_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))
            signup_email_field.send_keys(email)
            print("Sign Up Email Field successfully")
        except Exception as e:
            print("signup email field Exception: ", type(e).__name__)

        # SignUp Button Field
        try:
            signup_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))
            signup_button.click()
            print("Sign Up Button Click successfully")
        except Exception as e:
            print("SignUp button Exception: ", type(e).__name__)

        # Verify SignUp ENTER ACCOUNT INFORMATION
        assert "Automation Exercise - Signup" in driver.title, f"SignUp ENTER ACCOUNT INFORMATION failed."
        print("SignUp ENTER ACCOUNT INFORMATION Visible Successful.")

        # Title Field
        try:
            title_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#id_gender2")))
            title_field.click()
            print("Title Field successfully")
        except Exception as e:
            print("Title Field Exception: ", type(e).__name__)

        # Password Field
        try:
            signup_password_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
            signup_password_field.send_keys("123456789")
            print("Password Field successfully")
        except Exception as e:
            print("Password field Exception: ", type(e).__name__)

        # Date of Birth Field

        # Days Filed
        try:
            day_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#days")))
            select_day = Select(day_field)
            select_day.select_by_value("5")
            print("Days Field successfully")
        except Exception as e:
            print("Days Field Exception: ", type(e).__name__)

        # Months Filed
        try:
            month_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#months")))
            select_month = Select(month_field)
            select_month.select_by_value("6")
            print("Months Field successfully")
        except Exception as e:
            print("Months Field Exception: ", type(e).__name__)

        # Years Filed
        try:
            year_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#years")))
            select_year = Select(year_field)
            select_year.select_by_value("2020")
            print("Years Field successfully")
        except Exception as e:
            print("Years Field Exception: ", type(e).__name__)

        # Checkbox newsletter Field
        try:
            news_letter_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#newsletter")))
            news_letter_field.click()
            print("News Letter Field successfully")
        except Exception as e:
            print("News Letter Field Exception: ", type(e).__name__)

        # Checkbox special offers Field
        try:
            special_offers_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#optin")))
            special_offers_field.click()
            print("Special Offers Field successfully")
        except Exception as e:
            print("Special Offers Field Exception: ", type(e).__name__)

        # ADDRESS INFORMATION
        # FirstName Field
        try:
            firstname_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#first_name")))
            firstname_field.send_keys("johan")
            print("FirstName Field successfully")
        except Exception as e:
            print("FirstName field field Exception: ", type(e).__name__)

        # LastName Field
        try:
            lastname_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#last_name")))
            lastname_field.send_keys("ali")
            print("LastName Field successfully")
        except Exception as e:
            print("LastName Field Exception: ", type(e).__name__)

        # Company Field
        try:
            company_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#company")))
            company_field.send_keys("Khan Corporation")
            print("Company Field successfully")
        except Exception as e:
            print("Company Field Exception: ", type(e).__name__)

        # Address Field
        try:
            address_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address1']")))
            address_field.send_keys("Satartkul, PO: Badda")
            print("Address Field successfully")
        except Exception as e:
            print("Address Field Exception: ", type(e).__name__)

        # Address 2 Field
        try:
            address_2_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address2']")))
            address_2_field.send_keys("Greee Road, Dhaka")
            print("Address 2 Field successfully")
        except Exception as e:
            print("Address 2 Field Exception: ", type(e).__name__)

        # Country Field
        try:
            country_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='country']")))
            select_country = Select(country_field)
            select_country.select_by_value("Canada")
            print("Country Field successfully")
        except Exception as e:
            print("Country Field Exception: ", type(e).__name__)

        # State Field
        try:
            state_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#state")))
            state_field.send_keys("Dhaka")
            print("State Field successfully")
        except Exception as e:
            print("State Field Exception: ", type(e).__name__)

        # City Field
        try:
            city_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#city")))
            city_field.send_keys("Badda")
            print("City Field successfully")
        except Exception as e:
            print("City Field Exception: ", type(e).__name__)

        # Zip Code Field
        try:
            zip_code_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#zipcode")))
            zip_code_field.send_keys("4545")
            print("Zip Code Field successfully")
        except Exception as e:
            print("Zip Code Field Exception: ", type(e).__name__)

        # Mobile Phone Field
        try:
            mobile_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#mobile_number")))
            mobile_field.send_keys("+8801784585584")
            print("Mobile Phone Field successfully")
        except Exception as e:
            print("Mobile Phone Field Exception: ", type(e).__name__)

        # Create Account Button Field
        try:
            create_account_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
            create_account_button.click()
            print("Create Account Click successfully")
        except Exception as e:
            print("Create Account Exception: ", type(e).__name__)

        # Verify ACCOUNT CREATED!
        try:
            assert "https://automationexercise.com/account_created" in driver.current_url, \
                f"It's not Verify ACCOUNT CREATED page. URL Mismatch"
            print("ACCOUNT CREATED Page visible successfully")

            account_created_status = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
            print(account_created_status.text)
            ac_status_1 = "ACCOUNT CREATED!"
            ac_status_2 = f"{account_created_status.text}"
            assert ac_status_1 in ac_status_2, f"Verify ACCOUNT CREATED! Visible failed."
            print("Verify ACCOUNT CREATED! Visible Successful.")

        except Exception as e:
            print("ACCOUNT CREATED Page Exception: ", type(e).__name__)

        # Continue Button
        try:
            continue_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
            continue_button.click()
            print("Continue Button Click successfully")
        except Exception as e:
            print("Continue Button Exception: ", type(e).__name__)

        # Verify that 'Logged in as username' is visible
        try:
            # status_1 = WebDriverWait(driver, 10, poll_frequency=2).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
            status_2 = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "b")))
            v_1 = f"Logged in as {name}"
            v_2 = f"Logged in as {status_2.text}"
            print(v_1+v_2)
            assert v_1 in v_2, f"Verify that 'Logged in as username' failed."
            print(f"Verify that Logged in as {status_2.text} is visible Successful.")

        except Exception as e:
            print("Verify that 'Logged in as username' Exception: ", type(e).__name__)

        time.sleep(3)

    except Exception as e:
        print("Home page Exception: ", type(e).__name__)


def generate_random_email(length):
    domain_name = ['gmail', 'yahoo', 'icloud', 'hotmail']
    postfix = ['.com', '.org', '.bd', '.edu']
    characters = string.ascii_letters + string.digits
    domain_select = random.choice(domain_name)
    postfix_select = random.choice(postfix)
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting + "@" + domain_select + postfix_select


def generate_random_name(length):
    characters = string.ascii_letters + string.digits
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting


test_login(f"{generate_random_name(5)}", f"{generate_random_email(5)}")
