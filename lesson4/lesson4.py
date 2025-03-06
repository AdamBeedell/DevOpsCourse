#lesson4


#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome(service=Service("/Users/danielgotlieb/Downloads/chromedriver"))


# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")
driver.


import requests

results = requests.get("https://api.github.com/users/AdamBeedell/repos")

results = results.json()

results[0]

for result in results:
    print(result['name'])
    print(result['owner']['login'])

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.find_element(By.NAME, "q").send_keys("""hello world""")

driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)