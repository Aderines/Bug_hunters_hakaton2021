class BasketHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    # Здесь можно начинать писать функции для тестирования страницы

    def add_to_basket(self):
        self.wd.find_element_by_css_selector(".yCmsComponent.nav__link.js_nav__link").click()
        self.wd.find_element_by_css_selector(
            ".btn.btn-primary.btn-block.glyphicon.glyphicon-shopping-cart.js-enable-btn").click()
        self.wd.find_element_by_css_selector(".btn.btn-primary.btn-block.add-to-cart-button").click()

    def delete_basket(self):
        self.wd.find_element_by_css_selector(".glyphicon.glyphicon-option-vertical").click()
        self.wd.find_element_by_xpath('//*[@id="actionEntry_0"]/a').click()
        delete = self.wd.find_element_by_css_selector("content").find
        delete = int(delete.split().text)
        return delete

    def check_basket(self):
        quantity = self.wd.find_element_by_css_selector(".js-cart-top-totals.cart__top--totals").text
        quantity = int(quantity.split()[0])
        return quantity

    def verify_id_basket(self):
        id = self.wd.find_element_by_css_selector(".cart__id").text
        len_id = len(id)
        return len_id

    def help_popup(self):
        id = self.wd.find_element_by_class_name(".cart__id")
        self.wd.find_element_by_class_name(".help.js-cart-help").click()
        popup = self.wd.find_element_by_id(".cboxLoadedContent")
        if id == popup:
            return self.wd.find_element_by_id(".cboxLoadedContent").text
        else:
            print("Invalid ID name in help")

    def verify_new_cart(self):
        self.wd.find_element_by_css_selector(".yCmsComponent.nav__link.js_nav__link").click()
        self.wd.find_element_by_css_selector(
            ".btn.btn-primary.btn-block.glyphicon.glyphicon-shopping-cart.js-enable-btn").click()
        self.wd.find_element_by_css_selector(".btn.btn-primary.btn-block.add-to-cart-button").click()
        self.wd.find_element_by_css_selector(".save__cart--link.cart__head--link.js-save-cart-link").click()

    def verify_continue_shopping(self):
        self.wd.find_element_by_css_selector(".yCmsComponent.nav__link.js_nav__link").click()
        self.wd.find_element_by_css_selector(
            ".btn.btn-primary.btn-block.glyphicon.glyphicon-shopping-cart.js-enable-btn").click()
        self.wd.find_element_by_css_selector(".btn.btn-primary.btn-block.add-to-cart-button").click()
        self.wd.find_element_by_css_selector(
            ".btn.btn-default.btn-block.btn--continue-shopping.js-continue-shopping-button").click()
        return self.wd.current_url
