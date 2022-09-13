from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


s = Service(ChromeDriverManager().install())
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',
   options = webdriver.ChromeOptions())
driver.get("https://mojopro-fnacmgmt418.staging.joveo.com/adecco-staging/clients")
assert driver.title == "Joveo Account"


s = Service(GeckoDriverManager().install())
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',
   options = webdriver.FirefoxOptions())
driver.get("https://mojopro-fnacmgmt418.staging.joveo.com/adecco-staging/clients")
assert driver.title == "Joveo Account"