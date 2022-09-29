from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
#import MainScores
#from flask import Flask

def test_score_services (url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    my_driver = webdriver.Chrome('/',options=chrome_options)
    my_driver.implicitly_wait(10)
    #my_driver = webdriver.Remote()
    my_driver.get(url)
    if 0 < int(my_driver.find_element(By.ID,"score").text) < 1001:
        print("true")
        return True
    else:
        print("false")
        sys.exit(-1)
        return False


def main_function():
    #MainScores.app_run(Flask(__name__, template_folder='templates', static_folder='static'))
    if test_score_services("http://localhost:8777"):
        return 0
    else:
        try : raise Exception('ÓS exit code')
        except:
            return -1

main_function()