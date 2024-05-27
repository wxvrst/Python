class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]
 
    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        else:  # result == 'sink'
            # помечаем клетки вокруг потопленного корабля
            for r in range(max(0, row - 1), min(row + 2, 10)):
                for c in range(max(0, col - 1), min(col + 2, 10)):
                    if row != r or col != c:
                        if self.map[r][c] == '.':
                            self.map[r][c] = '*'
                        elif self.map[r][c] == 'x':
                            self.map[r][c] = "."
                            self.shoot(r, c, result)
            self.map[row][col] = 'x'
 
    def cell(self, row, col):
        return self.map[row][col]
    
sm=SeaMap()
sm.shoot(2,4,'sink')
sm.shoot(6,9,'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row,col),end="")
    print()