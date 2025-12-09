# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt


def display_list(items: list):
    for item in items:
        print(item)


def main():
    goncourt: Goncourt = Goncourt()

    identity: str = input("Entrez votre nom : ")

    print(goncourt.get_author_by_id(1))
    display_list(goncourt.get_all_authors())

    print(goncourt.get_book_by_id(1))
    display_list(goncourt.get_books_selection(3))

    books: list = [goncourt.get_book_by_id(1).id_book, goncourt.get_book_by_id(2).id_book]
    #goncourt.set_books_selection(books, 3)

    input("Entrez votre nom : ")

if __name__ == '__main__':
    main()
