import logging

from myproject.animals.animal import Animal

log = logging.getLogger(__name__)


class CommonViper(Animal):
    """
    The common European viper is a venomous snake that is extremely widespread.

    It can be found throughout most Central and Eastern Europe and as far
    as East Asia.
    """

    scientific_name = "Vipera berus"

    def vocalize(self) -> str:
        return "*hiss*"
