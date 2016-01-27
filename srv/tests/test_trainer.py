import unittest
from model.trainer import TrainingError
from model.castlebuilding import CastleBuilding

class TrainerTest(unittest.TestCase):
    def setUp(self):
        self.castle = CastleBuilding(position=(0, 0), owner="dude3", usable=True, training_queue=[])

    def tearDown(self):
        del self.castle

    def test_add_to_training_queue(self):
        self.assertEquals([], self.castle.training_queue)
        self.castle.add_to_training_queue('slave')
        self.assertEquals(['slave'], self.castle.training_queue)
        self.castle.add_to_training_queue('slave')
        self.assertEquals(['slave', 'slave'], self.castle.training_queue)

    def test_add_to_training_queue_invalid_unit(self):
        self.assertRaises(TrainingError, self.castle.add_to_training_queue, 'unit-which-cant-be-trained')

    def test_train_unusable(self):
        self.castle._usable = False
        self.castle.add_to_training_queue('slave')
        previous_progress = self.castle.training_progress
        for x in range(27):
            self.assertEquals(None, self.castle.train())
        self.assertEquals(previous_progress, self.castle.training_progress)

    def test_train_no_queue(self):
        for x in range(27):
            self.assertEquals(None, self.castle.train())

    def test_train_slave(self):
        self.castle.add_to_training_queue('slave')
        self.castle.train()
