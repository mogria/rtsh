from model.attacker import Attacker
from model.dirty import dirty

class Destroyable(object):
    armor_types = {
        'heavy': 0,
        'medium': 1,
        'light': 2,
        'normal': 3
    }

    def __init__(self, health = 1, armor_type = "normal", *args, **kwargs):
        super(Destroyable, self).__init__(*args, **kwargs)
        self._health = health
        if not armor_type in Destroyable.armor_types:
            raise ValueError("invalid armortype '{0}'".format(armor_type))
        self._armor_type = armor_type

    @property
    def health(self):
        return self._health

    @property
    def armor_type(self):
        return self._armor_type

    def is_destroyed(self):
        return self._health <= 0

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
