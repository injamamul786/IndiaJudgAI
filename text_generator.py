from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service('C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Change this path to where you saved chromedriver
driver = webdriver.Chrome(service=service)
time.sleep(2)  # Wait for 2 seconds to avoid overwhelming the server
# Scrape URLs from Indian Kanoon



# import json
url_list = []
with open('links.txt', 'r', encoding='utf-8') as file:
    # Read all non-empty lines, strip newline and whitespace
    url_list = [line.strip() for line in file if line.strip()]


# print((len(url_list)))
# print("ksdjfskjdfjgv**********bfghgfyg**     ", url_list[2])
# Create a directory to save the text files if it doesn't exist
import os

i=1
for url in url_list:  # Start from the third URL
     # Wait for 2 seconds to avoid overwhelming the server
    driver.get(url)
    time.sleep(2)  # Wait for the page to load  # Wait for the page to load
    divs = driver.find_elements(By.CLASS_NAME, "judgments")
    full_text = ""
    for div in divs:
        text = div.text.strip()
        if text:
            full_text += text + "\n"


    # Optional: Filter out blank lines
    lines = [line.strip() for line in full_text.split("\n") if line.strip()]

    time.sleep(1)  # Wait for the page to load completely
     # Wait for 2 seconds to avoid overwhelming the server
    with open(f"link_to_text/{i}.txt", "w", encoding="utf-8") as file:
        for line in lines[1:]:
            file.write(line + "\n")
    break
driver.quit()