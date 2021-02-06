from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

FACEBOOK_EMAIL = 'FB_EMAIL'
FACEBOOK_PASSWORD = 'FB_PASSWORD'
chrome_driver_path = r'C:\Program Files\Selenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(1)
login_button = driver.find_element_by_css_selector("#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.H\(100\%\).D\(f\).Ai\(c\) > div.H\(40px\).Px\(28px\) > button")
login_button.click()
time.sleep(1)
try:
    login_with_facebook_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_facebook_btn.click()
    time.sleep(1)
except:
    more_options = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    time.sleep(1)
    login_with_facebook_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_facebook_btn.click()
    time.sleep(1)
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)
facebook_email_form = driver.find_element_by_xpath('//*[@id="email"]')
facebook_email_form.send_keys(FACEBOOK_EMAIL)
facebook_password_form = driver.find_element_by_xpath('//*[@id="pass"]')
facebook_password_form.send_keys(FACEBOOK_PASSWORD)
facebook_password_form.send_keys(Keys.ENTER)
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
time.sleep(1)
try:
    facebook_continue_as_user = driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[2]/div[1]/button')
    facebook_continue_as_user.click()
    tinder_allow_geo = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    tinder_allow_geo.click()
except:
    tinder_allow_geo = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    tinder_allow_geo.click()

try:
    tinder_not_interested = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    tinder_not_interested.click()
except:
    pass

try:
    tinder_accept_cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    tinder_accept_cookies.click()
except:
    pass
time.sleep(5)
for i in range(100):
    tinder_nope_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    tinder_nope_button.click()
    time.sleep(3)
driver.quit()