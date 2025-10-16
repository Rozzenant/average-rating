from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data):
        """Базовый интерфейс для всех отчётов.
        Классы-наследники должны реализовать метод generate(data).
        Необходим для расширения под другие задачи."""
        pass
