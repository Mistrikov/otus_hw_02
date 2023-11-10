from card import Card
from player import Player
from random import choice

class Game:
    def __init__(self):
        self._players = []
        self.meshok = [i for i in range(1, 91)]

    def _create_players(self, players_count=2):
        for i in range(1, players_count+1):
            human = input(f'{i} игрок человек? (y/n): ') == 'y'
            if human:
                name = ''
                while name=='':
                    name = input('Введите имя игрока: ')
            else:
                name = 'Компьютер'
            self._players.append(Player(name, human))
    
    def show_cards(self):
        for player in self._players:
            player.show_card()

    def run(self):
        self._create_players(2)
        self.show_cards()