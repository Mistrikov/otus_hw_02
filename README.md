# otus_hw_02
Игра лото на 2 игрока по одной карточке у каждого.

Игроком могут быть человек или компьютер в любых комбинациях. 

Запуск игры через файл app.py

Добавлены тесты для pytest

tests/test_meshok.py - проверяет 2 функции: 1. создание мешка с 90 бочёнками, 2. Удаление всех 90 боченков из мешка

tests/test_player.py - проверяет 3 функции: 1. создание игрока, 2. зачеркивание существующего числа на карточке (правильный ход), 3. пропуск существующего числа на карточке (неправильный ход)