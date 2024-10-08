# import json
import os
# from PIL import Image
# import re
# import glob

import platform
# from dotenv import load_dotenv
# load_dotenv(r"D:\PProjects\NN\tavily\.env")
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import configparser
# config = configparser.ConfigParser()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
# import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('log_file.log')

# Create a console handler
console_handler = logging.StreamHandler()

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log a message

# import time as t
# import subprocess
# from PIL import Image
# import cv2
# import numpy as np
# import pyperclip
# from clicker import run_script, get_keyboard_controller,write_string
# import os
# import base64
# import sys
# sys.path.append(r"D:\PProjects\libs")
# from file_readers.tools import sanitize_filename
# config.read(r"D:\PProjects\libs\parsing\config.ini")
# from tenacity import retry, stop_after_attempt, wait_fixed



def get_platform_paths():
    """
    Возвращает пути к ChromeDriver и Chrome в зависимости от платформы.
    """

    system = platform.system()
    if system == "Windows":
        service_path = r"D:\PProjects\Parsing\chromedriver-win64\chromedriver.exe"
        browser_path = r"D:\chr\chrome.exe"
    elif system == "Linux":
        service_path = r"./chromedriver-linux64/chromedriver"
        browser_path = r"./chrome-linux64/chrome"
    else:
        raise OSError(f"Unsupported operating system: {system}")

    return service_path, browser_path

    # Пример использования:

service_path, browser_path = get_platform_paths()


service = Service(executable_path=service_path,service_args=["--verbose", "--log-path=cd.log"])
chrome_options = webdriver.ChromeOptions()

# userdatadir=r"C:\Users\Sergey\AppData\Local\Google\Chrome for Testing\User Data"
# userdatadir = r"C:\Users\Sergey\AppData\Local\Google\Chrome\User Data\Profile 1"

# chrome_options.add_argument(rf"--user-data-dir={userdatadir}") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# chrome_options.add_argument(r'--profile-directory=Profile 2')
# chrome_options.add_argument("--incognito")
# if headless:
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("disable-infobars")
# chrome_options.add_argument("start-maximized")
# chrome_options.binary_location = browser_path
# chrome_options.add_argument("--verbose")
# chrome_options.add_argument("--log-path=cd.log")
# logging.basicConfig(level=logging.DEBUG)

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
# def get_driver():
#     return uc.Chrome(service=service, options=chrome_options,browser_executable_path=browser_path)
import logging
import json

def log_webdriver_state(driver, logger):
    """
    Логирует текущее состояние WebDriver в файл.

    :param driver: Объект WebDriver.
    :param filename: Имя файла для логирования.
    """

    # logging.basicConfig(filename=filename, level=logging.INFO)

    try:
        # Получаем текущий URL
        current_url = driver.current_url
    except Exception as e:
        current_url = f"Ошибка получения URL: {str(e)}"

    try:
        # Получаем исходный код страницы
        page_source = driver.page_source
    except Exception as e:
        page_source = f"Ошибка получения исходного кода: {str(e)}"

    try:
        # Получаем заголовок страницы
        page_title = driver.title
    except Exception as e:
        page_title = f"Ошибка получения заголовка: {str(e)}"

    try:
        # Получаем capabilities
        capabilities = driver.capabilities
    except Exception as e:
        capabilities = f"Ошибка получения capabilities: {str(e)}"

    # Логируем информацию
    logger.info("=== Начало лога состояния WebDriver ===")
    logger.info(f"Текущий URL: {current_url}")
    logger.info(f"Заголовок страницы: {page_title}")
    logger.info(f"Capabilities: {json.dumps(capabilities, indent=4)}")
    # logging.info(f"Исходный код страницы: {page_source}")  # Раскомментируйте, если нужен исходный код
    logger.info("=== Конец лога состояния WebDriver ===")

def log_webdriver_caps(caps, filename=r"D:\PProjects\Ubuntu_selenium\caps_logs.txt"):
    logging.basicConfig(filename=filename, level=logging.INFO)
    
    capabilities = caps

    # Логируем информацию
    logging.info("=== Начало лога состояния WebDriver ===")
    logging.info(f"Capabilities: {json.dumps(capabilities, indent=4)}")
    # logging.info(f"Исходный код страницы: {page_source}")  # Раскомментируйте, если нужен исходный код
    logging.info("=== Конец лога состояния WebDriver ===")

driver = None
print("Selenium started")
try:
    # log_webdriver_state(driver)
    driver = uc.Chrome(service=service, options=chrome_options,browser_executable_path=browser_path)
    log_webdriver_state(driver, logger)
    # driver = uc.Chrome(service=service, options=chrome_options)
except Exception as e:
    logger.info(e)
    raise e

# try:                              
#     driver = uc.Chrome(service=service, options=chrome_options,browser_executable_path=browser_path)
# except Exception as e:          
#     logger.info(e)                    

# try:
#     driver = uc.Chrome(service=service, options=chrome_options,browser_executable_path=browser_path)
# except Exception as e:
#     logger.info(e)

# driver = uc.Chrome(service=service, options=chrome_options,browser_executable_path=browser_path)
# driver = get_driver()
# driver = uc.Chrome()
# driver.quit()
print("Chrome started")
wait = WebDriverWait(driver, 10)
print("Wait started")
actions = ActionChains(driver)
print("Actions started")
# keyboard=get_keyboard_controller()
url=r"https://4pda.to/"
print("URL started")
driver.get(url)
print("Get started")

def make_screenshot(driver,tail=""):
    screenshots_path=r""
    cur_time=datetime.now().strftime("%Y%m%d%H%M%S")
    driver.get_screenshot_as_file(os.path.join(screenshots_path, f"{cur_time}{tail}.png"))
    return cur_time

print("Screenshot started")
make_screenshot(driver,tail="")
print("Screenshot ended")
time.sleep(10)

try:
    driver.quit()
except Exception as e:
    logger.info(e)
# driver.quit()
# page_sourse=driver.page_source

# with open('page_source.html', 'w', encoding='utf-8') as f:
#     f.write(page_sourse)


# from bs4 import BeautifulSoup


# # Parse the HTML
# soup = BeautifulSoup(page_sourse, 'lxml')

# # Find all <source> tags with type="video/mp4"
# source_tags = soup.find_all('source', {'type': 'video/mp4'})

# # Print the source URLs
# for tag in source_tags:
#     print(tag['src'])
