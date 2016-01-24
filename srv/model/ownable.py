class Ownable(object):
    def __init__(self, owner = "none", *args, **kwargs):
        super(Ownable, self).__init__(*args, **kwargs)
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    def is_neutral(self):
        return self._owner == "none"

    def same_owner(self, ownable):
        return self._owner == ownable.owner

    def storage_location(self):
        return "/home/{0}".format(self._owner)
