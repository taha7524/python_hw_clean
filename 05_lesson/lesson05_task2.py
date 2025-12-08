from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def click_blue_button():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(2)

    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()
    sleep(2)
    driver.quit()

click_blue_button() 