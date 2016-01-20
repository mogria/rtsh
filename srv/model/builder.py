
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
