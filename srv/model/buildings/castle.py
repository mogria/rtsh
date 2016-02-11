from model.buildings.building import Building
from model.abilities.trainer import Trainer


class Castle(Building):
    def __init__(self, *args, **kwargs):
        super(Castle, self).__init__(*args, **kwargs)

    def give_name(self):
        return "{0}'s Castle".format(self.owner)

    def initial_abilities(self):
        units = {
            'slave': {
                'trainspeed': 20,
                'resources': {
                   'gold': 50,
                    'wood': 0,
                    'stone': 0
                }
            }
        }
        return super(Castle, self).initial_abilities() + [
                Trainer(trainable_units=units)
              ]

    def max_health(self):
        return 100

    def trainable_units(self):
        return {
        }
