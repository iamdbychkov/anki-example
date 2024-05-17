import pickle
import pathlib
import random
import textwrap


cards: list[dict] = []


def add_card(word: str, translation: str) -> None:
    cards.append(
        {
            'word': word,
            'translation': translation,
        }
    )


def guess_card():
    print('Для остановки, введите "стоп"')
    correct_answers = 0
    while True:
        card = random.choice(cards)
        user_translation = input(f'Ваше слово: {card["word"]}. Ваш перевод?\n')
        if user_translation.lower() == 'стоп':
            print(f'Вы верно перевели {correct_answers} слов!')
            break
        elif user_translation.lower() == card['translation']:
            correct_answers += 1
            print("Поздравляю! Все верно")
        else:
            print("Неправильно, учи ещё")


def create_new_cards():
    while True:
        user_input = input('Введите слово и его перевод в формате слово:перевод. Для остановки введите "стоп".\n')
        if user_input.lower() == "стоп":
            break
        word, separator, translation = user_input.partition(':')
        add_card(word, translation)


def main_loop():
    greeting = """\
        Программа Anki карты. Выберите что вы хотите сделать:
        0. Выход
        1. Добавить новую карту
        2. Угадывать
        3. Показать карточки
        """
    while True:
        print(textwrap.dedent(greeting))
        
        user_choice = input()
        if user_choice == '0':
            break        
        elif user_choice == '1':
            create_new_cards()
        elif user_choice == '2':
            guess_card()
        elif user_choice == '3':
            for card in cards:
                print(f'Слово: {card["word"]}, перевод: {card["translation"]}')
        else:
            print('Пока не сделал!')


if __name__ == '__main__':
    db_path = pathlib.Path('anki.db')
    if db_path.exists():
        with db_path.open('rb') as db:
            cards = pickle.load(db)
    
    main_loop()

    with db_path.open('wb') as db:
        pickle.dump(cards, db)