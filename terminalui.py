import textwrap

from anki import Anki


class TerminalUserInterface:

    greeting = """\
        Программа Anki карты. Выберите что вы хотите сделать:
        0. Выход
        1. Добавить новую карту
        2. Угадывать
        3. Показать карточки
        """
    
    def __init__(self, anki: Anki):
        self.anki = anki
        self.correct_answers = 0

    def main_loop(self):
        while True:
            print(textwrap.dedent(self.greeting))
            
            user_choice = input()
            if user_choice == '0':
                break        
            elif user_choice == '1':
                self.create_new_cards()
            elif user_choice == '2':
                self.guess_card()
            elif user_choice == '3':
                self.print_cards()
            else:
                print('Пока не сделал!')

    def create_new_cards(self):
        while True:
            user_input = input('Введите слово и его перевод в формате слово:перевод. Для остановки введите "стоп".\n')
            if user_input.lower() == "стоп":
                break
            word, separator, translation = user_input.partition(':')
            self.anki.add_card(word, translation)

    def guess_card(self):
        print('Для остановки, введите "стоп"')
        while True:
            card = self.anki.get_card()
            user_translation = input(f'Ваше слово: {card.word}. Ваш перевод?\n')
            if user_translation.lower() == 'стоп':
                print(f'Вы верно перевели {self.correct_answers} слов!')
                break
            elif card.guess_translation(user_translation):
                self.correct_answers += 1
                print("Поздравляю! Все верно")
            else:
                print("Неправильно, учи ещё")

    def print_cards(self):
        for card in self.anki:
            print(card)