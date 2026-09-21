from playwright.sync_api import Page, expect
from typing import Pattern
from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier : str):
        super().__init__(page)

        self.sidebar_icon = Icon(page, locator=f'{identifier}-drawer-list-item-icon', name = "Sidebar icon")
        self.sidebar_title = Text(page, locator=f'{identifier}-drawer-list-item-title-text', name = "Sidebar title")
        self.sidebar_button = Button(page, locator=f'{identifier}-drawer-list-item-button', name = "Sidebar button")


    def check_visible(self, title: str):
        self.sidebar_icon.check_visible()
        self.sidebar_title.check_visible()
        self.sidebar_title.check_have_text(title)

        self.sidebar_button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.sidebar_button.click()
        self.check_current_url(expected_url)