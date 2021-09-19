def test_verify_new_cart(app):  # Тест не работает.
    expected_basket_url = "https://apparel-uk.local:9002/ucstorefront/en/login"
    actual_basket_url = app.basket.verify_new_cart()
    assert actual_basket_url == expected_basket_url
