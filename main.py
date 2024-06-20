# Selenium is used to automate browser actions

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable_infobars")
  options.add_argument("start-maximised")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features = AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.python.pythonanywhere.com")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(By.XPATH, "/html/body/div[1]/p[2]")
  text = element.text
  driver.quit()  # Make sure to close the browser after finishing
  return text


print(main())
