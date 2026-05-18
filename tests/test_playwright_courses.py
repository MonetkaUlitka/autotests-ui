from playwright.sync_api import Page, expect 
from pages.courses_list_page import CoursesListPage
import pytest 


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.empty_view.check_visible(title = 'There is no results', description ='Results from the load test pipeline will be displayed here')

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    
    


    