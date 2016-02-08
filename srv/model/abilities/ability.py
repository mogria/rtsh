from abc import ABCMeta, abstractmethod

class Ability(metaclass=ABCMeta):
    @abstractmethod
    def get_property_names(self):
        getproperties(self)

    def get_properties(self):
        filterproperties(self, self.get_property_names())

    @abstractmethod
    def activate():
        """gets executed when the ability gets activated. This may happen
        because of a command."""
        pass

    @abstractmethod
    def tick():
        """gets executed each tick, even when the Ability hasn't activated yet"""
        pass
