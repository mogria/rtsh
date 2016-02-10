import random
from model.abilities.ability import Ability
from model.dirty import dirty

class Attacker(Ability):
    attack_types = {
        'pierce': 0,
        'blunt': 1,
        'sharp': 2,
        'normal': 3
    }

    def __init__(self, damage = 0, attack_type = "normal", attack_speed = 1, attack_range = 0):
        if not attack_type in Attacker.attack_types:
            raise ValueError("invalid attack type '{0}'".format(attack_type))
        self._attack_type = attack_type
        self._attack_speed = attack_speed
        self._attack_range = attack_range
        self._damage = damage
        self._attack_cycle = -1

    @property
    def attack_type(self):
        return self._attack_type

    @property
    def attack_speed(self):
        return self._attack_speed

    @property
    def attack_range(self):
        return self._attack_range

    @property
    def damage(self):
        return self._damage

    @property
    def attack_cycle(self):
        return self._attack_cycle

    def update(self, attack_cycle = -1, *args, **kwargs):
        self._attack_cycle = attack_cycle

    def activate(self):
        # TODO: save attack target
        pass

    def tick(self):
        # TODO: grab attack target and call attack() method
        pass

    def reset_attack_cycle(self):
        self._attack_cycle = self._attack_speed

    def attack(self, attacked_destroyable):
        self._attack_cycle -= 1
        if self._attack_cycle <= 0:
            dirty(self)
            attack_damage = self.randomized_damage()
            attacked_destroyable.get_attacked(attack_damage, self.attack_type)
            # only reset attack cycle after we've actually attacked
            self.reset_attack_cycle()
        else:
            self._attack_cycle -= 1

    def randomized_damage(self):
        return round(self.damage * random.uniform(0.9, 1.1))
