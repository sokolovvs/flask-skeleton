import abc
from pprint import pprint

from flask import jsonify

from src.controllers.base_controller import BaseController


class AbstractApiController(BaseController):
    __metaclass__ = abc.ABCMeta

    def create(self):
        pass

    def create_many(self):
        pass

    def update(self):
        pass

    def update_many(self):
        pass

    def delete(self):
        pass

    def delete_many(self):
        pass

    def get_all(self):
        posts = self._service.get_all()
        response = self._entities_adapter.to_response_data_from_entities(posts)

        return jsonify(response), 200

    def get(self, request):
        entity = self._service.get(self._entity_adapter.to_dto_from_request(request))
        response = self._entity_adapter.to_response_data_from_entity(entity)

        return jsonify(response), 200
