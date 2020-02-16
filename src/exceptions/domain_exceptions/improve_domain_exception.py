from src.exceptions.improve_exception import ImproveException


class DomainException(ImproveException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
