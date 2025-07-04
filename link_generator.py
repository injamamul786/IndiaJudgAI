from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service = Service('C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Change this path to where you saved chromedriver
driver = webdriver.Chrome(service=service)

for i in range(0, 40):
    time.sleep(2)  # Wait for 2 seconds to avoid overwhelming the server
    driver.get(f"https://indiankanoon.org/search/?formInput=criminal%20%20%20%20%20%20%20%20%20%20%20%20doctypes%3A%20allahabad%20authorid%3A%20s-ahmed%20year%3A%202022&pagenum={i}")   
    a_tags = driver.find_elements("css selector", ".result_title a")  # Get the first result
    # htmlpage.click()  # Click on the first result
    with open("links.txt", "a", encoding="utf-8") as file:
        for tag in a_tags:
            href = tag.get_attribute("href")
            if href:
                file.write(href + "\n")
    time.sleep(2)  # Wait for 2 seconds to avoid overwhelming the server
# print([element.get_attribute('href') for element in htmlpage])  # Print the title of the page
time.sleep(5)  # Wait for 5 seconds to see the page
driver.quit()
