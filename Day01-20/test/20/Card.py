class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = ['♠️', '♥️', '♦️', '♣️']
        faces = ['', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        # 返回牌的花色和点数
        return f'{suites[self.suite]}{faces[self.face]}'

    def __lt__(self, other):
        if self.suite != other.suite:
            return self.suite < other.suite
        else:
            return self.face < other.face
