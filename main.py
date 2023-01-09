import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Software/Development/chromedriver.exe"
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USERNAME = "KlausBern1453"
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]").click()
        time.sleep(40)
        down_speed = self.driver.find_element(By.XPATH,
                                              "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        up_speed = self.driver.find_element(By.XPATH,
                                            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up = up_speed.text
        self.down = down_speed.text

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
        sign_in_button.click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        email.send_keys(TWITTER_USERNAME)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)
        tweet_create = self.driver.find_element(By.CSS_SELECTOR, '.DraftEditor-editorContainer div')
        tweet_body = f"Hey Internet Provider why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}/{PROMISED_UP}?"
        tweet_create.send_keys(tweet_body)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
