# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt
from goncourt.models.academyMember import AcademyMember
from goncourt.models.book import Book


def display_academy_member(members: list[AcademyMember]) -> None:
    print("------------- Voici la liste des académiciens -------------\n")

    for member in members:
        print(member)


def display_book_name_list(books: list[Book]) -> None:
    if len(books) > 0:
        for book in books:
            print(f"{book.id_book} - {book.title}")
    else:
        print("La sélection n'a pas encore été faite")


def display_votes_and_winner(goncourt: Goncourt) -> None:
    print("------------- Voici les résultats des votes de la sélection 3 -------------\n")
    votes: dict[int, int] = goncourt.get_votes_selection_3()
    books: list[Book] = goncourt.get_books_selection(3)
    votes_by_title: dict[str, int] = {book.title: votes.get(book.id_book, 0) for book in books}

    for title, nb_votes in votes_by_title.items():
        print(f"{title} : {nb_votes} vote(s)")

    winner_title: str = max(votes_by_title, key=votes_by_title.get)
    winner_votes: int = votes_by_title[winner_title]

    print(f"\nLe lauréat est '{winner_title}' avec {winner_votes} vote(s)")


def add_books_in_selection(goncourt: Goncourt) -> None:
    current_selection: int = int(input("Quelle selection souhaitez-vous ajouter ?\n"))
    previous_selection: int = current_selection - 1

    print(
        f"------------- Voici la liste des livres de la selection {previous_selection} -------------\n")

    display_book_name_list(goncourt.get_books_selection(previous_selection))
    ids_book_str: str = input(
        f"\nVeuillez saisir les titres retenus pour la sélection {current_selection} "
        f"{"(8 livres)" if current_selection == 2 else "(4 livres)"} :\n")

    ids_book: list[int] = [int(x.strip()) for x in ids_book_str.split(",")]

    goncourt.set_books_selection(ids_book, current_selection)


def add_votes_in_selection(goncourt: Goncourt, selection_nb: int) -> None:
    votes: dict[int, int] = {}

    for book in goncourt.get_books_selection(selection_nb):
        vote_nb = int(input(f"Saisissez le nombre de vote pour le livre {book.title} : "))
        votes[book.id_book] = vote_nb

    goncourt.set_votes_selection_3(votes)
    print(f"Les votes pour la sélection {selection_nb} sont enregistrés :\n")


def display_book_details(goncourt: Goncourt) -> None:
    id_book: str = input("\nQuel livre souhaitez-vous consulter ?\n")
    book: Book = goncourt.get_book_by_id(int(id_book))

    if book:
        print(book)
    else:
        print("Livre inexistant")


def display_selection(goncourt: Goncourt, selection_nb: int) -> None:
    print(
        f"------------- Voici la liste des livres de la sélection n°{selection_nb}  -------------")
    display_book_name_list(goncourt.get_books_selection(selection_nb))


def main() -> None:
    goncourt: Goncourt = Goncourt()

    identity: str = input("Entrez votre nom : \n").strip()
    if goncourt.verify_is_president(identity):
        print("Bonjour président")

        while True:

            print("\nQue voulez-vous faire ?\n")
            choice: str = input("[1] afficher la liste des académiciens\n"
                                "[2] afficher la liste des livres d'une selection\n"
                                "[3] afficher les votes de la sélection 3\n"
                                "[4] ajouter la liste des livres retenus lors d'une sélection\n"
                                "[5] ajouter les votes de la sélection 3\n"
                                "[6] afficher les détails d'un livre\n"
                                "[7] session terminée\n")
            match choice:
                case '1':
                    display_academy_member(goncourt.get_all_academy_members())

                case '2':
                    selection_choice: int = int(input("\nQuelle selection souhaitez-vous afficher ?\n"))
                    display_selection(goncourt, selection_choice)

                case '3':
                    display_votes_and_winner(goncourt)

                case '4':
                    add_books_in_selection(goncourt)

                case '5':
                    display_selection(goncourt, 3)
                    add_votes_in_selection(goncourt, 3)

                case '6':
                    display_selection(goncourt, 1)
                    display_book_details(goncourt)

                case '7':
                    break

    else:

        print(f"Bonjour {"académicien" if goncourt.verify_is_academy_member(identity) else "utilisateur"}")
        while True:
            print("\nQue voulez-vous faire ?\n")
            choice: str = input("[1] afficher la liste des livres d'une selection\n"
                                "[2] afficher les détails d'un livre\n"
                                "[3] afficher les votes des livres de la sélection 3\n"
                                "[4] session terminée\n")

            match choice:
                case '1':
                    selection_choice: int = int(input("\nQuelle selection souhaitez-vous afficher ?\n"))
                    display_selection(goncourt, selection_choice)
                case '2':
                    display_selection(goncourt, 1)
                    display_book_details(goncourt)
                case '3':
                    display_votes_and_winner(goncourt)
                case '4':
                    break


if __name__ == '__main__':
    main()
