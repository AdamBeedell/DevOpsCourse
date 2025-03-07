#assignment4


# 1
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.walla.co.il") ## going to the https but ack it was http
time.sleep(4)
driver2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver2.get("https://www.ynet.co.il") ## going to the https but ack it was http



#2


fftitle = driver2.title

driver2.refresh()
print(driver2.title)
print((driver2.title == fftitle)) 


#3

#Looks the same but i could be wrong. My guess would be the html is server side and so names should be the same, though a browser could render it differently?


#4

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://translate.google.com/?sl=auto&tl=en&op=translate") ## 
time.sleep(3)
accept_all_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/form[1]/div/div/button/span[6]')
accept_all_button.click()

translate_window = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea')
translate_window.send_keys(fftitle)
translate_window.send_keys(Keys.RETURN)

driver.find_element(By.NAME, "q").send_keys("""hello world""")

driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)



#5

#driver.close()
driver.get("https://youtube.com") ## 
accept_all_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
accept_all_button.click()

searchbox = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
searchbox.click() #### only works at a larger size
searchbox.send_keys('never gonna give you up')
searchbox.send_keys(Keys.ENTER)
rickastley = driver.find_element(By.XPATH, '//*[contains(@aria-label, "Rick Astley - Never Gonna Give You Up (Official Music Video)")]')
rickastley.click()


#6

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://translate.google.com/?sl=auto&tl=en&op=translate") ## 
time.sleep(3)
accept_all_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span[6]')
accept_all_button.click()
translate_window = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea')
translate_window.send_keys("test")
translate_window = driver.find_element(By.CLASS_NAME, 'er8xn')
translate_window.send_keys("test2")
translate_window = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Source text"]') # by JSname should also be possible element = driver.find_element(By.CSS_SELECTOR, '[jsname="BJE2fc"]')
translate_window.send_keys("test3")

print(translate_window)


#7

driver.get("https://facebook.com") ## 
allow_cookies_button = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span')
allow_cookies_button.click()
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys(email)
password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys(password)
log_in_button = driver.find_element(By.XPATH, '//*[@id="u_0_5_IB"]')
log_in_button.click()
log_in_button.click()



