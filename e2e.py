from selenium import webdriver
from selenium.webdriver.common.by import By


def test_score_services (url):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    if 0 < int(my_driver.find_element(By.ID,"score").text) < 1001:
        return True
    else:
        return False


def main_function():
    if test_score_services("http://localhost:5001"):
        return 0
    else:
        try : raise Exception('ÓS exit code')
        except:
            return -1

