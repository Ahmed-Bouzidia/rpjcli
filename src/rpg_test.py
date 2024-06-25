import unittest
from personnage import Personnage


class TestPersonage(unittest.TestCase):

    def test_initalesPointsInit(self):
        personage = Personnage()
        self.assertEqual(100, personage.get_points())

    def test_isAliveAtGameStartInit(self):
        personage = Personnage()
        self.assertTrue(personage.is_alive())

    def test_attackReduceOnePointsForVictimInit(self):
        mechant = Personnage()
        victime = Personnage()
        mechant.attack(victime)
        self.assertEqual(99, victime.get_points())

    def test_hertReduceTwentyPointsForVictimInit(self):
        mechant = Personnage()
        victime = Personnage()
        mechant.hurt(victime)
        self.assertEqual(80, victime.get_points())

    def test_hertReducePointsToZeroForVictimInit(self):
        mechant = Personnage()
        victime = Personnage()
        for _ in range(5):
            mechant.hurt(victime)
        self.assertEqual(0, victime.get_points())

    def test_vicimeIsNotAliveInit(self):
        mechant = Personnage()
        victime = Personnage()
        for _ in range(5):
            mechant.hurt(victime)
        self.assertFalse(victime.is_alive())

    def test_initial_position(self):
        personage = Personnage()
        self.assertFalse((), personage.get_position())

    def test_return1(self):
        self.assertEqual(1, 1)

    def test_add_health(self):
        personnage = Personnage()
        personnage.hurt_player()
        personnage.hurt_player()
        personnage.add_health(30)
        self.assertEqual(90,personnage.points)

    def test_add_healthFail(self):
        personnage= Personnage()
        personnage.hurt_player()
        personnage.hurt_player()
        personnage.add_health(20)
        self.assertEqual(80, personnage.points)




if __name__ == '__main__':
    unittest.main()
