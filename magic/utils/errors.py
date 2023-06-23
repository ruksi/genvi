from __future__ import annotations

import string


class ValidationError(Exception):
    # problems that user could fix by changing configuration
    pass


class EmptyError(ValidationError):
    def __init__(self, thing: str) -> None:
        super().__init__(f"{thing} cannot be empty")


class NotLowAsciiError(ValidationError):
    def __init__(self, thing: str, value: str) -> None:
        valid = string.ascii_lowercase
        super().__init__(f"{thing} '{value}' must consist of lowercase ASCII ({valid})")


class NotAllowedError(ValidationError):
    def __init__(self, thing: str, value: str) -> None:
        super().__init__(f"{thing} '{value}' is not allowed")


class InternalError(Exception):
    # problems that user _can not_ fix by changing configuration
    pass


class NoProjectRootError(InternalError):
    def __init__(self) -> None:
        super().__init__("package root must be an existing directory")


class BadProjectRootError(InternalError):
    def __init__(self) -> None:
        super().__init__("package root does not look like `genvi` root")
