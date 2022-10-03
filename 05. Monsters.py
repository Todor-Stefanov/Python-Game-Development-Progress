import random


class Monster:
    def __init__(self, n_rows, n_cols, max_speed):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.my_row = random.randrange(self.n_rows)
        self.my_column = random.randrange(self.n_cols)
        self.my_speed_x = random.randrange(-max_speed, max_speed + 1)
        self.my_speed_y = random.randrange(-max_speed,max_speed + 1)
        self.max_speed = max_speed
        self.position = [self.my_row, self.my_column, self.my_speed_x, self.my_speed_y]

    def move(self):
        self.my_row = (self.my_row + self.my_speed_x) % self.n_rows
        self.my_column = (self.my_column + self.my_speed_y) % self.n_cols
        self.position[0] = self.my_row
        self.position[1] = self.my_column


n_monsters = 5
n_rows = 100
n_cols = 200
max_speed = 4
monster_list = []

for i in range(n_monsters):
    obj_monster = Monster(n_rows, n_cols, max_speed)
    print(obj_monster.position)
    monster_list.append(obj_monster)

print("--------------------")
for monster in monster_list:
    monster.move()
    print(monster.position)
