from abc import ABC, abstractmethod


class BaseReport(ABC):
    """
    BaseReport — абстрактный класс для всех отчетов.

    Примечание по покрытию тестами (coverage):

    - Метод `generate` помечен как @abstractmethod и не может быть вызван напрямую.
    - Любой потомок BaseReport обязан переопределить этот метод.
    - В coverage этот метод считается непокрытым, даже если мы тестируем потомков.
    """
    @abstractmethod
    def generate(self, data):
        """Базовый интерфейс для всех отчётов.
        Классы-наследники должны реализовать метод generate(data).
        Необходим для расширения под другие задачи.
        """
        pass
