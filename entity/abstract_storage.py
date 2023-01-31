from abc import ABC, abstractmethod


class AbstractStorage(ABC):  # склад

    @abstractmethod
    def add(self, title: str, quantity: int) -> None:  # ДОБАВИТЬ- увеличивает запас items(товаров)
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:  # УДАЛИТЬ - уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self) -> int:  # вернуть количество свободных мест
        pass

    # мёртвый код удалён

    @abstractmethod
    def get_unique_items_count(self):  # возвращает количество уникальных товаров.
        pass