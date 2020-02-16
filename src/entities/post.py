from datetime import datetime
from typing import Union

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData
from sqlalchemy.orm import mapper
from src.entities.base_model import BaseModel


class Post(BaseModel):

    __tablename__ = 'posts'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    content = Column(Text(), nullable=False)
    created_on = Column(DateTime(), default=datetime.utcnow)
    updated_on = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_id(self) -> Union[int, str, None]:
        return self.id

    def get_name(self) -> Union[str, None]:
        return self.name

    def update_name(self, value: Union[str, None]) -> 'Post':
        self.name = value

        return self

    def get_content(self) -> Union[str, None]:
        return self.content

    def update_content(self, value: Union[str, None]) -> 'Post':
        self.content = value

        return self

    def get_created_on(self):
        return self.created_on

    def get_updated_on(self):
        return self.updated_on

    def to_dict(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'content': self.get_content(),
            'created_on': self.get_created_on(),
            'updated_on': self.get_updated_on()
        }

