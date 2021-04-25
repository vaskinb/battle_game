from Player import Player
from Battle import Battle


# Симуляция сражения компьютера и одного игрока
battle = Battle()
computer = Player("Компьютер")
player_name = input("Введите имя игрока: ")
player = Player(player_name)
battle.add_players(computer, player)
battle.start()
