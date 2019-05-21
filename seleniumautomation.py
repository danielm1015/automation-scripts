from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# launch browser & website
driver= webdriver.Firefox()
driver.get("http://google.com");

# selecting google search bar
search = driver.find_element_by_name('q');
search.clear();

# entering & submitting text in google search bar
search.send_keys("python wiki front page");
search.send_keys(Keys.RETURN);
time.sleep(4)

# find link by text
link = driver.find_element_by_link_textPython Wiki: FrontPage")
link.click()

# python wiki search bar
searchBox= driver.find_element_by_id('searchinput')
searchBox.clear()

searchBox.send_keys("Beginner")
searchBox.send_keys(Keys.RETURN)
time.sleep(5)

# no unique id, name, or class; will use xpath:
# html/body/div[2]/div[3]/ul/li[5]/form/div/select
select = Select(driver.find_element_by_xpath("///*/form/div/select")
select.select_by_visible_text("Raw Text")

driver.close();
