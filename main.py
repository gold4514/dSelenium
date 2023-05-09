import selenium_metamask_automation
from certifi.__main__ import args
from selenium import webdriver
import requests
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def run():
    extension_id = "cfkgdnlcieooajdnoehjhgbmpbiacopjflbjpnkm"  # chrome-extension:///home.html nkbihfbeogaeaoehlefnkodbefgpgknn
    metamask_password = "asd"
    profile_id = 'dsa'  # 'dsa'
    req_url = 'http://localhost:3001/v1.0/browser_profiles/' + profile_id + '/start?automation=1'

    response = requests.get(req_url)
    response_json = response.json()
    print(response_json)

    port = str(response_json['automation']['port'])
    print(port)

    web_driver = Service(r'C:\Users\leo\Downloads\chromedriver108\chromedriver-windows-x64.exe')
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:' + port

    driver = webdriver.Chrome(service=web_driver, chrome_options=options)

    driver.get(f"chrome-extension://{extension_id}/popup.html")
    time.sleep(1)
    time.sleep(1)

    passT = driver.find_element(By.XPATH, "//*[@id='password']")
    passT.send_keys(metamask_password)
    time.sleep(1)
    clickT = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/button")
    clickT.click()

    driver.get("https://scroll.io/alpha")
    time.sleep(3)

    selenium_metamask_automation.connectToWebsite()

run()