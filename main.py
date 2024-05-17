from anki import Anki
from terminalui import TerminalUserInterface
from loader import PickleLoader, JsonLoader


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('storage', choices=['json', 'pickle'])
    parser.add_argument('filename')
    args = parser.parse_args()
    
    if args.storage == 'pickle':
        loader = PickleLoader(args.filename)
    else:
        loader = JsonLoader(args.filename)

    with loader as loader:
        anki = Anki(loader.load_cards())
        user_interface = TerminalUserInterface(anki)
        user_interface.main_loop()
