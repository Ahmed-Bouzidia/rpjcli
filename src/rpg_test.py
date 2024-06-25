import unittest
from personnage import Personnage

class TestPersonnage(unittest.TestCase):

    def test_initalesPointsInit(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.get_points())

    def test_isAliveAtGameStartInit(self):
        personnage = Personnage()
        self.assertTrue(personnage.is_alive())

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
    
    def test_return1(self):
        self.assertEqual(1, 1)
    
    def test_add_health(self):
        personnage= Personnage()
        personnage.hurt_player()
        personnage.hurt_player()
        personnage.add_health(20)
        self.assertEqual(80,personnage.points)

    def test_add_health_failure(self):
        personnage= Personnage()
        personnage.hurt_player()
        personnage.hurt_player()
        personnage.add_health(20)
        self.assertEqual(60,personnage.points)
if __name__ == '__main__':
    unittest.main()