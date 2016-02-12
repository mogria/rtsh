from faker import Faker
from abc import ABCMeta, abstractmethod

class Nameable(metaclass=ABCMeta):
    _fake = Faker()
    def __init__(self, name = None, give_name_func=None, *args, **kwargs):
        super(Nameable, self).__init__(*args, **kwargs)
        self._name = name
        self._give_name_func = None 
        if hasattr(give_name_func, '__call__'):
            self._give_name_func = give_name_func
        else:
            self._give_name_func = lambda f: "unnamed entity"

    def ability_name(self):
        return "nameable"

    @property
    def name(self):
        if self._name == None: # no name yet?
            self._name = self._give_name_func(Nameable._fake) # then give it a name!
        return self._name

