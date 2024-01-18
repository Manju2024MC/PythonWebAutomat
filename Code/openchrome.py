from selenium import webdriver
import logging

def test_open_chrome():
    broser = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
    broser.get("https://www.youtube.com/")
    broser.maximize_window()
    print(broser.title)
    LOGGER.info("This is the information log")
    print("I am successfully ran the job")