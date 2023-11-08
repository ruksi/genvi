from __future__ import annotations

import logging

from myproject.animals.animal import Animal

log = logging.getLogger(__name__)


class Human(Animal):
    """
    Humans are the most widespread species of primate.

    They are mainly characterized by bipedalism and large heads.
    """

    scientific_name = "Homo sapiens"

    def vocalize(self) -> str:
        return f"{self.scientific_name}: *grunt*"
