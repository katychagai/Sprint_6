import pytest
import allure
from src.pages.home_faq_page import HomeFaqPage
from src.helpers import FAQ_TEST_DATA



class TestFAQAccordion:

    @pytest.mark.parametrize("question_number,expected_keywords", FAQ_TEST_DATA)
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
