from card import Card
from player import Player
from random import choice
from meshok import Meshok

class Game:
    def __init__(self):
        self._players = []
        self.meshok = Meshok()
        self._isRun = False

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
    
    def _show_cards(self):
        for player in self._players:
            player.show_card()
    
    def next_step(self, b):
        for player in self._players:
            if not player.next_step(b):
                print(f'Игрок {player.name} проиграл')
                self._isRun = False
                break

    def run(self):
        self._isRun = True
        self._create_players(2)
        print(self._players[0].card.numbers)
        #while self._isRun:
        '''for i in range(5):
            self._show_cards()
            b = self.meshok.get_new()
            if not b:
                self._isRun = False
                break
            self.next_step(b)
            print(self.meshok.get_used())'''
        self._show_cards()
        print(self.next_step(int(input('n='))))
        for player in self._players:
            print(player.name, player.isWin)
        self._show_cards()