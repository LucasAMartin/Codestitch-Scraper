import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape():
    # Set the URL you want to scrape from
    url = 'https://codestitch.app/app/dashboard/stitches/1058'

    # Set your login credentials
    username = 'lucasmartiniscool@gmail.com'
    password = 'Seahawksarelit5'

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Connect to the website and fetch the page
    driver.get(url)

    driver.implicitly_wait(2)
    # Find the username and password fields
    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    # Enter your login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.submit()

    # Wait for the page to load
    driver.implicitly_wait(2)

    driver.get(url)

    # Get the page source
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first two elements with the 'tab' class
    tabs = driver.find_elements(By.CLASS_NAME, 'tab')[:2]

    # Add the 'active-tab' class to them
    for tab in tabs:
        driver.execute_script("arguments[0].classList.add('active-tab')", tab)

    # Get the content from the 'CodeMirror-code' class
    code_elements = driver.find_element(By.CLASS_NAME, 'CodeMirror-code')
    data = code_elements.text

    # Do something with the data
    print(data)

    # Close the driver
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
