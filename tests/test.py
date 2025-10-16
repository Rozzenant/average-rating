from reports.average_rating import AverageRatingReport


def test_average_rating_report():
    data = [
        {"brand": "apple", "rating": "4.9"},
        {"brand": "apple", "rating": "4.7"},
        {"brand": "samsung", "rating": "4.8"},
    ]
    report = AverageRatingReport()
    result = report.generate(data)
    assert result[0][0] == "apple"
    assert result[0][1] == 4.8
