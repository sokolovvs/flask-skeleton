import abc
from pprint import pprint

from src.helpers.dto.abstract_entity_dto import AbstractEntityDTO
from src.repositories.abstract_repository import AbstractRepository


class AbstractService:

    __metaclass__ = abc.ABCMeta

    def __init__(self, repository: AbstractRepository) -> None:
        self._repository = repository

    def get(self, dto: AbstractEntityDTO):
        return self._repository.get(dto.get_id())

    def get_all(self):
        return self._repository.find_all()

    def create(self, dto):
        pass

    def update(self, dto):
        pass

    def delete(self, dto):
        pass
