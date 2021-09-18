

def test_basket_items(app):
    app.basket.add_to_basket()
    app.basket.check_basket_items()