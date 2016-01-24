from model.gameobject import GameObject
from model.positionable import Positionable
from model.ownable import Ownable

class Resources(GameObject, Positionable, Ownable):
    def __init__(self, gold = 0, wood = 0, stone = 0, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self._gold = gold
        self._wood = 0
        self._stone = 0

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, new_gold):
        self._gold = new_gold

    @property
    def stone(self):
        return self._stone

    @stone.setter
    def stone(self, new_stone):
        self._stone = new_stone

    @property
    def stone(self):
        return self._stone

    @stone.setter
    def stone(self, new_gold):
        self._stone = new_gold

    def storage_location():
        base_location = Positionable.storage_location(self) if self.is_neutral() else Ownable.storage_location(self)
        return "{0}/resources.json".format(base_location)

    def symlinks():
        # no symlinks needed for this
        return []
