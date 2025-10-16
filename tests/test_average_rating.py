from reports.avg_rating import AverageRatingReport


# Тест 1: базовый сценарий
def test_average_rating_basic():
    data = [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {
            "name": "galaxy s23 ultra",
            "brand": "samsung",
            "price": "1199",
            "rating": "4.8",
        },
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
        {"name": "iphone 14", "brand": "apple", "price": "899", "rating": "4.7"},
    ]

    report = AverageRatingReport()
    table = report.generate(data)
    brands = [brand for brand, _ in table]

    # Проверяем, что все бренды присутствуют
    assert "apple" in brands
    assert "samsung" in brands
    assert "xiaomi" in brands

    # Проверяем средний рейтинг брендов
    ratings_dict = dict(table)

    assert ratings_dict["apple"] == 4.8  # (4.9 + 4.7)/2 = 4.8
    assert ratings_dict["xiaomi"] == 4.6
    assert ratings_dict["samsung"] == 4.8


# Тест 2: пустой список
def test_average_rating_empty():
    data = []
    report = AverageRatingReport()
    table = report.generate(data)
    # Должно быть пустым
    assert not table


# Тест 3: один бренд
def test_average_rating_one_brand():
    data = [
        {"name": "item1", "brand": "testbrand", "price": "100", "rating": "4.5"},
        {"name": "item2", "brand": "testbrand", "price": "200", "rating": "5.0"},
    ]
    report = AverageRatingReport()
    table = report.generate(data)
    brands = [brand for brand, _ in table]
    assert "testbrand" in brands
    ratings_dict = dict(table)
    assert ratings_dict["testbrand"] == 4.75  # среднее (4.5+5.0)/2


# Тест 4: несколько брендов одинаковый рейтинг
def test_average_rating_equal_scores():
    data = [
        {"name": "item1", "brand": "brand1", "price": "100", "rating": "4.5"},
        {"name": "item2", "brand": "brand2", "price": "200", "rating": "4.5"},
    ]
    report = AverageRatingReport()
    table = report.generate(data)
    brands = [brand for brand, _ in table]
    # Оба бренда должны присутствовать
    assert "brand1" in brands
    assert "brand2" in brands
    ratings_dict = dict(table)
    assert ratings_dict["brand1"] == 4.5
    assert ratings_dict["brand2"] == 4.5
