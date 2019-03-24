import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------  USER INPUT  ------------------ #

email_id = ''
password = ''

page_link = ''
number_of_times =
frequency =
message = ""

# -----------------  INITIALIZE CHROMEDRIVER  ---------------------- #

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"                     # Enable explicit wait.
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')             # Start Chrome maximized.
options.add_argument('--disable-notifications')
url = 'https://www.facebook.com'
driver = webdriver.Chrome('E:\Python\chromedriver.exe', desired_capabilities=capa, chrome_options=options)  # Arguments
driver.get(url)

# ----------------  LOG IN AND SPAM  ----------------- #

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID, "email")))
driver.find_element_by_id('email').send_keys(email_id)                                   # Enter Email ID
driver.find_element_by_id('pass').send_keys(password)                                    # Enter password
driver.find_element_by_xpath("//input[@value='Log In']").click()                         # Login

WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
driver.get(page_link)                                                                    # Go to page or profile
time.sleep(10)

''' Keep scrolling down until the number of spammable posts >= number_of_times'''
comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")
while len(comment_boxes) < number_of_times:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        pass
    comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")               # Go to top of page.
original = len(driver.find_elements_by_xpath("//div[text()='Write a comment...']"))    # Keep track of number of posts.
pyperclip.copy(message)                                                                # Copy the message to clipboard.

actions = ActionChains(driver)                                                             # Initialize ActionChains
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER)   # Ctrl+V

for i in range(0, number_of_times):
    for j in range(0, frequency):
        comment_boxes = driver.find_elements_by_xpath("//div[text()='Write a comment...']")   # Find the comment boxes.
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", comment_boxes[i])  # Scroll to view.
        time.sleep(1)
        driver.execute_script("arguments[0].click();", comment_boxes[i])                        # Click on comment box.
        time.sleep(1)
        actions.perform()                                                                       # Perform Ctrl+V
        ''' Perform next comment only when previous comment is performed.'''
        while len(driver.find_elements_by_xpath("//div[text()='Write a comment...']")) != original:
            time.sleep(0.5)
    print(str(i+1), "/", str(number_of_times), "posts spammed.")