from selenium import webdriver
from fixture.basket import BasketHelper
from fixture.categories import CategoriesHelper
from fixture.global_header import GlobalHeaderHelper
from fixture.home_page import HomeHelper
from fixture.proceed_to_checkout import CheckoutHelper
from fixture.product import ProductHelper


class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.wd = webdriver.Chrome(chrome_options=options)
        self.wd.implicitly_wait(10)
        self.basket = BasketHelper(self)
        self.categories = CategoriesHelper(self)
        self.global_header = GlobalHeaderHelper(self)
        self.home = HomeHelper(self)
        self.checkout = CheckoutHelper(self)
        self.product = ProductHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://apparel-uk.local:9002/ucstorefront/en")
        wd.find_element_by_css_selector(".page-homepage.pageType-ContentPage")
        wd.find_element_by_class_name()


    def add_to_basket(self):
        wd = self.wd
        self.basket.add_to_basket()

    def verify_id_basket(self):
        wd = self.wd
        self.basket.verify_id_basket()


    def destroy(self):
        self.wd.quit()