from abc import ABCMeta, abstractmethod

class GameObject(object):
    def __init__(self, classname):
        self._classname = classname

    @property
    def classname(self):
        return self._classname

    @abstractmethod
    def storage_location(self):
        pass
