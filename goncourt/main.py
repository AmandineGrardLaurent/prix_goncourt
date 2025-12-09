# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt


def display_list(items: list):
    for item in items:
        print(item)


def main():
    goncourt: Goncourt = Goncourt()

    print(goncourt.get_author_by_id(1))
    display_list(goncourt.get_all_authors())

    print(goncourt.get_book_by_id(2))
    display_list(goncourt.get_all_books())


if __name__ == '__main__':
    main()
