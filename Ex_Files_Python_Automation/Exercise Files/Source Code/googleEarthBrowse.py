from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.google.com/earth'
driver = webdriver.Chrome((ChromeDriverManager().install()))
driver.get(url)
wait = WebDriverWait(driver, 10) #creat implicit wati function for wait 10  second 
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
driver.execute_script("arguments[0].click();", launchEarthButton)
