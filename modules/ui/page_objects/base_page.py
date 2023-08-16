from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"C:\Users\Кузьма\QA_auto_2023" + "chromedriver.exe"
    DRIVER_NAME = "chromedriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
