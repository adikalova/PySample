from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def test_login_to_jira():
    # driver = webdriver.Chrome('C:\\Users\\Анастасия\\Desktop\\python\\PySample\\chromedriver_win32\\chromedriver.exe')
    driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://jira.hillel.it:8080/secure/Dashboard.jspa')
    assert "System Dashboard - Hillel IT School JIRA" in driver.title

    driver.find_element_by_id("login-form-username").clear()
    driver.find_element_by_id("login-form-username").send_keys("adikalova")
    driver.find_element_by_id("login-form-password").clear()
    driver.find_element_by_id("login-form-password").send_keys("1234567")
    driver.find_element_by_id("login").submit()

    assert driver.page_source.find('Dashboard')

    driver.implicitly_wait(3)

    driver.find_element(By.ID, "create_link").click()
    driver.implicitly_wait(7)

    driver.find_element_by_id("summary").clear()
    driver.find_element_by_id("summary").send_keys("Test26")
    driver.find_element_by_id("description").send_keys("Text")
    driver.find_element_by_id("create-issue-submit").click()

    driver.implicitly_wait(7)
    assert driver.find_element_by_xpath("//*[contains(text(),'Test26')]")


