import Constants
import random


class Battle:
    """Класс моделирования игры"""
    def __init__(self):
        self.__players = []
        self.__current_user = None
        self.__winner = None

    def add_players(self, *players):
        """Метод добавления игроков"""
        for player in players:
            if player not in self.__players:
                self.__players.append(player)

    def status_game(self):
        """Вывод здоровья игроков"""
        for i in range(0, len(self.__players)):
            print("У " + self.__players[i].get_name() + "а " + str(self.__players[i].get_health()) + " HP. ")

    def select_move(self, enemy_id, move_num):
        """ Метод выбора хода"""
        enemy = self.__players[enemy_id]

        # Урон в небольшом диапазоне
        if move_num == Constants.MoveNums.LOW_RANGE_DAMAGE:
            hit = self.__current_user.damage(Constants.Ranges.MIN_LOW_RANGE, Constants.Ranges.MAX_LOW_RANGE)
            enemy.set_health(enemy.get_health() - hit)
            print(self.__current_user.get_name() + " нанес " + str(hit) + " урона " + enemy.get_name() + "у.")
            self.status_game()

        # Урон в большом диапазоне
        elif move_num == Constants.MoveNums.HIGH_RANGE_DAMAGE:
            hit = self.__current_user.damage(Constants.Ranges.MIN_HIGH_RANGE, Constants.Ranges.MAX_HIGH_RANGE)
            enemy.set_health(enemy.get_health() - hit)
            print(self.__current_user.get_name() + " нанес " + str(hit) + " урона " + enemy.get_name() + "у.")
            self.status_game()

        # Исцеление в малом диапазоне
        else:
            restored_hp = self.__current_user.heal(Constants.Ranges.MIN_LOW_RANGE, Constants.Ranges.MAX_LOW_RANGE)
            self.__current_user.set_health(self.__current_user.get_health() + restored_hp)
            print(self.__current_user.get_name() + " восстановил " + str(restored_hp) + " HP.")
            self.status_game()

    def start(self):
        """Метод запуска игры"""
        if len(self.__players) < Constants.PlaySettings.MIN_NUM_PLAYERS:
            print("Недостаточно игроков.")
            return

        while True:
            # Определение игрока, делающего ход
            current_player = random.randint(0, len(self.__players) - 1)
            self.__current_user = self.__players[current_player]

            # Определение противника игрока на этот ход
            enemy_list = list(range(0, current_player)) + list(range(current_player + 1, len(self.__players)))
            enemy_id = random.choice(enemy_list)

            move_id = 0
            # Повышен шанс исцеления если здоровье компютера меньше 35
            if self.__current_user.get_name == "Computer" and self.__current_user.get_health < Constants.PlaySettings.POOR_HP:
                move_id = random.randint(1, 4)
                if move_id > 3:
                    move_id = 3
            else:
                move_id = random.randint(1, 3)

            self.select_move(enemy_id, move_id)

            # Поражение если игроков больше 2-х
            if self.__players[enemy_id].get_health() == 0 and len(self.__players) > Constants.PlaySettings.MIN_NUM_PLAYERS:
                print(self.__players[enemy_id].get_name() + " проиграл и покидает игру.")
                del self.__players[enemy_id]

            # Поражение при 2-х игроках
            elif self.__players[enemy_id].get_health() == 0 and len(self.__players) == Constants.PlaySettings.MIN_NUM_PLAYERS:
                print(self.__players[enemy_id].get_name() + " проиграл.")
                break

        self.__winner = self.__current_user
        print(self.__winner.get_name() + " победил.")
