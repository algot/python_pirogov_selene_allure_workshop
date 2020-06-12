from selene.support.jquery_style_selectors import s


class MainPage:
    def __init__(self):
        self.icon_waffle = s('//div[contains(@class, "slds-icon-waffle")]')
