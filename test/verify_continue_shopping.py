def test_verify_continue_shopping(app):  # Тест работает.
    exp_url = "https://apparel-uk.local:9002/ucstorefront/en/Brands/c/brands"
    actual_url = app.basket.verify_continue_shopping()
    assert exp_url == actual_url
