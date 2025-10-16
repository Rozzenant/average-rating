from reports.base import BaseReport
from collections import defaultdict


class AverageRatingReport(BaseReport):
    """Реализация BaseReport под средние оценки"""

    def generate(self, data):
        brand_ratings = defaultdict(list)
        for row in data:
            brand = row["brand"]
            rating = float(row["rating"])
            brand_ratings[brand].append(rating)

        result = []
        for brand, ratings in brand_ratings.items():
            avg = sum(ratings) / len(ratings)
            result.append((brand, round(avg, 2)))

        result.sort(key=lambda x: x[1], reverse=True)
        return result
