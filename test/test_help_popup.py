

def add_to_basket(app):
    app.basket.add_to_basket()
    assert app.basket.help_popup()


