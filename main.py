from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def login(url, username, password):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Connect to the website and fetch the page
    driver.get(url)

    # Find the username and password fields
    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    # Enter your login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.submit()

    return driver


def scrape(driver, url, directory):
    # Check if the buttons directory exists
    if not os.path.exists(directory):
        # If not, create the buttons directory
        os.makedirs(directory)

    driver.get(url)

    # Find all buttons with the ID get-code
    buttons = driver.find_elements(By.ID, 'get-code')

    # Find all titles and save them in a list
    titles = driver.find_elements(By.XPATH, '//*[@id="stitch-library"]/div/div/h3')
    filenames = [title.text for title in titles]

    for i, button in enumerate(buttons):
        try:
            # Get the corresponding filename from the list
            filename = filenames[i]

            # Click on the button
            button.click()

            # Switch to the new window that opens
            driver.switch_to.window(driver.window_handles[1])

            # Find the first two elements with the 'tab' class
            tabs = driver.find_elements(By.XPATH,
                                        '//*[@id="CODE_TABS"]/div[2]/div[contains(@class, "tab")]')

            # Find the textarea elements within the first two tabs
            text_areas = [tab.find_element(By.TAG_NAME, 'textarea') for tab in tabs]

            # Get the text data from all text areas
            data = [text_area.get_attribute('value') for text_area in text_areas]

            # Check if a file with the same name already exists in the buttons directory
            i = 1
            new_filename = filename
            while os.path.exists(os.path.join(directory, new_filename + '.txt')):
                new_filename = filename + f' ({i})'
                i += 1

            # Open a new file in write mode
            with open(os.path.join(directory, new_filename + '.txt'), 'w', encoding='utf-8') as f:
                # Write the data to the file
                f.write('\n'.join(data))

        except Exception as e:
            print(f'An error occurred while saving the file: {e}')

        # Close the new window
        driver.close()

        # Switch back to the original window
        driver.switch_to.window(driver.window_handles[0])


if __name__ == '__main__':
    url = 'https://codestitch.app/app/dashboard/catalog/sections/1'
    username = 'lucasmartiniscool@gmail.com'
    # Password was changed before repository was made public
    password = 'Seahawksarelit5'

    driver = login(url, username, password)

    # Add all the URLs to scrape. Could be made more efficient which I can work on.
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/22', 'Buttons')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/1', 'Navigation')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/2', 'Hero')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/2?page=2', 'Hero')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/3', 'Services')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/3?page=2', 'Services')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/3?page=3', 'Services')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/3?page=4', 'Services')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=2', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=3', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=4', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=5', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=6', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/4?page=7', 'Side by Side')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/78', 'Content Flair')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/5', 'Gallery')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/43', 'Meet Our Team')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/43?page=2', 'Meet Our Team')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/52', 'Steps')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/13', 'Stats')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/49', 'Pricing')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/50', 'FAQ')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/19', 'Why Choose Us')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/62', 'Quotes')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/56', 'Misc')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/20', 'Reviews')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/20?page=2', 'Reviews')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/94', 'Events')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/44', 'Forms and Contact')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/44?page=2', 'Forms and Contact')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/79', 'Blog')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/7', 'Call to Action')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/21', 'Footer')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/21?page=2', 'Footer')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/55', 'Interior Pages')
    scrape(driver, 'https://codestitch.app/app/dashboard/catalog/sections/23', 'Dark Mode')
    driver.close()























