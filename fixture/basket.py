class BasketHelper:

    def __init__(self, app):
        self.app = app
        self.wd = None

    # Здесь можно начинать писать функции для тестирования страницы

    def add_to_basket(self):
        self.wd = self.app.wd
        self.wd.find_element_by_css_selector(".yCmsComponent.nav__link.js_nav__link").click()
        self.wd.find_element_by_css_selector(".btn.btn-primary.btn-block.glyphicon.glyphicon-shopping-cart.js-enable-btn").click()
        self.wd.find_element_by_css_selector(".btn.btn-primary.btn-block.add-to-cart-button").click()

    def verify_id_basket(self, id):
        self.wd = self.app.wd
        return self.wd.find_element_by_css_selector(f"cart__{id}").text


    def help_popup(self):
        self.wd = self.app.wd
        id = self.wd.find_element_by_class_name("cart__id")
        popup = self.wd.find_element_by_class_name("help js-cart-help").click()
        if id == popup:
            return self.wd.find_element_by_id("cboxLoadedContent").text
        else:
            print("Invalid ID name in help")


    def verify_new_cart(self):
        self.ws = self.app.wd
        self.wd.find_element_by_class_name("save__cart--link cart__head--link js-save-cart-link").click()
        if self.wd.current_url == "https://apparel-uk.local:9002/ucstorefront/en/login":
            return True

    def verify_continue_shopping(self):
        self.ws = self.app.wd
        self.wd.find_element_by_class_name
