import pytest
import allure
from src.pages.home_faq_page import HomeFaqPage



class TestFAQ:

    @pytest.mark.parametrize("question_number,expected_keywords", [
        (0, ["Сутки", "400", "рублей"]),
        (1, ["пока", "один", "самокат"]),
        (2, ["допустим", "заказ", "привозим"]),
        (3, ["завтрашнего", "дня", "расторопнее"]),
        (4, ["пока", "поддержку", "1010"]),
        (5, ["зарядкой", "восемь", "суток"]),
        (6, ["пока", "самокат", "привезли"]),
        (7, ["самокатов", "москве", "области"])
    ])
    def test_faq_questions(self, faq_page, question_number, expected_keywords):
        with allure.step(f"Раскрываем вопрос {question_number + 1}"):
            faq_page.expand_question(question_number)
            
        with allure.step("Проверяем что вопрос раскрыт"):
            assert faq_page.is_question_expanded(question_number)
            
        with allure.step("Проверяем что ответ виден"):
            assert faq_page.is_answer_visible(question_number)
            
        with allure.step("Проверяем содержимое ответа"):
            answer_text = faq_page.get_answer_text(question_number)
            for keyword in expected_keywords:
                assert keyword.lower() in answer_text.lower()


