from selenium import webdriver
import time
import urllib3


capabilities = {
    "build" : "Liz First Test",
    "name" : "Python-Amazon-Iphone-Search",
    "platform" : "Windows 10",
    "browserName" : "Chrome",
    "version" : "77",
    # "selenium_version" : "3.13.0",
    "console" : True,
    "network" : True,
    "visual" : True,
    "geoLocation" : "US",
    "ie.driver" : "2.53.1",
    "ie.compatibility" : 11001
}

driver = webdriver.Remote(
    command_executor='http://elizabethb:zvSUfxvJ5T3eegn5rwXQWCPCXDrCUkQYfyYw9MYLbk6T1PaauA@hub.lambdatest.com/wd/hub',
    desired_capabilities=capabilities)

# desired_cap['lambdatest.local'] = True
# desired_cap['lambdatest.localIdentifier'] = '1.2'

driver.get("https://www.amazon.com")
time.sleep(3)

Search = driver.find_element_by_id("twotabsearchtextbox")
Search.send_keys("i","P","h","o","n","e","X" )
Search.submit()
time.sleep = 2

driver.find_element_by_id("a-autoid-0").click()
time.sleep = 2

driver.find_element_by_id("s-result-sort-select_2").click()

products = driver.find_elements_by_css_selector("#search > div.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-result-list.s-search-results.sg-row > div")

for product in products:
    title = product.find_element_by_css_selector("a.a-link-normal.a-text-normal")
    print(title.text)
    price = driver.find_element_by_css_selector(".a-price.a-text-price")
    print(price.text)
    print(title.get_attribute('href'))

driver.quit()