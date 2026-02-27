
from Card import Card
import random


class Poker:
    """
    例子1：扑克游戏。
    说明：简单起见，我们的扑克只有52张牌（没有大小王），
    游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，
    按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
    """

    def __init__(self):
        self.cards = [Card(suite, face) for suite in range(4)
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        return self.current < len(self.cards)
