import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Set up the Selenium webdriver
driver = webdriver.Chrome()
url = 'https://learn.microsoft.com/en-us/lifecycle/products/'
driver.get(url)

# Create a CSV file to store the data
csv_file = open('product_lifecycle2.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Start Date', 'End Date'])

# Scrape the data from all pages
while True:
    # Find the product rows
    
    product_rows = driver.find_element(By.CLASS_NAME, "card-content")
    #find_element("xpath", '//*[@id="content-browser-container"]/div/div/div[2]/ul/li[1]')

    # Scrape the data for each product
    for row in product_rows:
        # Extract the title
      
        
        title_element = row.find_element(By.CLASS_NAME, "card-content-title")
        #row.find_element("xpath", '//*[@id="ax-59"]')
        title = title_element.text

        # Extract the start date
        start_date_element = row.find_element("xpath", '//*[@id="content-browser-container"]/div/div/div[2]/ul/li[1]/article/div[1]/ul/li[1]')
        start_date = start_date_element.text

        # Extract the end date if available, otherwise use "NaN"
        try:
            end_date_element = row.find_element("xpath", '//*[@id="content-browser-container"]/div/div/div[2]/ul/li[1]/article/div[1]/ul/li[2]')
            end_date = end_date_element.text
        except NoSuchElementException:
            end_date = "NaN"

        # Write the data to the CSV file
        csv_writer.writerow([title, start_date, end_date])

    # Check if there is a next page button
    next_page_button = driver.find_element_by_xpath('//*[@id="content-browser-container"]/div/div/div[2]/div[4]/div[1]/div/nav/ul/li[4]/button')
    if 'disabled' in next_page_button.get_attribute('class'):
        # No next page button found, break the loop
        break

    # Click the next page button
    next_page_button.click()

# Close the CSV file
csv_file.close()

# Close the browser
driver.quit()
