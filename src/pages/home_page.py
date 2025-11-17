from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    PATH = "/"

    # Локаторы для сайта
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex') and contains(@href, 'yandex.ru')]")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    FAQ_LINK = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
    ORDER_LINK = (By.XPATH, "//button[contains(text(),'Заказать')]")

    def open_home(self):
        self.open_root()

    def go_to_faq(self):
        self.click(self.FAQ_LINK)

    def go_to_order(self):
        self.click(self.ORDER_LINK)