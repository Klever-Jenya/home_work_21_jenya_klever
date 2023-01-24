from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    # request - строка от пользователя, "хранилища" в виде словаря # storages - хранилища
    # storages = {
    #     "магазин": shop,
    #     "склад": store,
    #     }    нужно для того, чтобы проверить что такой склад существует и сохранить этот склад себе
    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        # TODO: Разделить строку по пробелам (самая простая валидация)
        splitted_request = request.lower().split(" ")
        if len(splitted_request) != 7:
            raise InvalidRequest

        # TODO: Внести значения из строки в атрибуты класса
        self.quantity = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]

        # TODO: Провалидировать пункты отправки и назначения
        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName





        # И возвращает объект класса Request
        # return from = "склад",
        #     to =  "магазин",
        #     amount = 3,
        #     product = "печеньки"