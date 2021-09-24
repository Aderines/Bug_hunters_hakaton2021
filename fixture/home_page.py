class HomeHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    # Здесь можно начинать писать функции для тестирования страницы

    def open_start_page(self):
        self.wd.find_element_by_css_selector(".page-homepage.pageType-ContentPage")
        if self.wd.current_url.endswith("/en") is not True:
            self.wd.find_element_by_css_selector(".js-mobile-logo").click()
            self.wd.find_elements_by_css_selector(".page-homepage.pageType-ContentPage")

    def click_on_banners(self, name):
        self.wd.find_element_by_css_selector(f".js-responsive-image[title='{name}']")
        self.wd.find_element_by_css_selector(f".js-responsive-image[title='{name}']").click()
        self.wd.find_element_by_css_selector(".product__list--wrapper")

    def get_text_cataloge_name(self):
        self.wd.find_element_by_css_selector(".breadcrumb .active")
        return self.wd.find_element_by_css_selector(".breadcrumb .active").text
