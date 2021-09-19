def test_verify_new_cart(app):  # Тест не работает.
    app.basket.add_to_basket()
    app.basket.verify_new_cart()
