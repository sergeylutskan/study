# Simple Sea battle 

from solution3 import SeaMap

sm = SeaMap()
sm.shoot(9, 3, 'sink')
sm.shoot(9, 4, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
