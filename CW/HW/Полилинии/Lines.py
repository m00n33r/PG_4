from Board import Board
import queue


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def has_path(self, x1, y1, x2, y2, n):
        was = [[1e4] * n[0] for _ in range(n[1])]
        p = [[0] * n[0] for _ in range(n[1])]
        q = queue.Queue()
        q.put([x1, y1])
        pth = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        was[y1][x1] = 0
        while not q.empty():
            v = q.get()
            for i in pth:
                if (not 0 <= v[1] + i[1] < n[1]) or (not 0 <= v[0] + i[0] < n[0]):
                    continue
                if self.board[v[1] + i[1]][v[0] + i[0]] != -1:
                    continue
                if was[v[1] + i[1]][v[0] + i[0]] > was[v[1]][v[0]]:
                    was[v[1] + i[1]][v[0] + i[0]] = was[v[1]][v[0]] + 1
                    p[v[1] + i[1]][v[0] + i[0]] = [v[0], v[1]]
                    q.put([v[0] + i[0], v[1] + i[1]])
        ans = []
        if was[y2][x2] != 1e4:
            ind = [x2, y2]
            while ind != [x1, y1]:
                ans.append(ind)
                ind = p[ind[1]][ind[0]]
            ans.append(ind)
            return ans
        return 0
