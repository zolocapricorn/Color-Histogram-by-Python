#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Opens up web driver and goes to Google Images
driver = webdriver.Firefox()
driver.get("https://www.google.com/search?q=orange&client=firefox-b-d&sxsrf=ALeKk02rFLZJDczUwawr91XzwZKUChRX3Q:1623329826893&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjclb3tjo3xAhXJzjgGHS26BJgQ_AUoAXoECAEQAw&biw=1536&bih=711")
