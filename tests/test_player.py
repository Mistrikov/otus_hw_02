import unittest
from unittest.mock import patch, MagicMock

from player import Player

class Card:
    def __init__(self):
        # для быстрой проверки, можно зафиксировать карточки для обоих игроков
        self.numbers = [[0, 13, 0, 34, 43, 0, 62, 77, 0], [0, 0, 0, 35, 0, 54, 64, 78, 86], [4, 14, 28, 0, 44, 0, 0, 79, 0]]



class PlayerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.name = 'Человек'
        cls.isHuman = True
        cls.player = Player(name=cls.name, human=cls.isHuman)
        #cls.player.card = Card() # переписать карточку игрока для возможности проверки
    
    def test_init(self):
        self.assertEqual(self.player.name, self.name)

    def test_check_step_human_1(self):
        nums = [ x for x in self.player.card.numbers[0] if x>0 ] # берем из карточки верхний ряд чисел
        class MockInput(MagicMock):
            def __call__(self, *args):
                return 'y'
        for num in nums:
            with patch('builtins.input', MockInput()):
                assert self.player._check_step_human(num) == True, 'Человек вычеркивает число из карточки'
        
    
    def test_check_step_human_2(self):
        nums = [ x for x in self.player.card.numbers[0] if x>0 ] # берем из карточки верхний ряд чисел
        class MockInput(MagicMock):
            def __call__(self, *args):
                return 'n'
        
        for num in nums:
            with patch('builtins.input', MockInput()):
                assert self.player._check_step_human(num) == False, 'Человек НЕ вычеркивает число из карточки'