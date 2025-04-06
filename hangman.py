import random
class hangman:
    def __init__(self):
        self.bukvi = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']
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
        c = 0
        file = open('russian_nouns.txt', 'r', encoding='utf-8')
        content = file.readlines()
        while c <= 5:
            self.word = list(content[random.randint(1, 51301)])
            self.word.pop(len(self.word)-1)
            c = len(self.word)
        file.close()
        print(self.word)
        self.guessed = []
        for i in self.word:
            self.guessed.append("_")
        game.turn()
            
    def turn(self):
        self.lives = 10
        self.wrongs = []
        while self.lives != 0:
            if self.word == self.guessed:
                
                break
            print("Выбери букву:")
            f = input().lower()
            if f in self.guessed:
                print("Буква повторяется")
            elif f in self.bukvi and f in self.word:
                game.right(f)
            elif f in self.bukvi and f not in self.word:
                game.wrong(f)
            else:
                print("Ошибка ввода")
        game.end()
    
    def right(self, f):
        print("Буква ", f, " есть")
        for i in range(len(self.word)):
            if self.word[i] == f:
                self.guessed.pop(i)
                self.guessed.insert(i, f)
        print(game.prins())
        print(self.guessed)
        
    def wrong(self, f):
        print("Буквы ", f, " нет")
        self.lives -= 1
        self.wrongs.append(f)
        print(game.prins())
        print("Угаданные: ", self.guessed)
        print("Неверные: ", self.wrongs)
     
    def prins(self):
        s = "*Сделать виселицу"
        return s
    
    def end(self):
        if self.lives > 0:
            print("Слово: ", self.word)
            print("Ты победил!")
        else:
            print("Слово: ", self.word)
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
                