from selenium import webdriver

browser = webdriver.Chrome()
with open('course2.js', 'r') as f:
    js = f.read()
print(browser.execute_script(js))