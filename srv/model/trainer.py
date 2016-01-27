from abc import ABCMeta, abstractmethod
from model.unitfactory import UnitFactory
from model.util import filterobject

class TrainingError(Exception):
    def __init__(self, message):
        super(TrainingError, self).__init__(message)

class Trainer(metaclass=ABCMeta):
    def __init__(self, training_progress=0, training_queue=[], *args, **kwargs):
        super(Trainer, self).__init__(*args, **kwargs)
        self._training_progress = training_progress
        self._training_queue = training_queue

    @property
    def training_progress(self):
        return self._training_progress

    @property
    def training_queue(self):
        return self._training_queue

    @abstractmethod
    def trainable_units(self):
        """returns a dictionary. In the form of
        {
            'unit_type': {
                'trainspeed': amount_of_ticks_until_created,
                'resource_cost': {
                    'gold': amount_of_gold_cost,
                    'wood': amount_of_wood_cost,
                    'stone': amount_of_stone_cost
                }
            }
            'unit_type2': ...
        }
        """
        pass

    def add_to_training_queue(self, unit_type):
        if not unit_type in self.trainable_units():
            raise TrainingError("cannot train unit {0}".format(unit_type))

        self._training_queue.append(unit_type)

    def train(self):
        """should be called every tick, returns a Unit everytime
        a new unit has been trained, else None is returned."""
        if hasattr(self, 'usable') and not self.usable:
            return None

        if len(self._training_queue) == 0:
            # nothing to do
            return None

        trained_unit = self._training_queue[0]
        trained_unit_info = self.trainable_units()[trained_unit]
        self._training_progress += 1
        if self._training_progress >= trained_unit_info['trainspeed']:
            # unit finished
            self._training_queue = self._training_queue[1:]
            return UnitFactory(trained_unit, **filterobject(self, ['position', 'owner']))

        # nothing trained this tick
        return None

