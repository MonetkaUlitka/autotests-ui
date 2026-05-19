from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
        
        self.students_chart_view = ChartViewComponent(identifier="students", chart_type="bar")
        self.activities_chart_view = ChartViewComponent(identifier="activities", chart_type="line")
        self.scores_chart_view = ChartViewComponent(identifier="scores", chart_type="pie")
        self.courses_chart_view = ChartViewComponent(identifier="courses", chart_type="scatter")


        self.dashboard_button = page.get_by_test_id('dashboard-drawer-list-item-button')

    