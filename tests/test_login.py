from selene.support.conditions import be
from src.pages.LoginPage import LoginPage
from src.domain.user import User

USERNAME = 'username'
PASSWORD = 'password'


def test_admin_can_login():
    admin = User(USERNAME, PASSWORD)

    (LoginPage()
     .open()
     .login_as(admin)
     .icon_waffle.should_be(be.visible, 20))
