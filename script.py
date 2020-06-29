import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

USERNAME = input("Enter a USERNAME: ")
PASSWORD = getpass.getpass("Enter a PASSWORD: ")
MESSAGE = input("Enter a message to be marked as done: ")
PATH = './drivers/chromedriver'
URL = 'https://business.facebook.com/reducept/inbox/?business_id=641855079929'
driver = webdriver.Chrome(PATH)
driver.get(URL)


def mark_message_as_done():
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[3]/div/div[1]/div[1]/div/div/div[3]/div/div[6]'))
    )

    button_to_click_as_done = driver.find_element_by_xpath(
        '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[3]/div/div[1]/div[1]/div/div/div[3]/div/div[6]')
    button_to_click_as_done.click()


def login():
    # Get and enters the email address
    email = driver.find_element_by_id('email')
    email.send_keys(USERNAME)

    # Get and enters the password address
    password = driver.find_element_by_id('pass')
    password.send_keys(PASSWORD)

    # Gets and clicks the login button
    submit = driver.find_element_by_id('loginbutton')
    submit.click()


# The for loop loops through the users and marks the conversation as done based on a certain message
def get_last_message():
    # Gets the 'mark as done' button on facebook business to be able to move a converation to another folder
    messages = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '._3oh-._58nk'))
    )

    message = driver.find_elements_by_css_selector('._3oh-._58nk')
    return message[len(message) - 1].text


def get_names_of_completed_conversations():
    names = []

    # Waits until all the list of unread messages loads
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, '_5m17'))
    )

    # Gets the users in a list
    users_list = driver.find_elements_by_class_name("_5m17")

    for x in range(0, len(users_list)):
        if users_list[x].is_displayed():
            users_list[x].click()

            last_message = get_last_message()

            if last_message == MESSAGE:
                names.append(driver.find_element_by_class_name('_iyo').text)
    return names


def click_on_messenger_section():
    # Navigates to the messenger button
    messenger_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[1]/div/div[1]/div[1]/a'))
    )
    messenger_button.click()


def main():
    login()

    click_on_messenger_section()

    list_of_names = get_names_of_completed_conversations()

    for name in list_of_names:
        user = driver.find_element_by_xpath("//span[contains(text(),'" + name + "')]")
        user.click()
        print('Name marked as done: ' + name)
        try:
            mark_message_as_done()
        except exceptions.StaleElementReferenceException:
            mark_message_as_done()
    print('Successfully completed!')
    driver.quit()


if __name__ == "__main__":
    main()
