import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chromeOptions = Options()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("test-type")
chromeOptions.add_argument("enable-strict-powerful-feature-restrictions")
chromeOptions.add_argument("enable-geolocation")
cap = chromeOptions.to_capabilities()


class instaBot():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe', options=chromeOptions, desired_capabilities=cap)
        self.username = ''
        self.pwd = ''
    def get(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    def login(self):
        driver = self.driver
        username = self.username
        pwd = self.pwd
        emailInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input')))
        pwdInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input')))
        emailInput.send_keys(username)
        pwdInput.send_keys(pwd)
        submitLogin = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]')))
        submitLogin.click()
        # notifications = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[3]/button[2]')))
        notifications = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
        notifications.click()
    def explore(self):
        driver = self.driver
        username = self.username
        pwd = self.pwd
        # explore = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "react-root"] / section / nav / div[2] / div / div / div[3] / div / div[1] / a')))
        explore = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')))
        explore.click()
        photo = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div[1]/div[2]')))
        photo.click()
        while True:
            time.sleep(random.randint(1,5))
            follow = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')))
            if follow.text == 'Obserwuj':
                if random.randint(1, 100) > 44:
                    print('Followed')
                    follow.click()
            time.sleep(random.randint(1, 10))
            if random.randint(1, 100) > 64:
                like = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]')))
                print('Liked')
                like.click()
            time.sleep(random.randint(1, 7))
            try:
                next = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'coreSpriteRightPaginationArrow')))
                print('Next')
                next.click()
            except Exception:
                close = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/button')))
                close.click()
                print('Closed')
                explore.click()
                print('Explore clicked')



bot = instaBot()
bot.get()
bot.login()
bot.explore()
# driver = webdriver.Chrome('chromedriver.exe', options=chromeOptions, desired_capabilities=cap)
# driver.get('https://tinder.com')

# beginClose = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/button')))
# # beginClose.click()
# loginButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')))
# # loginButton.click()
# loginViaFB = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')))
# # loginViaFB.click()
# try:
#     loginViaFB.click()
# except Exception:
#     try:
#         beginClose.click()
#         loginButton.click()
#         loginViaFB.click()
#     except Exception:
#         pass
# baseWindow = driver.window_handles[0]
# fbPopup = driver.switch_to.window(driver.window_handles[1])
#
# emailInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
# pwdInput = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
# submitLogin = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0"]')))
# emailInput.send_keys('tekoszi@hotmail.com')
# pwdInput.send_keys('japierdole123')
# submitLogin.click()
# driver.switch_to.window(driver.window_handles[0])
# location = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
#
# location.click()
# notiffications = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')))
# notiffications.click()
# likeButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')))
# dislikeButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')))
# x=1
# while True:
#     try:
#         likeButton.click()
#         time.sleep(0.3)
#         print('Like no. ' + str(x))
#         x+=1
#     except Exception:
#         try:
#             startScreen = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/button[2]')))
#             startScreen.click()
#         except Exception:
#             pass
#
# driver.close()