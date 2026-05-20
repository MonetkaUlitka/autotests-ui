from playwright.sync_api import Page, expect 
from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

         # Меню курса
        self.menu_button = Button(page, locator='course-view-menu-button', name='menu')

        self.edit_menu_item = Button(page, locator='course-view-edit-menu-item-text', name='Edit')
        self.course_edit_icon = Icon(page, locator='EditOutlinedIcon', name='Edit Icon')

        self.delete_menu_item = Button(page, locator='course-view-delete-menu-item-text', name='Delete')
        self.course_delete_icon = Icon(page, locator='DeleteOutlineOutlinedIcon', name='Delete Icon')

    def click_edit(self, index:int):
        self.menu_button.click(nth=index)
        
        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    def click_delete(self, index:int):
        self.menu_button.click(nth=index)
        
        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index) 