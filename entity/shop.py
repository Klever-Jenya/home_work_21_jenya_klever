from entity.base_storage import BaseStorage
from exceptions import TooManyDifferentProducts


class Shop(BaseStorage):

    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int) -> None:
        # TODO: Проверить, что в магазине храниться не более 5 уникальных товаров
        if self.get_unique_items_count() > 5:
            raise TooManyDifferentProducts

        super().add(title, quantity)
