
def add_to_basket(app):
    app.open_basket_page()


def verify_id_basket(app):
    app.basket.add_to_basket()
    app.basket.verify_id_basket()
    assert len(app.basket.verify_id_basket(id)) == 8

def help_popup(app):
    assert app.basket.help_popup()
