def test_check_basket(app):  # Тест работает.
    expected = 1
    app.basket.add_to_basket()
    actual = app.basket.check_basket()
    assert actual == expected
