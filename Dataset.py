#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Opens up web driver and goes to Google Images
driver = webdriver.Chrome("C:/Users/Lenovo/Downloads/chromedriver.exe")
driver.get("https://www.google.com/")

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("apple fruit")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[5]/input").click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for p in range(1, 105):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(p)+']/a[1]/div[1]/img').screenshot("F:/Github/Color-Histogram-by-Python/Dataset/Apple/apple("+str(p)+").png")
    except:
        pass

#ภาพที่ 25 หาร 25 ลงตัว จะไม่สามารถรันได้