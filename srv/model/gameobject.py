from abc import ABCMeta, abstractmethod


class GameObject(metaclass=ABCMeta):
    def __init__(self, classname, *args, **kwargs):
        super(GameObject, self).__init__(*args, **kwargs)
        self._classname = classname

    @property
    def classname(self):
        return self._classname

    @abstractmethod
    def storage_location(self):
        pass
