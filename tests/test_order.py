import pytest
import allure
import time
from src.pages.order_page import OrderPage
from src.pages.home_page import HomePage


class TestOrderScooter:

    @pytest.mark.parametrize("order_data", [
        {
            "first_name": "Иван",
            "last_name": "Иванов", 
            "address": "Москва, ул. Тверская, д. 1",
            "metro": "Сокольники",
            "phone": "89604715879",
            "date": "25.09.2025",
            "rental_period": "сутки",
            "color": "чёрный жемчуг",
            "comment": "Позвонить за час до доставки"
        },
        {
            "first_name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский проспект, д. 10", 
            "metro": "Черкизовская",
            "phone": "89604715880",
            "date": "26.09.2025",
            "rental_period": "двое суток",
            "color": "серая безысходность",
            "comment": "Оставить у подъезда"
        }
    ])
    def test_order_scooter(self, driver, settings, order_data):
        
        
        page = OrderPage(driver, settings.base_url)
        
        with allure.step("Открываем страницу заказа"):
            page.open_order()
            
        with allure.step("Заполняем первую страницу формы"):
            page.type(page.FIRST_NAME_INPUT, order_data["first_name"])
            page.type(page.LAST_NAME_INPUT, order_data["last_name"])
            page.type(page.ADDRESS_INPUT, order_data["address"])
            page.type(page.PHONE_INPUT, order_data["phone"])
            page.select_metro_station(order_data["metro"])
            
        with allure.step("Переходим на вторую страницу"):
            # Проверяем что кнопка кликабельна
            page.wait_for_clickable(page.NEXT_BUTTON, timeout=10)
            time.sleep(1)  # Небольшая пауза для активации кнопки
            page.click(page.NEXT_BUTTON)
            
        with allure.step("Заполняем вторую страницу формы"):
            # Ждем появления поля даты
            page.wait_for_visible(page.DATE_INPUT, timeout=20)
            page.type(page.DATE_INPUT, order_data["date"])
            
            # Скрываем календарь если он мешает
            page.execute_script("document.querySelector('.react-datepicker').style.display = 'none';")
            
            # Выбираем срок аренды из dropdown
            page.select_rental_period(order_data['rental_period'])
            
            # Выбираем цвет самоката
            if order_data["color"] == "чёрный жемчуг":
                page.click(page.COLOR_CHECKBOX_BLACK)
            elif order_data["color"] == "серая безысходность":
                page.click(page.COLOR_CHECKBOX_GRAY)
                
            page.type(page.COMMENT_INPUT, order_data["comment"])
            
        with allure.step("Подтверждаем заказ"):
            page.click(page.ORDER_BUTTON)
            page.wait_for_visible(page.ORDER_MODAL_HEADER, timeout=15)
            page.wait_for_visible(page.CONFIRM_BUTTON, timeout=15)
            page.click(page.CONFIRM_BUTTON)
            
        with allure.step("Проверяем успешное оформление заказа"):
            page.wait_for_visible(page.SUCCESS_BANNER, timeout=20)
            
            # Извлекаем номер заказа
            order_text = page.get_text(page.SUCCESS_BANNER)
            assert "Заказ оформлен" in order_text
            
        with allure.step("Нажимаем кнопку 'Посмотреть статус'"):
            page.wait_for_visible(page.VIEW_STATUS_BUTTON, timeout=10)
            page.click(page.VIEW_STATUS_BUTTON)
            
            
        with allure.step("Проверяем переход на главную страницу через логотип"):
            home_page = HomePage(page.driver, page.base_url)
            
            page.wait_for_visible(home_page.LOGO_SCOOTER, timeout=10)
            page.click(home_page.LOGO_SCOOTER)
            home_page.wait_for_visible(home_page.FAQ_LINK, timeout=10)
            
        with allure.step("Проверяем клик по логотипу Яндекса"):
            home_page.wait_for_visible(home_page.LOGO_YANDEX, timeout=10)
            home_page.click(home_page.LOGO_YANDEX)
            time.sleep(2)
            current_url = home_page.driver.current_url
            assert "scooter" in current_url.lower()


