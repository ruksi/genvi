import logging

from myproject.animals.animal import Animal

log = logging.getLogger(__name__)


class BlueWhale(Animal):
    """The blue whale is a marine mammal and a baleen whale."""

    scientific_name = 'Balaenoptera musculus'

    def vocalize(self) -> str:
        return '*WEEEAAAAAOOOUUU*'
