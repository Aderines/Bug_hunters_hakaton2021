import time

from selenium.webdriver.common.action_chains import ActionChains


class HomeHelper:

    def __init__(self, app):
        self.app = app
        self.wd = None


# Здесь можно начинать писать функции для тестирования страницы

    def open_start_page(self):
        self.wd = self.app.wd
        if self.wd.current_url.endswith("/en") is not True:
            self.click_logo()

    def click_logo(self):
        logo = self.wd.find_element_by_css_selector("title='hybris Accelerator'")
        ActionChains(self.wd).move_to_element(logo).click()
        self.wd.find_elements_by_css_selector(".page-homepage.pageType-ContentPage")

    def click_on_banners(self, name):
        self.wd.find_element_by_css_selector(f".js-responsive-image[title='{name}']")
        self.wd.find_element_by_css_selector(f".js-responsive-image[title='{name}']").click()
        self.wd.find_element_by_css_selector(".product__list--wrapper")

    def get_text_cataloge_name(self):
        self.wd.find_element_by_css_selector(".breadcrumb .active")
        return self.wd.find_element_by_css_selector(".breadcrumb .active").text

#--------Best Prouducts---------------------

    def best_selling_product(self):
        return self.wd.find_element_by_xpath(
            "//*[contains(@class, 'carousel__component--headline') and contains(., 'Best Selling Products')]/..")

    def scroll_to_best_selling(self):
        best_selling = self.best_selling_product()
        ActionChains(self.wd).move_to_element(best_selling).perform()

    def count_best_selling_products(self):
        product = self.best_selling_product()
        count = len(product.find_elements_by_css_selector(".owl-item"))
        return count

    def get_name_best_selling_product(self, index):
        product = self.best_selling_product()
        name = product.find_elements_by_css_selector(".carousel__item--name")[index].text
        if name == '':
            product.find_element_by_css_selector(".owl-prev .glyphicon-chevron-left").click()
            time.sleep(2)
        name = product.find_elements_by_css_selector(".carousel__item--name")[index].text
        return name

    def click_on_best_selling_product(self, index):
        product = self.best_selling_product()
        product.find_elements_by_css_selector(".carousel__item--name")[index].click()
        self.wd.find_element_by_css_selector(".product-details.page-title")

    def get_text_name(self):
        name = self.wd.find_element_by_css_selector(".product-details.page-title .name").text
        name1 = name.split("ID")
        name2 = name1[0].upper()
        return name2

    def click_on_button_home(self):
        self.wd.find_element_by_xpath("//*[contains(@class, 'breadcrumb-section')]//a[contains(., 'Home')]").click()
        self.wd.find_elements_by_css_selector(".page-homepage.pageType-ContentPage")

#------New Products-----------------------

    def new_product(self):
        return self.wd.find_element_by_xpath("//div[@class='carousel__component' and contains(., 'New')]/.. ")

    def scroll_to_new_selling(self):
        new = self.new_product()
        ActionChains(self.wd).move_to_element(new).perform()

    def count_new_products(self):
        product = self.new_product()
        count = len(product.find_elements_by_css_selector(".owl-item"))
        return count

    def get_name_new_product(self, index):
        product = self.new_product()
        name = product.find_elements_by_css_selector(".carousel__item--name")[index].text
        if name == '':
            product.find_element_by_css_selector(".owl-prev .glyphicon-chevron-left").click()
            time.sleep(2)
        name = product.find_elements_by_css_selector(".carousel__item--name")[index].text
        return name

    def click_on_new_product(self, index):
        product = self.new_product()
        product.find_elements_by_css_selector(".carousel__item--name")[index].click()
        self.wd.find_element_by_css_selector(".product-details.page-title")
