
class Builder(object):
    def __init__(self, build_speed = 0, capacity = 0, *args, **kwargs):
        super(Builder, self).__init__(*args, **kwargs)
        self._build_speed = build_speed
        self._capacity = capacity

    @property
    def build_speed(self):
        return self._build_speed

    @property
    def capacity(self):
        return self._capacity

    def harvest(self, resources):
        pass

    def build(self, building):
        """should be called every tick this builder is reparing or creating a building.
        Returns true when finished. False if more work can be done."""
        max_health = building.max_health()
        if building._health < max_health:
            building._health += self._build_speed
            if building._health >= max_health:
                building._health = max_health

            if building.health == max_health:
                building._usable = True
                return True
            else:
                return False

        else:
            return True

