from abc import ABCMeta, abstractmethod
from model.abilityfactory import AbilityFactory

class GameObject(metaclass=ABCMeta):
    default_abilities = {}
    """represents a game object which is written to disk by the storage class"""
    def __init__(self, classname, abilities = {}, *args, **kwargs):
        self._classname = classname
        self._abilities = {}
        initial_abilities = self.initial_abilities()[:]
        for ability in initial_abilities:
            key = ability.ability_name()
            if key in abilities:
                ability_properties = abilities[key]
                ability.update(**ability_properties)
            self._abilities[key] = ability
        self._dirty = False

    @property
    def classname(self):
        return self._classname

    @property
    def abilities(self):
        return self._abilities

    def ability(self, ability_name):
        return self._abilities[ability_name]

    def has_ability(self, ability_name):
        return ability_name in self._abilities

    def self.dirty():
        self._dirty = True

    @abstractmethod
    def initial_abilities(self):
        """returns a list of ability objects"""
        return []

    @abstractmethod
    def storage_location(self):
        pass

    @abstractmethod
    def symlinks(self):
        """multiple calls to the symlinks() method of the same GameObject must
        return the same amount of symlinks in the same order. This is so old symlinks
        can properly be replaced by new ones.""" 
        pass
