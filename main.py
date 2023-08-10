from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def scrape(url, directory):
    # Set your login credentials
    username = 'lucasmartiniscool@gmail.com'
    password = 'Seahawksarelit5'

    # Check if the buttons directory exists
    if not os.path.exists(directory):
        # If not, create the buttons directory
        os.makedirs(directory)

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

    # Close the driver
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape('https://codestitch.app/app/dashboard/catalog/sections/1', 'Buttons')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/2', 'Hero')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/2?page=2', 'Hero')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/3', 'Services')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/3?page=2', 'Services')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/3?page=3', 'Services')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/3?page=4', 'Services')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=2', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=3', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=4', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=5', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=6', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/4?page=7', 'Side by Side')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/78', 'Content Flair')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/43', 'Meet Our Team')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/43?page=2', 'Meet Our Team')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/52', 'Steps')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/13', 'Stats')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/49', 'Pricing')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/50', 'FAQ')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/19', 'Why Choose Us')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/62', 'Quotes')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/56', 'Misc')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/20', 'Reviews')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/20?page=2', 'Reviews')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/94', 'Events')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/44', 'Forms and Contact')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/79', 'Blog')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/7', 'Call to Action')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/21', 'Footer')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/55', 'Interior Pages')
    scrape('https://codestitch.app/app/dashboard/catalog/sections/23', 'Dark Mode')






















