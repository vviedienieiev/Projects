from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r'C:\Program Files\Selenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Samsung-Factory-Unlocked-Smartphone-Pro-Grade/dp/B08FYV84JT")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.close() # close tab
driver.quit()  # close browser

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.com/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
article_count.click()
driver.quit()  # close browser


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.com/wiki/Main_Page")
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
driver.quit()  # close browser


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("V")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("V")
email = driver.find_element_by_name("email")
email.send_keys("V@v.com")
btn = driver.find_element_by_css_selector(".btn-block")
btn.click()

#######################################Cookies game

driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break