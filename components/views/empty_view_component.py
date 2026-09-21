from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.empty_view_icon = Icon(page, locator=f"{identifier}-empty-view-icon", name = "Empty view icon")
        self.empty_view_title = Text(page, locator=f"{identifier}-empty-view-title-text", name = "Empty view title")
        self.empty_view_description = Text(page, locator=f"{identifier}-empty-view-description-text", name = "Empty view description")

    def check_visible(self, title: str, description: str):
        self.empty_view_icon.check_visible()
        self.empty_view_title.check_visible()
        self.empty_view_title.check_visible()
        self.empty_view_title.check_have_text(title)
        self.empty_view_description.check_visible()
        self.empty_view_description.check_have_text(description)