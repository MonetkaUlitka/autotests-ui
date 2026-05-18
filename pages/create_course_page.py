from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.views.empty_view_compoments import EmptyViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponent(page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

# Блок загрузки изображения для превью курса: картинка курса не выбрана
        self.upload_image_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_image_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.upload_image_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button').locator('input[type="file"]')


# Блок загрузки изображения для превью курса: картинка курса выбрана
        self.uploaded_course_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        self.remove_uploaded_course_image_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

# Блок с полями для создания курса
        self.course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.course_description_textarea = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

# Блок с добавление упражнений в курс: упражнения не добавлены
        self.exercises_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.add_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

# # Блок с добавление упражнений в курс: упражнения добавлены
#         self.exercises_subtitle = page.get_by_test_id('create-course-exercise-0-box-toolbar-subtitle-text')
#         self.exercise_title_input = page.get_by_test_id('create-course-exercise-form-title-0-input').locator('input')
#         self.empty_exercise_description_input = page.get_by_test_id('create-course-exercise-form-description-0-input').locator('input')
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

    def check_visible_image_preview_empty_view(self):
        self.preview_empty_view.check_visible(
            title = 'No image selected',
            description = 'Preview of selected image will be displayed here'
        )

    def check_visible_image_upload_view(self,is_image_uploaded:bool = False):
        expect(self.upload_image_title).to_be_visible()
        expect(self.upload_image_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.upload_image_description).to_be_visible()
        expect(self.upload_image_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_image_button).to_be_visible()

        if is_image_uploaded:
            expect(self.preview_empty_view_icon).not_to_be_visible()
            expect(self.uploaded_course_image).to_be_visible()
            expect(self.remove_uploaded_course_image_button).to_be_visible()
        else:
            expect(self.preview_empty_view_icon).to_be_visible()
            expect(self.preview_empty_image_title).to_be_visible()
            expect(self.preview_empty_image_title).to_have_text('No image selected')
            expect(self.preview_empty_view_description).to_be_visible()
            expect(self.preview_empty_view_description).to_have_text('Preview of selected image will be displayed here')


    def click_remove_image_button(self):
        expect(self.remove_uploaded_course_image_button).to_be_visible()
        self.remove_uploaded_course_image_button.click()

    def check_visible_preview_image(self):
        expect(self.uploaded_course_image).to_be_visible()

    def upload_preview_image(self, file:str):
        expect(self.upload_image_button).to_be_visible()
        self.upload_image_button.set_input_files(file)


    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: int, min_score: int):
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
        expect(self.empty_exercise_view_icon).to_be_visible()

        expect(self.empty_exercise_view_title).to_be_visible()
        expect(self.empty_exercise_view_title).to_have_text('There is no exercises')

        expect(self.empty_exercise_view_description).to_be_visible()
        expect(self.empty_exercise_view_description).to_have_text('Click on "Create exercise" button to create new exercise')

    def click_delete_exercise_button(self, index:int):
        self.delete_exercise_button.nth(index).click()

# Посмотреть код и повторить. Нужно разобраться почему я не смогла это сделать - чего мне не хватило для понимания.

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)


    def fill_create_exercise_form(self, index:int, title:str, description:str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        exercise_description_input.fill(description)


    


        
    
    



