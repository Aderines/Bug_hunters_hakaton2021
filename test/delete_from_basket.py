def test_delete_from_basket(app):  # Тест не работает.
    expected_result = "Product has been removed from your bag."
    app.basket.add_to_basket()
    actual_result = app.basket.delete_basket()
    assert int(expected_result == actual_result)
