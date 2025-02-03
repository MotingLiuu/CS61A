class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

pair1 = Pair(1, Pair(Pair(1, 1), 1))