from faker import Faker
from abc import ABCMeta, abstractmethod

class Nameable(metaclass=ABCMeta):
    _fake = Faker()
    def __init__(self, name = None, *args, **kwargs):
        self._name = self.give_name() if name == None else name
        super(Nameable, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return self._name

    @abstractmethod
    def give_name(self):
        pass
