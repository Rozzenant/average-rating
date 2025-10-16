"""
Тест для BaseReport.

Проверяет, что:
- Невозможно создать экземпляр абстрактного класса BaseReport.
- Потомки BaseReport (например AverageRatingReport) создаются нормально.

Примечание: этот тест необязателен.
"""

import pytest
from reports.base import BaseReport
from reports.avg_rating import AverageRatingReport


def test_base_report_instantiation():
    # Проверяем, что BaseReport нельзя инстанцировать напрямую
    with pytest.raises(TypeError):
        BaseReport()

    # А потомок работает нормально
    report = AverageRatingReport()
    assert report is not None
