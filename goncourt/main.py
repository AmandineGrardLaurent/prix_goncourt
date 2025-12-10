# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt


def display_list(items: list):
    for item in items:
        print(item)


def display_book_name_list(books: list):
    if len(books) > 0:
        for book in books:
            print(f"{book.id_book} - {book.title}")
    else:
        print("La sélection n'a pas encore été faite")


def main():
    goncourt: Goncourt = Goncourt()

    identity: str = input("Entrez votre nom : \n")
    if goncourt.verify_is_president(identity):
        print("Bonjour président")

        while True:

            print("\nQue voulez-vous faire ?\n")
            choice: str = input("[1] afficher la liste des académiciens\n"
                                "[2] afficher la liste des livres d'une selection\n"
                                "[3] ajouter la liste des livres retenus lors d'une sélection\n"
                                "[4] afficher les détails d'un livre\n"
                                "[5] session terminée\n")
            match choice:
                case '1':
                    print("------------- Voici la liste des académiciens -------------\n")
                    display_list(goncourt.get_all_academy_members())
                case '2':
                    selection_choice: str = input("\nQuelle selection souhaitez-vous afficher ?\n")
                    print(
                        f"------------- Voici la liste des livres de la sélection n°{selection_choice}  -------------")
                    display_book_name_list(goncourt.get_books_selection(int(selection_choice)))
                case '3':
                    current_selection_str: str = input("Quelle selection souhaitez-vous ajouter ?\n")
                    current_selection_int: int = int(current_selection_str)
                    last_selection_int = int(current_selection_str) - 1

                    print(
                        f"------------- Voici la liste des livres de la selection {last_selection_int} -------------\n")
                    display_book_name_list(goncourt.get_books_selection(last_selection_int))
                    id_book_list_str: str = input(
                        f"\nVeuillez saisir les titres retenus pour la sélection {current_selection_int} "
                        f"{"(8 livres)" if current_selection_int == 2 else "(4 livres)"} :\n")
                    id_book_list_int: list[int] = [int(x.strip()) for x in id_book_list_str.split(",")]
                    goncourt.set_books_selection(id_book_list_int, current_selection_int)

                case '4':
                    print("------------- Voici la liste des livres ------------\n")
                    display_book_name_list(goncourt.get_books_selection(1))
                    id_book: str = input("\nQuel livre souhaitez-vous consulter ?\n")
                    print(goncourt.get_book_by_id(int(id_book)))
                case '5':
                    break

    else:
        print("Bonjour académicien")


if __name__ == '__main__':
    main()
