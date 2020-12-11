import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("test-type")
chromeOptions.add_argument("enable-strict-powerful-feature-restrictions")
chromeOptions.add_argument("enable-geolocation")
cap = chromeOptions.to_capabilities()


class twitterscrap():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe', options=chromeOptions, desired_capabilities=cap)
        self.username = 'z'
        self.pwd = 'gooChris1'
    def get(self):
        self.driver.get('https://twitter.com/login')
    def login(self):
        driver = self.driver
        username = self.username
        pwd = self.pwd
        emailInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')))
        pwdInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')))
        emailInput.send_keys(username)
        pwdInput.send_keys(pwd)
        submitLogin = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')))
        submitLogin.click()
    def explore(self):
        driver = self.driver
        listoftrends = []
        self.driver.get('https://twitter.com/i/trends')

        for x in range(2,22):
            print("Getting trend no.: " + str(x))
            # driver.implicitly_wait(20)
            # trendingtile = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div['+str(x)+']/div/div/div')
            trendingtile = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div['+str(x)+']/div/div/div')))
            listoftrends.append(trendingtile.text)
            print("Get no.: "+str(x))
        for trend in listoftrends:
            print(trend)
            print('\n')
        with open('trendinglist.txt', "w", encoding="utf-8") as f:
            for trend in listoftrends:
                f.write(trend + '\n')
        driver.close()


scrap = twitterscrap()
scrap.get()
scrap.login()
scrap.explore()
