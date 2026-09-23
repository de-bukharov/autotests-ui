from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.textarea import TextArea
from elements.input import Input

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, locator="create-course-form-title-input", name="Title input")
        self.create_course_estimated_time_input = Input(
            page, locator="create-course-form-estimated-time-input", name="Estimated time input")
        self.create_course_description_textarea = TextArea(
            page, locator="create-course-form-description-input", name="Description textarea")

        self.create_course_max_score_input = Input(page, locator="create-course-form-max-score-input", name="Max score input")
        self.create_course_min_score_input = Input(page, locator="create-course-form-min-score-input", name="Min score input")


    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)




    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        expect(self.create_course_description_textarea).to_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input).to_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input).to_have_value(min_score)