import pathlib
import pickle
import json

from anki import Card


class PickleLoader:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.cards = []

    def load_cards(self):
        db_path = pathlib.Path(self.file_name)
        if db_path.exists():
            with db_path.open('rb') as db:
                self.cards = pickle.load(db)
                return self.cards
        else:
            return self.cards

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        db_path = pathlib.Path(self.file_name)
        with db_path.open('wb') as db:
            pickle.dump(self.cards, db)


class JsonLoader:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.cards = []

    def load_cards(self):
        db_path = pathlib.Path(self.file_name)
        if db_path.exists():
            with db_path.open('rb') as db:
                self.cards = [
                    Card(card["word"], card["translation"]) for card in  json.load(db)
                ]
                return self.cards
        else:
            return self.cards

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        db_path = pathlib.Path(self.file_name)
        with db_path.open('w') as db:
            cards = [
                {"word": card.word, "translation": card.translation} for card in self.cards
            ]
            json.dump(cards, db)

