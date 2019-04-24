class SeaMap():
    def __init__(self):
        self.map = [['.' for i in range(11)] for i in range(11)]
        
    def shoot(self, row, col, result):
        if result == 'sink':
            self.map[row][col] = 'x'
            if self.map[row+1][col+1] != 'x' : self.map[row+1][col+1] = '*'
            if self.map[row-1][col-1] != 'x' : self.map[row-1][col-1] = '*'
            if self.map[row+1][col] != 'x' : self.map[row+1][col] = '*'
            if self.map[row][col+1] != 'x' : self.map[row][col+1] = '*'
            if self.map[row-1][col] != 'x' : self.map[row-1][col] = '*'
            if self.map[row-1][col+1] != 'x' : self.map[row-1][col+1] = '*'
            if self.map[row+1][col-1] != 'x' : self.map[row+1][col-1] = '*'
            if self.map[row][col-1] != 'x' : self.map[row][col-1] = '*'

        elif result == 'miss':
            self.map[row][col] = '*'
    def cell(self, row, col):
        return self.map[row][col]

