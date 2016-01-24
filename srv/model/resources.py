from model.gameobject import GameObject

class Resources(GameObject):
    def __init__(self, gold = 0, wood = 0, stone = 0):
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
