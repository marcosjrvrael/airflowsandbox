import argparse
import logging


def get_count(input_str: str) -> str:
    """
        Função responsável por fazer a contagem de vogais em uma palavra
    """
    num_vowels = 0
    lista = [i for i in input_str if i in 'aeiou']
    num_vowels = len(lista)
    return num_vowels


def run (word: str) -> str:
    logging.info(f'Vowels count: {get_count(word)}')


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--word',
        type=str,
        help='Word to have vowels count',
        required=True
    )

    args = parser.parse_args()
    logging.info(f"Execution arguments: {args}")

    run(args.word)
