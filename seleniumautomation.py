import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dirver_path = r'C:\Users\Daniel.Martinez\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(dirver_path)
driver.get("http://google.com")

# selecting google search bar
google_search = driver.find_element_by_name('q')
google_search.clear()

# entering & submitting text in google search bar
google_search.send_keys("python wiki front page")
google_search.send_keys(Keys.RETURN)
time.sleep(4)

# find link by text
link = driver.find_element_by_link_text("Python Wiki: FrontPage")
link.click()

# python wiki search bar
python_serchbox = driver.find_element_by_id('searchinput')
python_serchbox.clear()

python_serchbox.send_keys("Beginner")
python_serchbox.send_keys(Keys.RETURN)
time.sleep(5)

# no unique id, name, or class; will use xpath:
# html/body/div[2]/div[3]/ul/li[5]/form/div/select
# select = Select(driver.find_element_by_xpath("///*/form/div/select")
# select.select_by_visible_text("Raw Text")

driver.close()
