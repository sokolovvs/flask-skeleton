from src.repositories.post_repository import PostRepository
from src.services.crud.abstract_service import AbstractService


class PostService(AbstractService):

    def __init__(self, repository: PostRepository) -> None:
        super().__init__(repository)
