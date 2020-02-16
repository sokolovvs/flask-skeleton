from src.entities.post import Post
from src.repositories.abstract_repository import AbstractRepository


class PostRepository(AbstractRepository):

    def __init__(self, model: Post) -> None:
        super().__init__(model)
