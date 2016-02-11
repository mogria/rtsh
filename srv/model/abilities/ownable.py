from model.abilities.ability import Ability

class Ownable(Ability):
    def __init__(self, owner = "none", *args, **kwargs):
        super(Ownable, self).__init__(*args, **kwargs)
        self._owner = owner

    def ability_name(self):
        return "ownable"

    def update(self, owner=None, *args, **kwargs):
        self._owner = owner

    def activate(self):
        pass

    def tick(self):
        pass

    @property
    def owner(self):
        return self._owner

    def is_neutral(self):
        return self._owner == "none"

    def same_owner(self, ownable):
        return self._owner == ownable.owner

    def base_storage_location(self):
        return "/home/{0}".format(self._owner)
