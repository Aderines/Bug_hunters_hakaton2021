# tests check filters on Category page
import time


def test_filter_check(app):
    """
    1. open Category page
    2. check all expected Filters are available
    2. check each filter has expected options
    """
    # в скобках видимо количество продуктов, надо было бы удалить из проверки
    expected_filters_options = {
        'Shop by Stores': ['SEARCH', 'or', 'FIND STORES'],
        'Shop by Price': ['£0-£19.99  (89)', '£20-£49.99  (571)', '£50-£99.99  (294)',
                          '£100-£199.99  (117)', '£200-£299.99  (6)', '£300-£399.99  (2)',
                          '£400-£499.99  (11)', '£500-£599.99  (2)', '£600-£699.99  (1)',
                          '£700-£799.99  (1)'],
        'Shop by Colour': ['BLACK  (252)', 'WHITE  (198)', 'BLUE  (197)', 'GREEN  (102)',
                           'GREY  (89)', 'RED  (81)', 'YELLOW  (52)', 'PURPLE  (48)',
                           'ORANGE  (45)','BROWN  (39)','PINK  (27)'],
        'Shop by Size': ['5.0  (5)', '5.0 US  (2)', '6.0  (7)', '6.0 US  (2)', '6.3  (3)',
                         '7.0  (7)', '7.0 US  (3)', '7.5 US  (2)', '8.0  (7)', '8.0 US  (3)',
                         '8.5 US  (4)', '9.0  (5)', '9.0 US  (4)', '9.5 US  (4)', '10.0  (4)',
                         '10.0 US  (3)', '10.5 US  (3)', '11.0 US  (3)', '11.5 US  (3)',
                         '12.0 US  (3)', '13.0 US  (2)', '14.0 US  (1)', '15.0 US  (1)',
                         '36  (1)', '37  (1)', '38.0  (2)', '41.0  (2)', '42.0  (2)',
                         '151.5  (1)', '153.0  (2)', '154.0  (1)', '154.5  (1)', '156.0  (1)',
                         '157.0  (1)', '158.0  (2)', '164.0  (1)', '168.0  (1)', 'XXS  (14)',
                         'XS  (94)', 'S  (192)', 'M  (214)', 'L  (200)', 'LXL  (5)',
                         'XL  (155)', 'XXL  (28)', 'UNI  (22)', 'SM  (5)', 'XXXL  (3)',
                         'XXXS  (2)', 'XXXXS  (2)'],
        'Shop by gender': ['Male (696)', 'Female (398)'],
        'Shop by Collection': ['Streetwear (523)', 'Surf (419)', 'Snow (394)',
                               'T-Shirts (350)', 'Kids (216)', 'T-Shirts men (184)',
                               'T-Shirts youth (101)', 'Shoes (96)', 'T-Shirts women (65)',
                               'Sandals women (48)', 'Sandals (48)', 'Shirts (35)',
                               'Ski Gear (18)', 'Sunglasses (15)', 'Shades (14)',
                               'Boards (6)', 'Shortboards + Fish (4)', 'Backpacks (3)',
                               'Caps (2)', 'Goggles (2)', 'Tools (2)', 'Long + Funboards (1)',
                               'Skimboard (1)', 'Guides (1)', 'Helmets (1)'],
        'Shop by Category': ['Clothes (499)', 'T-Shirts (350)', 'Streetwear men (268)',
                             'T-Shirts men (184)', 'Snowwear women (157)', 'Streetwear youth (140)',
                             'Snowwear men (107)', 'T-Shirts youth (101)', 'Snow Jackets women (99)',
                             'Streetwear women (98)', 'Shoes (96)', 'T-Shirts women (65)',
                             'Snowwear youth (61)', 'Snow Pants (60)', 'Snow Pants women (58)',
                             'Shorts (57)', 'Shoes women (48)', 'Sandals women (48)', 'Sandals (48)',
                             'Snow Jackets (47)', 'Shoes (47)', 'Boardshorts youth (39)',
                             'Snow Pants youth (37)', 'Protection (36)', 'Shirts (35)', 'Helmets (34)',
                             'Skirts and Dresses women (28)', 'Accessories (27)', 'Belts (27)',
                             'Others (26)', 'Snow Jackets youth (24)', 'Tuning (19)', 'Tools (19)',
                             'Helmets Snow (19)', 'Ski Gear (18)', 'Bags+Boardbags (17)', 'Bindings (16)',
                             'Soft Bindings (16)', 'Helmets youth (15)', 'Sunglasses (15)', 'Eyewear (14)',
                             'Shades (14)', 'Snowboards (11)', 'Freestyle+Freeride (11)', 'Bags women (7)',
                             'Accessories women (7)', 'Backpacks (6)', 'Surf (6)', 'Bags (4)'],
        'Shop by Brand': ['Burton (240)', 'Billabong (209)', 'Volcom (144)', 'Vans (60)', 'DC (56)',
                          'Quiksilver (40)', 'Red (36)', 'Playboard (32)', 'Special Blend (25)',
                          'Element (23)', 'Roxy (23)', 'Foursquare (20)', 'Nike 6.0 (18)', 'Toko (16)',
                          'Alien Workshop (11)', 'Orage (10)', 'PYUA (10)', 'WLD (10)', 'Zimtstern (10)',
                          'Armada (9)', 'Carhartt (8)', 'Analog (6)', 'Hurley (6)', 'Reef (5)', '667 (4)',
                          'Blue Tomato (4)', 'Dakine (4)', 'Horsefeathers (4)', 'Nike (4)',
                          'Von Zipper (4)', 'adidas Originals (4)', '686 (3)', 'Al Merrick (3)',
                          'Anon (3)', 'Dainese (3)', 'F2-FTWO (3)', 'Fox (3)', '69 Slam (2)',
                          'Femipleasure (2)', 'Pro Tec (2)', 'Sessions (2)', 'Skullcandy (2)',
                          'Aesthetiker (1)', 'Nikita (1)', 'Periplus AC+Ion Guides (1)', 'Ride (1)',
                          'Rip Curl (1)', 'Skim One (1)', 'Southpoint (1)'],
    }
    expected_filters = list(expected_filters_options.keys())

    app.categories.open_category_page()
    actual_filters = app.categories.collect_filters()

    # it could be check each filter one by one
    assert expected_filters == actual_filters

    # check option for each filter
    for filter in expected_filters:

        actual_options = app.categories.collect_options(filter)
        expected_options = expected_filters_options[filter]
        assert actual_options == expected_options
