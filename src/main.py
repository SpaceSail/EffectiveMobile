import argparse
import sys
from argparse import ArgumentParser
from models import Storage
from helpers import (check_json_storage, create_json_storage, write_json,
                     get_all_books, map)

parser = ArgumentParser(description='Simple app')
parser.add_argument('-t', type=str, help='Title of a book')
parser.add_argument('-a', type=str, help='Author of a book')
parser.add_argument('-y', type=str, help='Year of a book')
parser.add_argument('-com', choices=['search', 'delete', 'get_all',
                                     'change_status'], help='Command list.'
                                                            'delete needs an '
                                                            'id. Change status '
                                                            'needs id and new '
                                                            'status')
args = parser.parse_args()


def main():
    try:
        check_json_storage()
        if check_json_storage() is False:
            create_json_storage()
        map(args.com)
        parser.print_help()
        book = Storage(title=args.t, author=args.a, year=args.y)
        write_json(book)

    except Exception as e:
        print(e)
        parser.print_help()


if __name__ == '__main__':
    main()
