import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape():
    # Set the URL you want to scrape from
    url = 'https://codestitch.app/app/dashboard/stitches/758?nav=Top%20Dropdown'

    # Set your login credentials
    username = 'lucasmartiniscool@gmail.com'
    password = 'Seahawksarelit5'

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Connect to the website and fetch the page
    driver.get(url)

    driver.implicitly_wait(.5)
    # Find the username and password fields
    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    # Enter your login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.submit()

    driver.get(url)

    # Get the page source
    html = driver.page_source

    # Find the first two elements with the 'tab' class
    tabs = driver.find_elements(By.XPATH, '//*[@id="CODE_TABS"]/div[2]/div[contains(@class, "tab")][position() < 4]')[:3]

    # Find the textarea elements within the first two tabs
    text_areas = [tab.find_element(By.TAG_NAME, 'textarea') for tab in tabs]

    # Get the text data from the two text areas
    data1 = text_areas[0].get_attribute('value')
    data2 = text_areas[1].get_attribute('value')
    data3 = text_areas[2].get_attribute('value')

    # Get the filename from the h2 element
    filename = driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div[1]/div/h2')
    filename = filename.text

    # Open a new file in write mode
    with open(filename + '.txt', 'w') as f:
        # Write the data to the file
        f.write(data1 + '\n' + data2 + '\n' + data3)

    # Close the driver
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
