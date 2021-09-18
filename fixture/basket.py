class BasketHelper:

    def __init__(self, app):
        self.app = app
        self.wd = None

    # Здесь можно начинать писать функции для тестирования страницы

    def add_to_cart(self):
        self.wd = self.app.wd
        self.wd.find_element_by_xpath("/html/body/main/header/nav[3]/div/ul[2]/li[1]/span[1]/a").click()
        self.wd.find_element_by_class_name(
            "btn btn-primary btn-block glyphicon glyphicon-shopping-cart js-enable-btn").click()
        self.wd.find_element_by_class_name("btn btn-primary btn-block add-to-cart-button").click()


    def verify_id_basket(self, id):
        self.wd = self.app.wd
        id = self.wd.find_element_by_class_name(f"cart__{id}")
        if len(id) == 8:
            return id
        else:
            print("Invalid ID length")
