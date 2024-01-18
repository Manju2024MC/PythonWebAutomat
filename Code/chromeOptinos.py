import time

from selenium import webdriver
import logging

def test_open_chrome():

    Chrome_options = webdriver.ChromeOptions()
    # for applion we have to downalod the crx file then crx file have to provide
    # in the crx file path
    # Chrome_options.add_extension("CRX_File_Path")
    LOGGER = logging.getLogger(__name__)
    broser = webdriver.Chrome(options=Chrome_options)
    broser.get("https://www.youtube.com/")
    broser.maximize_window()
    print(broser.title)
    LOGGER.info("This is the information log")
    print("I am successfully ran the job")
    # time.sleep(2000)
    # broser.close()  #close session window and webdriver session will open
    # broser.close() #Close all the windows and webdriver session wii close
    broser.back()
    broser.get("https://www.google.com")
    broser.refresh()
    broser.forward()
    time.sleep(1000)
