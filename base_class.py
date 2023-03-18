class BasicWord:
    """
    Класс загадываемых слов.
    Содержит основное слово и список возможных слов.
    """

    def __init__(self, base_word, word_list):
        """
        Инициализация аттрибутов класса
        :param base_word:
        :param word_list:
        """

        self.base_word = base_word.upper()
        self.word_list = word_list

    def __repr__(self):
        """
        Представлеие полей объектов класса
        :return:
        """

        return f"Базовое слово: {self.base_word} \n Допустимые слова: {self.word_list}"

    def word_count(self):
        """
        Возвращает количество возможных слов
        :return:
        """
        return len(self.word_list)

    def check_word(self, word):
        """
        Определяет вхождение слова в список возможных слов
        Возвращает булевое значение
        :param word:
        :return:
        """
        for item in self.word_list:
            if word == item:
                return True
        else:
            return False