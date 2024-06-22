from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

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
  driver.get("https://member.insight.rakuten.co.in/sign-in")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by="id",value="userName").send_keys("Enter_credentials")
  time.sleep(2)
  driver.find_element(by="id",value="password").send_keys("Enter_credentials"+Keys.RETURN)
  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/div[1]/div/div/header/div/header/div/div/div/div/div[2]/span/div/strong")

  text = element.text
  print(driver.current_url)
  driver.quit()
  return text


print(main())