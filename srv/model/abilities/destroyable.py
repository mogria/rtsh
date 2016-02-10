from model.abilities.ability import Ability
from model.abilities.attacker import Attacker
from model.dirty import dirty

class Destroyable(Ability):
    armor_types = {
        'heavy': 0,
        'medium': 1,
        'light': 2,
        'normal': 3
    }

    def __init__(self, armor_type="normal", health=1):
        if not armor_type in Destroyable.armor_types:
            raise ValueError("invalid armortype '{0}'".format(armor_type))
        self._armor_type = armor_type
        self._health = health

    def ability_name(self):
        return "destroyable"

    @property
    def health(self):
        return self._health

    @property
    def armor_type(self):
        return self._armor_type

    def update(self, health=1, *args, **kwargs):
        self._health = health

    def is_destroyed(self):
        return self._health <= 0

    def activate(self):
        pass

    def tick(self):
        pass

    def get_attacked(self, damage, attack_type):
        dirty(self)
        bonusmap = [
            [2.0, 0.5, 1.0, 1.0],
            [1.0, 2.0, 0.5, 1.0],
            [0.5, 1.0, 2.0, 1.0],
            [1.0, 1.0, 1.0, 1.0]
        ]
        armor_idx = Destroyable.armor_types[self.armor_type]
        attack_idx = Attacker.attack_types[attack_type]
        bonus = bonusmap[armor_idx][attack_idx]

        self._health -= damage * bonus
