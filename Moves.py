import random


class Moves:
    """Класс действий игрока"""
    # Урон
    def damage(self, min_range, max_range):
        hit = random.randint(min_range, max_range)
        return hit

    # Исцеление
    def heal(self, min_range, max_range):
        restored_hp = random.randint(min_range, max_range)
        return restored_hp
