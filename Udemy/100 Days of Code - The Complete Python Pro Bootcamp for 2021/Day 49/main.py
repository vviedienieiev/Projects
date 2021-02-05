from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
chrome_driver_path = r'C:\Program Files\Selenium\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

counter = 1
job_search_url = f'https://www.linkedin.com/jobs/search/?geoId=103173899&keywords=data%20analyst&location=Kyiv%20City%2C%20Ukraine&start={counter}'

driver.get(job_search_url)
time.sleep(3)
sign_in_btn_1 = driver.find_element_by_css_selector(".nav__button-secondary")
sign_in_btn_1.click()
time.sleep(3)
username = driver.find_element_by_css_selector("#username")
username.send_keys(EMAIL)
password = driver.find_element_by_css_selector("#password")
password.send_keys(PASSWORD)
sign_in_btn_2 = driver.find_element_by_css_selector(".from__button--floating")
sign_in_btn_2.click()
time.sleep(3)

list_of_companies = []

while True:
    job_search_url = f'https://www.linkedin.com/jobs/search/?geoId=103173899&keywords=data%20analyst&location=Kyiv%20City%2C%20Ukraine&start={counter}'
    driver.get(job_search_url)
    time.sleep(3)
    job_search_result_panel = driver.find_element_by_css_selector(".jobs-search__left-rail")
    job_search_result_panel.click()
    body = driver.find_element_by_css_selector("body")
    body.send_keys(Keys.END)
    time.sleep(3)

    companies = driver.find_elements_by_css_selector(".job-card-container__company-name")
    jobs = driver.find_elements_by_css_selector(".job-card-list__title")
    if len(jobs) == 0:
        break
    else:
        list_of_companies.extend([company.get_attribute("href") for company in companies])
        counter += 25
list_of_companies = list(set(list_of_companies))
for company in list_of_companies[0:1]:
    driver.get(company)
    follow_button = driver.find_element_by_css_selector('#ember55')
    follow_button.click()

driver.quit()