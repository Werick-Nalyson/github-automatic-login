from selenium import webdriver
from time import sleep
import sys


class GithubAutoLogin:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Profile')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def access_url(self, url):
        self.chrome.get(url)

    def close_chrome(self):
        self.chrome.quit()

    def click_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_xpath(
                '/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def click_profile(self):
        try:
            profile = self.chrome.find_element_by_xpath(
                '/html/body/div[1]/header/div[7]/details/summary')
            profile.click()
        except Exception:
            print(Exception)

    def click_sign_out(self):
        try:
            profile = self.chrome.find_element_by_xpath(
                '/html/body/div[1]/header/div[7]/details/details-menu/form/button')
            profile.click()
        except Exception as err:
            print('Erro fazer logout:', err)

    def check_corect_username(self, usuario):
        profile_link = self.chrome.find_element_by_class_name(
            'user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def insert_credentials(self, email, password):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys(email)
            input_password.send_keys(password)
            btn_login.click()

        except Exception as err:
            print('Erro ao fazer login:', err)


if __name__ == '__main__':
    chrome = GithubAutoLogin()
    chrome.access_url('https://github.com/')

    try:
        chrome.click_sign_in()
        chrome.insert_credentials("emailexample@gmail.com", "passwordexample")
        chrome.click_profile()

        sleep(1)
        chrome.check_corect_username('Werick-Nalyson')

        sleep(1)
        chrome.click_sign_out()
    except Exception as err:
        print('Um erro ocorreu:', err)
    else:
        chrome.click_profile()

        sleep(1)
        chrome.click_sign_out()

        chrome.click_sign_in()
        chrome.insert_credentials("emailexample@gmail.com", "passwordexample")
    finally:
        sleep(5)
        chrome.close_chrome()
        sys.exit()
