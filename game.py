from card import Card
from player import Player
from random import choice
from meshok import Meshok

class Game:
    def __init__(self):
        self._players = []
        self._meshok = Meshok()
        self._isRun = False

    def _create_players(self, players_count=2):
        idx=1
        for i in range(1, players_count+1):
            human = input(f'{i} игрок человек? (y/n): ') == 'y'
            if human:
                name = ''
                while name=='':
                    name = input('Введите имя игрока: ')
            else:
                name = f'Компьютер {idx}'
                idx += 1
            self._players.append(Player(name, human))
    
    def _show_cards(self):
        for player in self._players:
            #if not player.isLoss: player.show_card()
            player.show_card()
    
    def next_step_game(self):
        #b = int(input('Боченок=')) # ручной ввод боченка
        b = self._meshok.get_new() # новый боченок
        if not b:
            self._isRun = False
            return False
        
        # Выполнить ходы каждым игроком
        for player in self._players:
            #if not player.isLoss: player.next_step(b)
            player.next_step(b)
        
        # проверка окончания игры
        for player in self._players:
            if player.isWin or player.isLoss: 
                self._isRun = False
                return False

        return True

    def run(self):
        # подготовка
        self._isRun = True
        self._create_players(2)

        # игра
        while self._isRun:
            self._show_cards()
            self._isRun = self.next_step_game()
        
        # после игры
        self._show_cards()
        for player in self._players:
            if player.isWin:
                print(f'Игрок {player.name} выиграл')
            if player.isLoss:
                print(f'Игрок {player.name} проиграл')