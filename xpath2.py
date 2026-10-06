from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("=== Practical 6 : XPath - II ===")

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    driver.get(
        "https://practicetestautomation.com/practice-test-login/"
    )

    username = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@id='username' and @name='username']"
            )
        )
    )

    username.send_keys("student")
    print("AND Operator : Username Entered")

    password = driver.find_element(
        By.XPATH,
        "//input[@id='password' or @name='password']"
    )

    password.send_keys("Password123")
    print("OR Operator : Password Entered")

    driver.find_element(By.ID, "submit").click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1")
        )
    )

    print("Login Successful")

    self_axis = driver.find_element(
        By.XPATH,
        "//h1/self::h1"
    )

    print("Self Axis :", self_axis.tag_name)

    parent = driver.find_element(
        By.XPATH,
        "//h1/parent::*"
    )

    print("Parent Axis :", parent.tag_name)

    child = driver.find_element(
        By.XPATH,
        "//article/child::*[1]"
    )

    print("Child Axis :", child.tag_name)

    desc = driver.find_element(
        By.XPATH,
        "//article/descendant::h1"
    )

    print("Descendant Axis :", desc.text)

    desc_self = driver.find_element(
        By.XPATH,
        "//h1/descendant-or-self::h1"
    )

    print(
        "Descendant-or-self :",
        desc_self.tag_name
    )

    follow = driver.find_element(
        By.XPATH,
        "//h1/following::a[1]"
    )

    print("Following Axis :", follow.text)

    precede = driver.find_element(
        By.XPATH,
        "//a/preceding::h1[1]"
    )

    print("Preceding Axis :", precede.text)

    print("Practical Completed Successfully")

finally:
    driver.quit()