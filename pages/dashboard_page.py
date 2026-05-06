from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
        self.dashboard_button = page.get_by_test_id('dashboard-drawer-list-item-button')
        self.student_widget_title = page.get_by_test_id('students-widget-title-text')
        self.student_bar = page.get_by_test_id('students-bar-chart')
        self.activities_widget_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_line = page.get_by_test_id('activities-line-chart')
        self.courses_widget_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_pie = page.get_by_test_id('courses-pie-chart')
        self.scores_widget_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_scatter = page.get_by_test_id('scores-scatter-chart')

    def check_dashboard_header(self):
        expect(self.dashboard_header).to_be_visible()