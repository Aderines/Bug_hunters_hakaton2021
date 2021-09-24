from selenium import webdriver

from fixture.basket import BasketHelper
from fixture.categories import CategoriesHelper
from fixture.global_header import GlobalHeaderHelper
from fixture.home_page import HomeHelper
from fixture.proceed_to_checkout import CheckoutHelper
from fixture.product import ProductHelper

URL = r"https://apparel-uk.local:9002/ucstorefront/en"
PATH = r"C:\Users\denki\Desktop\ui-tests\chrome4\chromedriver.exe"


class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--start-maximized')
        self.wd = webdriver.Chrome(executable_path=PATH, chrome_options=options)
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
        self.wd.get(URL)
        self.home.open_start_page()

    def add_to_basket(self):
        self.wd.get(URL)
        self.basket.add_to_basket()

    def delete_from_basket(self):
        self.wd.get(URL)
        self.basket.delete_basket()

    def check_basket(self):
        self.wd.get(URL)
        self.basket.check_basket()

    def verify_id_basket(self, id):
        self.wd.get(URL)
        self.basket.verify_id_basket(id)

    def verify_new_cart(self):
        self.wd.get(URL)
        self.basket.verify_new_cart()

    def help_popup(self):
        self.wd.get(URL)
        self.basket.help_popup()

    def verify_continue_shopping(self):
        self.wd.get(URL)
        self.basket.verify_continue_shopping()

    def destroy(self):
        self.wd.quit()
