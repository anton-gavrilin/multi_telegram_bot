import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from other_files.constants import vk_group_anekdots

firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(executable_path="other_files/geckodriver.exe", options=firefox_options)

try:
    driver.get(vk_group_anekdots)

    last_height = driver.execute_script("return document.body.scrollHeight")

    print("Start scrapping...")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")

    s = soup.find_all('div', class_='wall_post_text')

    with open("other_files/anekdots.txt", "w", encoding="utf-8") as f:
        for text in s:
            f.write(text.text + "\n")

    print("Successfully scrap.")

    with open("other_files/anekdots.txt", "r") as f:
        lines = f.readlines()
        print(random.choice(lines))

finally:
    driver.quit()