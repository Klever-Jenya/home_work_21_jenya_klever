from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import RequestError, CourierError

store = Store(items={})
shop = Shop(items={})

store.items = {
    "печенька": 25,
    "собачка": 25,
    "елка": 25,
    "пончик": 3,
    "зонт": 5,
    "ноутбук": 1,
}
shop.items = {
    "печенька": 2,
    "собачка": 2,
    "елка": 2,
    "зонт": 1,
    "пончик": 1,
}

store_2 = Store(items={"печенька": 13})
store_3 = Store(items={"пенал": 34})


# storages - хранилища
# маппинг русского названия
# для будущего масштабирования

storages = {
    "магазин": shop,
    "склад": store,
    "магазин_2": store_2,
    "магазин_3": store_3,
}


def main():
    print("\nДобрый день!\n")

    while True:
        # TODO: Вывести содержимое складов
        for storage_title in storages:
            print(f"Сейчас в {storage_title}:\n {storages[storage_title].items}")  # items == get.__items в прошлом

        # TODO Запросить ввод от пользователя
        user_input = input(
            "Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n"
            "Введите 'стоп' или 'stop', если хотите закончить:\n"
        )
        if user_input in ("stop", "стоп"):
            break

        # TODO: Распарсить и провалидировать ввод пользоввателя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.massage)
            continue  # переносит в начало цикла. Кривой запрос мы не выполняем

        # TODO: Запустить доставку
        courier = Courier(
            request=request,
            storages=storages,
        )

        try:
            courier.move()
        except CourierError as error:  # ловим всех наследников CourierError
            print(error.massage)
            courier.cancel()


if __name__ == "__main__":
    main()
