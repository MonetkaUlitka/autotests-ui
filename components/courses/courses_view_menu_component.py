from playwright.sync_api import Page, expect 
from components.base_component import BaseComponent

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

         # Меню курса
        self.menu_button = page.get_by_test_id('course-view-menu-button')

        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item-text')
        self.course_edit_icon = page.get_by_test_id('EditOutlinedIcon')

        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item-text')
        self.course_delete_icon = page.get_by_test_id('DeleteOutlineOutlinedIcon')

    def click_edit(self, index:int):
        self.menu_button.nth(index).click()
        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.click()

    def click_delete(self, index:int):
        self.menu_button.nth(index).click()
        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.click()