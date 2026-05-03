from playwright.sync_api import Page, expect 
import pytest 


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    courses_text = page.get_by_test_id('courses-list-empty-view-title-text')
    
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text('Courses')
    
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('There is no results')
    