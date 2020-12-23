# from selenium import webdriver
# url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
# driver = webdriver.Chrome()
# driver.get(url)
# messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# messageField.send_keys("Hello World")
# showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# showMessageButton.click()
# additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
# additionField1.send_keys('10')
# additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
# additionField2.send_keys('12')
# getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
# getTotalButton.click()

# webdriver is basically a broweser that selenium will used to interact with the web
'''
niche me new library install kri che jethi chrome browser khule ane 
pip install webdriver-manager ### aa cmd ma jai ne install krvanu 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome((ChromeDriverManager().install()))
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
driver.execute_script("arguments[0].click();", showMessageButton)
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('11')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
driver.execute_script("arguments[0].click();", getTotalButton)


