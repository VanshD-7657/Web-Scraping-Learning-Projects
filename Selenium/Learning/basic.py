from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.com/s?k={query}&crid=1EHMA3MJU714F&sprefix=lap%2Caps%2C405&ref=nb_sb_ss_p13n-expert-pd-ops-ranker_1_3")
print(driver.get_attribute("outerHTML"))
driver.close()