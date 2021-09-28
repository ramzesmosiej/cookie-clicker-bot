import time

from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element_by_id("cookie")


def do_shopping():
    all_prices = driver.find_elements_by_css_selector("#store b")
    item_names = []
    item_prices = []
    # created two lists, one for prices and one for item name, index of one list corresponds to the index of another
    for price in all_prices:
        if price.text != "":
            item_prices.append(int(price.text.split()[-1].replace(",", "")))
            item_names.append(price.text.split()[0])
    buy = []
    # select only this elements from price list which we can afford 
    current_money = int(driver.find_element_by_id("money").text.replace(",", ""))
    for cps in item_prices:
        if current_money >= cps:
            buy.append(cps)
    index_of_item_to_buy = item_prices.index(max(buy))
    element_to_click = driver.find_element_by_id(f"buy{item_names[index_of_item_to_buy]}")
    element_to_click.click()


end_time = time.time() + 300
time_to_buy = time.time() + 10

while time.time() < end_time:
    cookie_button.click()
    if time.time() > time_to_buy:
        do_shopping()
        time_to_buy += 10
result = driver.find_element_by_id("cps")
print(result.text)
