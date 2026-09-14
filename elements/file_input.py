from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_file(self, input_file: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(input_file)