# The below code works to render the homepage of Frontier
# However, one instance consumes 400MB of RAM
# Instead of rendering the entire browser after every iteration
# (which would quickly get expensive)
# Splash will be used.
# The below code is given for documentation purposes.

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://flyfrontier.com'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

driver = webdriver.Firefox()

driver.get(URL)

from_ = driver.find_element(By.ID, 'promocode')

from_.send_keys('LGA')
