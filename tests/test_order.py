import pytest
import allure
from src.pages.order_page import OrderPage
from src.pages.home_page import HomePage
from src.helpers import ORDER_TEST_DATA


class TestOrderScooter:

    @pytest.mark.parametrize("order_data", ORDER_TEST_DATA)
    def test_order_scooter(self, driver, settings, order_data):
        
        page = OrderPage(driver, settings.base_url)
        
        with allure.step("Открываем страницу заказа"):
            page.open_order()
            
        with allure.step("Заполняем первую страницу формы"):
            page.fill_order_form(order_data)
            
        with allure.step("Переходим на вторую страницу"):
            # Проверяем что кнопка кликабельна
            page.wait_for_clickable(page.NEXT_BUTTON, timeout=10)
            page.click(page.NEXT_BUTTON)
            
        with allure.step("Заполняем вторую страницу формы"):
            page.fill_second_page_form(order_data)
            
        with allure.step("Подтверждаем заказ"):
            page.confirm_order()
            
        with allure.step("Проверяем успешное оформление заказа"):
            page.wait_for_visible(page.SUCCESS_BANNER, timeout=20)
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
            home_page.wait_for_page_load(timeout=5)
            current_url = home_page.get_current_url()
            assert "scooter" in current_url.lower()
