from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


#WEBSITE-URL
driver.get("http://orteil.dashnet.org/experiments/cookie/")
#COOKIE
cookie = driver.find_element(by="id", value="cookie")
#5-MINUTES-COUNTDOWN
five_min = time.time() + 60*5
#5-SECONDS-COUNTDOWN
timeout = time.time() + 2.5


#--------------------------BOT-ALGORITHMS-----------------------------
while True:
    cookie.click()
    if time.time() > timeout:

        #BALANCE
        cookie_balance = driver.find_element(by="id", value="money").text.replace(",", "")
        # print(cookie_balance)
        #RIGHT-HAND-PANEL
        store = driver.find_elements(by="css selector", value="#store b")
        item = []
        for each in store:
            each_item = each.text
            item.append(each_item)
        item.pop(-1)

        items_price = [int(item[index].split("-")[1].strip().replace(",", "")) for index in range(len(item))]
        # print(items_price)

        #ITEMS-NAMES-#ID
        item_ids = []
        for id in store:
            item_id = id.text.split("-")[0].strip()
            item_ids.append(item_id)
        # print(item_ids)

        #PURCHASE-ITEMS
        if int(cookie_balance) > items_price[7]:
            element = driver.find_element(by="id", value=f"buy{item_ids[7]}")
            element.click()
        elif int(cookie_balance) > items_price[6]:
            element = driver.find_element(by="id", value=f"buy{item_ids[6]}")
            element.click()
        elif int(cookie_balance) > items_price[5]:
            element = driver.find_element(by="id", value=f"buy{item_ids[5]}")
            element.click()
        elif int(cookie_balance) > items_price[4]:
            element = driver.find_element(by="id", value=f"buy{item_ids[4]}")
            element.click()
        elif int(cookie_balance) > items_price[3]:
            element = driver.find_element(by="id", value=f"buy{item_ids[3]}")
            element.click()
        elif int(cookie_balance) > items_price[2]:
            element = driver.find_element(by="id", value=f"buy{item_ids[2]}")
            element.click()
        elif int(cookie_balance) > items_price[1]:
            element = driver.find_element(by="id", value=f"buy{item_ids[1]}")
            element.click()
        elif int(cookie_balance) > items_price[0]:
            element = driver.find_element(by="id", value=f"buy{item_ids[0]}")
            element.click()

        timeout = time.time() + 2.5

    if time.time() > five_min:
        cps = driver.find_element(by="id", value="cps")
        print(cps.text)
        break  #WHEN COUNTDOWN ENDS IT WILL STOP WHILE LOOP.












