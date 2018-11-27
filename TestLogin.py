

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_login_to_jira():
    # driver = webdriver.Chrome('C:\\Users\\Анастасия\\Desktop\\python\\PySample\\chromedriver_win32\\chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://jira.hillel.it:8080/secure/Dashboard.jspa')
    assert "System Dashboard - Hillel IT School JIRA" in driver.title




