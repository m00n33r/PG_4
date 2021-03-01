from Board import Board


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.was = []

    def rec(self, x1, y1, x2, y2, n):
        if x1 == x2 and y1 == y2:
            return 1
        if self.was[y1][x1]:
            return 0
        self.was[y1][x1] = 1
        if y1 + 1 < n[1] and self.get_color((x1, y1 + 1)) == -1:
            z = self.rec(x1, y1 + 1, x2, y2, n)
            if z:
                return 1
        if y1 - 1 >= 0 and self.get_color((x1, y1 - 1)) == -1:
            z = self.rec(x1, y1 - 1, x2, y2, n)
            if z:
                return 1
        if x1 + 1 < n[0] and self.get_color((x1 + 1, y1)) == -1:
            z = self.rec(x1 + 1, y1, x2, y2, n)
            if z:
                return 1
        if x1 - 1 >= 0 and self.get_color((x1 - 1, y1)) == -1:
            z = self.rec(x1 - 1, y1, x2, y2, n)
            if z:
                return 1
        return 0

    def has_path(self, x1, y1, x2, y2, n):
        self.was = [[0] * n[0] for _ in range(n[1])]
        return self.rec(x1, y1, x2, y2, n)
