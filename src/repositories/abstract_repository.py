import abc
from typing import List, Union
from src.app import App
from src.entities.base_model import BaseModel
from src.exceptions.domain_exceptions.entity.entity_not_found_exception import EntityNotFoundException


class AbstractRepository:

    __metaclass__ = abc.ABCMeta

    def __init__(self, model: BaseModel) -> None:
        self._model = model
        self._class_of_model = self._model.__class__

    def find(self, id) -> BaseModel:
        return App.get_db().session.query(self._class_of_model).get(id)

    def find_all(self) -> List[BaseModel]:
        return App.get_db().session.query(self._class_of_model).all()

    def get(self, id: Union[int, str, None]):
        entity = self.find(id)

        if isinstance(entity, BaseModel):
            return entity

        raise EntityNotFoundException('Entity not found')

    def persist(self, entity: BaseModel) -> BaseModel:
        return App.get_db().session.add(entity)

    def remove(self, entity: BaseModel) -> None:
        App.get_db().session.delete(entity)
