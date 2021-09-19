from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixture.basket import BasketHelper
from fixture.categories import CategoriesHelper
from fixture.global_header import GlobalHeaderHelper
from fixture.home_page import HomeHelper
from fixture.proceed_to_checkout import CheckoutHelper
from fixture.product import ProductHelper
from fixture.registration_and_login import RegistrationLoginHelper


class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--start-maximized')
        self.wd = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        self.wd.implicitly_wait(10)
        self.basket = BasketHelper(self)
        self.categories = CategoriesHelper(self)
        self.global_header = GlobalHeaderHelper(self)
        self.home = HomeHelper(self)
        self.checkout = CheckoutHelper(self)
        self.product = ProductHelper(self)
        self.registration = RegistrationLoginHelper(self)

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

    def destroy(self):
        self.wd.quit()
