from selenium import webdriver

def test_open_chrome():
    broser = webdriver.Chrome()
    broser.get("https://www.youtube.com/")
    broser.maximize_window()
    print(broser.title)