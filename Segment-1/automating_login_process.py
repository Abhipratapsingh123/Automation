from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by = "id",value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
  print(driver.current_url)



print(main())
