import random
class hangman:
    def __init__(self):
        self.words = ["asd", "dsa", "dgw"] # заменить на файл со словами
        self.bukvi = ["a", "s", "d","g", "w"] # заменить на файл с буквами
    def start(self):
        print("Добро пожаловать в игру виселица")
        
        a = input("Начнем? (старт/выход)").lower()
        if a == "старт":
            print("Начинаем")
            game.roung()
        elif a == "выход":
            print("до скорой встречи")    
        else:
            print("Неверный ввод")
            game.start()
            
            
    def roung(self):
        self.guessed = []
        self.word = []
        self.word = list(self.words[random.randint(0, 2)])
        for i in self.word:
            self.guessed.append("_")
        game.turn()
            
    def turn(self):
        self.lives = 10
        self.wrong = []
        while self.lives != 0:
            if self.word == self.guessed:
                break
            print("Выбери букву:")
            f = input().lower()
            if f in self.guessed:
                print("Буква повторяется")
            elif f in self.bukvi and f in self.word:
                print("Буква ", f, " есть")
                for i in range(self.word.count(f)):
                    self.guessed.pop(self.word.index(f))
                    self.guessed.insert(self.word.index(f), f)
                print(game.prins())
                print(self.guessed)
            elif f in self.bukvi and f not in self.word:
                print("Буквы ", f, " нет")
                self.lives -= 1
                self.wrong.append(f)
                print(game.prins())
                print("Угаданные: ", self.guessed)
                print("Неверные: ", self.wrong)
                print(self.lives)
            else:
                print("Ошибка ввода")
        game.end()
            
    def prins(self):
        s = "*Сделать виселицу"
        return s
    
    def end(self):
        if self.lives > 0:
            print("Ты победил!")
        else:
            print("Тебя повесили")
        c = input("Сыграем еще? (Да/Нет)").lower()
        if c == "да":
            print("Сыграем")
            game.roung()
        elif c == "нет":
            print("До скорой встречи")
        else:
            print("Ошибка ввода")
            
game = hangman()
game.start()
                