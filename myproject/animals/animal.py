import abc
import logging

log = logging.getLogger(__name__)


class Animal(abc.ABC):
    """
    Animals are multicellular, eukaryotic organisms in the biological kingdom Animalia.

    With few exceptions, animals make sounds, eat and live in different habitats.
    """

    name: str
    scientific_name: str = "Animalia"

    def __init__(self, name: str) -> None:
        log.debug("create")
        self.name: str = name

    @abc.abstractmethod
    def vocalize(self) -> str:
        raise NotImplementedError()
