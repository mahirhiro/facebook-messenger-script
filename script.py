import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'mahirhiro'
PASSWORD = 'password'
PATH = './drivers/chromedriver'
URL = 'https://business.facebook.com/reducept/inbox/?business_id=641855079929'
driver = webdriver.Chrome(PATH)

driver.get(URL)

# Get and enters the email address
email = driver.find_element_by_id('email')
email.send_keys(USERNAME)

# Get and enters the password address
password = driver.find_element_by_id('pass')
password.send_keys(PASSWORD)

# Gets and clicks the login button
submit = driver.find_element_by_id('loginbutton')
submit.click()

# Navigates to the messenger button
messenger_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[1]/div/div[1]/div[1]/a'))
)
messenger_button.click()

# Waits until all the list of unread messages loads
messenger_button = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, '_5m17'))
)

# Gets the users in a list
list = driver.find_elements_by_class_name("_5m17")

# The for loop loops through the users and marks the conversation as done based on a certain message
for x in range(0, len(list)):
    try:
        time.sleep(2)
        if list[x].is_displayed():
            list[x].click()

            # Waits until the 'mark as done' button on facebook business appears
            final = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[3]/div/div[1]/div[1]/div/div/div[3]/div/div[6]'))
            )
            # Gets the 'mark as done' button on facebook business to be able to move a converation to another folder
            shit = mark_as_done = driver.find_element_by_xpath('//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[3]/div/div[1]/div[1]/div/div/div[3]/div/div[6]')
            shit.click()

    except exceptions.StaleElementReferenceException as e:
        # Gets the 'mark as done' button on facebook business to be able to move a converation to another folder
        shit = mark_as_done = driver.find_element_by_xpath(
            '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[3]/div/div[1]/div[1]/div/div/div[3]/div/div[6]')
        shit.click()
print('hi')

