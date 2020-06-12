from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.MainPage import MainPage


class LoginPage:
    def __init__(self):
        self.username_input = s('#username')
        self.password_input = s('#password')
        self.login_button = s('#Login')

    def open(self):
        browser.open_url('/')
        return self

    def login_as(self, user):
        self.username_input.set(user.name)
        self.password_input.set(user.password)
        self.login_button.click()
        return MainPage()
