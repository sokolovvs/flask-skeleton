from src.exceptions.domain_exceptions.security.base_security_exception import BaseSecurityException


class AccessDeniedException(BaseSecurityException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
