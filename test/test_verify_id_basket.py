def test_verify_id_basket(app):  # Тест работает.
    expected = 8
    app.basket.add_to_basket()
    actual = app.basket.verify_id_basket()
    assert actual == expected
