from Moves import Moves


class Player(Moves):
    """Клас игрок"""
    def __init__(self, name):
        self.__hp = 100
        self.__name = name

    def get_health(self):
        return self.__hp

    def set_health(self, hp):
        if hp < 0:
            self.__hp = 0
        elif hp > 100:
            self.__hp = 100
        else:
            self.__hp = hp

    def get_name(self):
        return self.__name

