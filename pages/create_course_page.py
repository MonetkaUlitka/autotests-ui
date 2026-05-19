from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.views.empty_view_compoments import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent


class CreateCoursePage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')
       

# Блок с полями для создания курса
        self.course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.course_description_textarea = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

# Блок с добавление упражнений в курс: упражнения не добавлены
        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.add_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        self.delete_exercise_button = page.get_by_test_id('create-course-exercise-0-box-toolbar-delete-exercise-button')


    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')


    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.course_title_input).to_be_visible()
        expect(self.course_title_input).to_have_value(title)

        expect(self.course_estimated_time_input).to_be_visible()
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        expect(self.course_description_textarea).to_be_visible()
        expect(self.course_description_textarea).to_have_value(description)

        expect(self.course_max_score_input).to_be_visible()
        expect(self.course_max_score_input).to_have_value(str(max_score))

        expect(self.course_min_score_input).to_be_visible()
        expect(self.course_min_score_input).to_have_value(str(min_score))

    def fill_create_course_form(self, title:str, estimated_time:str, description:str, max_score:str, min_score:str):
        self.course_title_input.fill(title)
        expect(self.course_title_input).to_have_value(title)

        self.course_estimated_time_input.fill(estimated_time)
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        self.course_description_textarea.fill(description)
        expect(self.course_description_textarea).to_have_value(description)

        self.course_max_score_input.fill(max_score)
        expect(self.course_max_score_input).to_have_value(max_score)

        self.course_min_score_input.fill(min_score)
        expect(self.course_min_score_input).to_have_value(min_score)

    def check_visible_exercises_title(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_create_exercise_button(self):
        expect(self.add_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.add_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title = 'There is no exercises',
            description = 'Click on "Create exercise" button to create new exercise'
        )


    def click_delete_exercise_button(self, index:int):
        delete_button = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-delete-exercise-button")
        expect(delete_button).to_be_visible()
        delete_button.click()



    


        
    
    



