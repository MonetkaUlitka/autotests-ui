from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.image import Image

class ChartViewComponent(BaseComponent):
    def __init__(self, page:Page, identifier:str, chart_type:str):
        super().__init__(page)

        self.title = Text(page, locator=f'{identifier}-widget-title-text', name='Title')
        self.chart = Image(page, locator=f'{identifier}-{chart_type}-chart', name='Chart')

    def check_visible(self, expected_title:str):
        self.title.check_visible()
        self.title.check_text(expected_title)

        self.chart.check_visible()