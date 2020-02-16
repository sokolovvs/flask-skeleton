from src.exceptions.domain_exceptions.entity.base_entity_exception import BaseEntityException


class EntityNotFoundException(BaseEntityException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
