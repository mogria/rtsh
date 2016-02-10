from model.abilities.ability import Ability


class Builder(Ability):
    def __init__(self, build_speed=0, capacity=0):
        self._build_speed = build_speed
        self._capacity = capacity
        self._build_target = None

    def ability_name(self):
        return "builder"

    @property
    def build_speed(self):
        return self._build_speed

    @property
    def capacity(self):
        return self._capacity

    @property
    def build_target(self):
        return self._build_target

    @build_target.setter
    def build_target(self, build_target):
        self._build_target = build_target

    def update(self, build_target=None, *args, **kwargs):
        self._build_target = build_target

    def harvest(self, resources):
        pass

    def activate(self):
        # TODO: should set build target 
        pass


    def tick(self):
        """should be called every tick this builder is repairing or creating a building.
        Returns true when finished. False if more work can be done."""
        if self.build_target is None:
            return False

        if self.build_target.position != self.position:
            self._build_target = None
            self.dirty()
            return False

        max_health = self.build_target.max_health()
        if self.build_target.health < max_health:
            self.dirty()
            self.build_target._health += self._build_speed
            if self.build_target.health >= max_health:
                self.build_target._health = max_health

            return self.build_target.usable

        else:
            return True
