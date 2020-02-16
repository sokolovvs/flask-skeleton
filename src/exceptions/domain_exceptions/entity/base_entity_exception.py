from src.exceptions.domain_exceptions.improve_domain_exception import DomainException


class BaseEntityException(DomainException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
