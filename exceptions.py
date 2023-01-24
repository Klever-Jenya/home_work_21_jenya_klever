class BaseError(Exception):
    massage = "Неожиданная ошибка"  # или None, ""


# не используется, но что бы было от кого наследоваться


class CourierError(BaseError):
    massage = "Произошла ошибка при доставке"


class RequestError(BaseError):
    massage = "Произошла ошибка обработки запроса"


# --------ошибки доставки-------
class NotEnoughSpace(CourierError):
    massage = "Недостаточно места на складе"


class NotEnoughProduct(CourierError):
    massage = "Недостаточно товара на складе"


class TooManyDifferentProducts(CourierError):
    massage = "Слишком много товара в магазине"


# ------------ошибки запроса------------
class InvalidStorageName(RequestError):
    massage = "Выбран не существующий склад"


class InvalidRequest(RequestError):
    massage = "Неправильный запрос. Попробуйте снова"
