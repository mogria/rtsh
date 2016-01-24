from abc import ABCMeta, abstractmethod


class GameObject(metaclass=ABCMeta):
    """represents a game object which is written to disk by the storage class"""
    def __init__(self, classname, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self._classname = classname

    @property
    def classname(self):
        return self._classname

    @abstractmethod
    def storage_location(self):
        pass

    @abstractmethod
    def symlinks(self):
        """multiple calls to the symlinks() method of the same GameObject must
        return the same amount of symlinks in the same order. This is so old symlinks
        can properly be replaced by new ones.""" 
        pass
