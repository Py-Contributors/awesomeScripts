# importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# setup for chromedriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)
driver.get("https://web.whatsapp.com/")
input("Press anything after QR scan")
time.sleep(5)
# code for getting all recent contacts
contact_list = []
for contacts in driver.find_elements_by_class_name('_21xgG'):
    # looping through each contact name
    title = contacts.find_element_by_xpath
    ('div/div/div[2]/div[1]/div[1]/span').text
    contact_list += list(title.split('\n'))
print(contact_list)
# response Dictionaries add this according to you
response = {
  "hii": "hello there we are unavaiable right now leave your message",
  "how are you": "i am fine 😁",
  "bhai paisa de de": "nikallllllllll"}
# reading recent chats of every person on list
for name in contact_list:
    try:
        person = driver.find_element_by_xpath
        ('//span[@title = "{}"]'.format(name))
        person.click()
        time.sleep(3)
    except Exception:
        continue
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    msg_got = driver.find_elements_by_css_selector
    (".GDTQm.message-in.focusable-list-item")
    msg = [message.text for message in msg_got]
    print(msg)
    if msg == []:
        msg = ['none']
    # sending response according to message
    for key, value in response.items():
        if key in msg[-1]:
            print(key, value)
            reply = driver.find_element_by_class_name("_2A8P4")
            actions = ActionChains(driver)
            actions.send_keys(value + Keys.ENTER)
            actions.perform()
            time.sleep(10)
            print('MESSAGE FOUND :)')
        else:
            print('No one message you :( ')

driver.quit()
