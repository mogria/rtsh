from faker import Faker
from abc import ABCMeta, abstractmethod
from model.dirty import dirty

class Nameable(metaclass=ABCMeta):
    _fake = Faker()
    def __init__(self, name = None, *args, **kwargs):
        super(Nameable, self).__init__(*args, **kwargs)
        self._name = name

    @property
    def name(self):
        if self._name == None: # no name yet?
            dirty(self)
            self._name = self.give_name() # then give it a name!
        return self._name

    @abstractmethod
    def give_name(self):
        return "unnamed entity"
