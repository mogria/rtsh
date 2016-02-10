from abc import ABCMeta, abstractmethod

class Ability(metaclass=ABCMeta):
    @abstractmethod
    def ability_name(self):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def activate(self):
        """gets executed when the ability gets activated. This may happen
        because of a command."""
        pass

    @abstractmethod
    def tick(self):
        """gets executed each tick, even when the Ability hasn't activated yet"""
        pass
