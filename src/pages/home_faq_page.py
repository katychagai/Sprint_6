from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomeFaqPage(BasePage):

    FAQ_SUB_HEADER = (By.XPATH, "//div[contains(@class, 'Home_SubHeader')]")
    ACCORDION = (By.XPATH, "//div[@data-accordion-component='Accordion']")

    # Вопросы FAQ
    QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"), 
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7")
    }

    # Ответы FAQ
    ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7")
    }

    # Раскрытые вопросы
    EXPANDED_QUESTIONS = {
        0: (By.XPATH, "//div[@id='accordion__heading-0' and @aria-expanded='true']"),
        1: (By.XPATH, "//div[@id='accordion__heading-1' and @aria-expanded='true']"),
        2: (By.XPATH, "//div[@id='accordion__heading-2' and @aria-expanded='true']"),
        3: (By.XPATH, "//div[@id='accordion__heading-3' and @aria-expanded='true']"),
        4: (By.XPATH, "//div[@id='accordion__heading-4' and @aria-expanded='true']"),
        5: (By.XPATH, "//div[@id='accordion__heading-5' and @aria-expanded='true']"),
        6: (By.XPATH, "//div[@id='accordion__heading-6' and @aria-expanded='true']"),
        7: (By.XPATH, "//div[@id='accordion__heading-7' and @aria-expanded='true']")
    }

    def open_faq(self):
        self.open_root()
        self.wait_for_page_load(timeout=30)
        self.wait_for_visible(self.ACCORDION, timeout=20)
        self.scroll_into_view(self.FAQ_SUB_HEADER)

    def expand_question(self, question_number):
        question_locator = self.QUESTIONS[question_number]
        answer_locator = self.ANSWERS[question_number]
        
        self.scroll_into_view(question_locator)
        element = self.wait_for_visible(question_locator, timeout=20)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_visible(answer_locator, timeout=20)
        self.wait_for_attribute(question_locator, "aria-expanded", "true", timeout=20)

    def get_answer_text(self, question_number):
        answer_locator = self.ANSWERS[question_number]
        return self.get_text(answer_locator)

    def is_question_expanded(self, question_number):
        return self.is_element_present(self.EXPANDED_QUESTIONS[question_number], timeout=3)

    def is_answer_visible(self, question_number):
        return self.is_visible(self.ANSWERS[question_number], timeout=3)