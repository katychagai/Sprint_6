from selenium.webdriver.common.by import By

from .base_page import BasePage


class OrderPage(BasePage):
    PATH = "/order"

    # Поля формы заказа
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_INPUT = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_CHECKBOX_BLACK = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    COLOR_CHECKBOX_GRAY = (By.XPATH, "//label[contains(text(),'серая безысходность')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Заголовки страниц
    ORDER_HEAD_SECOND_PAGE = (By.XPATH, "//div[contains(@class, 'Order_Header')]")
    ORDER_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    # Кнопки
    ORDER_LINK = (By.XPATH, "//button[contains(text(),'Заказать')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Да']")
    
    # Заказ оформлен
    SUCCESS_BANNER = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
    
    # Опции dropdown
    METRO_OPTION = (By.XPATH, "//ul//li")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(text(), '{}')]")
    
    # Кнопка просмотра статуса
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Посмотреть статус']")

    def open_order(self):
        self.open_root()
        self.click(self.ORDER_LINK)

    def select_metro_station(self, station_name):
        # Кликаем на поле метро для открытия списка
        self.click(self.METRO_INPUT)
        # Вводим название станции для поиска
        self.type(self.METRO_INPUT, station_name)
            
        # Ждем появления опций и кликаем на первую найденную
        self.wait_for_visible(self.METRO_OPTION, timeout=5)
        self.click(self.METRO_OPTION)

    def select_rental_period(self, rental_period):
        """Select rental period from dropdown"""
        self.click(self.RENTAL_PERIOD_INPUT)
        rental_option = (self.RENTAL_OPTION[0], self.RENTAL_OPTION[1].format(rental_period))
        self.wait_for_visible(rental_option, timeout=5)
        self.click(rental_option)

    def place_order(self, first_name, last_name, address, metro, phone, date, rental_period, color, comment):
        # Заполняем первую страницу формы
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.ADDRESS_INPUT, address)
        self.select_metro_station(metro)
        self.type(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        
        # Заполняем вторую страницу формы
        self.type(self.DATE_INPUT, date)
        self.type(self.RENTAL_PERIOD_INPUT, rental_period)
        
        # Выбираем цвет самоката
        if color == "чёрный жемчуг":
            self.click(self.COLOR_CHECKBOX_BLACK)
        elif color == "серая безысходность":
            self.click(self.COLOR_CHECKBOX_GRAY)
        
        self.type(self.COMMENT_INPUT, comment)
        
        # Подтверждаем заказ
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    def success_banner_visible(self):
        return self.is_visible(self.SUCCESS_BANNER)