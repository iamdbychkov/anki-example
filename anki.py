import random


class Card:
    
    def __init__(self, word: str, translation: str):
        self.word = word
        self.translation = translation.lower()

    def guess_translation(self, user_transaltion: str) -> bool:
        return self.translation == user_transaltion.lower()
    
    def __str__(self):
        return f'Слово: {self.word}, перевод: {self.translation}'


class Anki:

    _cards: list[Card]

    def __init__(self, cards: list | None = None):
        if cards is None:
            cards = []
        self._cards = cards

    def add_card(self, word: str, translation: str) -> None:
        self._cards.append(
            Card(word, translation)
        )
    
    def get_card(self):
        """Возвращает случайную карточку из `self._cards`
        """
        return random.choice(self._cards)
    
    def __iter__(self):
        return iter(self._cards)