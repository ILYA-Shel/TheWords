class Player:

    def __init__(self, name):
        """
        Инициализирует аттрибуты класса.
        Обязательным является только аттрибут "имя игрока"
        :param name:
        """
        self.name = name
        self.points = 0
        self.used_word = list()

    def __repr__(self):
        return f"Имя пользователя: {self.name}\nОчки: {self.points}"

    def used_words_count(self):
        """
        Считает количество угаданных слов
        :return:
        """
        return len(self.used_word)

    def add_word(self, word):
        """
        Добавляет словов в список угаданных
        :param word:
        :return:
        """
        self.used_word.append(word)
        self.points = self.points + 1

    def check(self, word):
        """
        Проверяет слово на наличие в списке угаданных (на повторение)
        :param word:
        :return:
        """
        for item in self.used_word:
            if word == item:
                return True
        else:
            return False

    def player_result(self):
        return f"Имя игрока: {self.name}, угадано слов {len(self.used_word)}"
