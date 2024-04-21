# 1)Создание класса поля где мы будем ходить: 10 минут
# 1.2)вывод поля: 10 минут
#
# 2)Создания класс персонажа игрока: 10 минут
# 2.2)Возможность ходить персонажем: 20 минут
#
# 5)Создание клеток преград через которые нельзя проходить
#
# 6)Создание интерфейсов, меню и диалоговых окон

# Поле 100 x 20

class Field:
    def __init__(self):
        self.stock_field = []
        with open("map.txt", "r", encoding="utf-8") as f:
            self.imported_map = f.read()
        self.stock_field = self.imported_map.split("\n")


class Game(Field):
    def __init__(self):
        self.grid = self.stock_field
        self.x = 0
        self.y = 0

    def walk(self, direction):
        if direction == "w":
            self.y -= 1
        elif direction == "s":
            self.y += 1
        elif direction == "d":
            self.x += 1
        else:
            self.x -= 1

    def display(self):
        self.grid[self.y][self.x] = "@"
        print(self.grid)

    def play(self):
        while True:
            self.display()
            self.walk(input())


fif = Game()
fif.play()
