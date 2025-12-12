# -*- coding: utf-8 -*-

from goncourt.business.goncourt import Goncourt
from goncourt.models.academyMember import AcademyMember
from goncourt.models.book import Book


# Display -------------------------------------------------------------------------------------------------------------

def display_academy_member_list(members: list[AcademyMember]) -> None:
    """
        Display the list of academy members
    :param members: List of academy members to display.
    """

    print("------------- Voici la liste des académiciens -------------\n")
    for member in members:
        print(member)


def display_book_selection(books: list[Book], selection_nb: int) -> None:
    """
        Display the list of books for a given selection.
    :param books: List of books in the selection.
    :param selection_nb: Selection number (1, 2, 3)
    """

    if len(books) > 0:
        print(
            f"------------- Voici la liste des livres de la sélection n°{selection_nb}  -------------")
        for book in books:
            print(f"{book.id_book} - {book.title}")
    else:
        print(f"La sélection n°{selection_nb} n'a pas encore été faite")


def display_winner(goncourt: Goncourt) -> None:
    """
        Display the winner of selection #3 based on the votes.
    """

    votes: dict[str, int] = goncourt.get_votes_selection(3)
    if len(goncourt.get_books_selection(3)) == 0 and len(goncourt.get_books_selection(3)) == 0:
        print("Le lauréat n'est pas encore connu")
    else:
        winner_title: str = max(votes, key=votes.get)
        winner_votes: int = votes[winner_title]
        print(f"\nLe lauréat est '{winner_title}' avec {winner_votes} vote(s)")


def display_votes_selection(goncourt: Goncourt, selection_nb: int):
    """
         Display the voting results for a given selection.
    :param selection_nb: Selection number (1, 2, 3)
    """

    votes: dict[str, int] = goncourt.get_votes_selection(selection_nb)
    if len(goncourt.get_books_selection(selection_nb)) == 0:
        print(f"La sélection {selection_nb} n'a pas encore eu lieu")
    else:
        print("------------- Voici les résultats des votes de la sélection n°3 -------------\n")
        for title, nb_votes in votes.items():
            print(f"{title} : {nb_votes} vote(s)")


def display_book_details(goncourt: Goncourt) -> None:
    """
        Display detailed information about a specific book.
    """
    id_book: str = input("\nQuel livre souhaitez-vous consulter ?\n")

    if verify_is_number(id_book):
        book: Book = goncourt.get_book_by_id(int(id_book))

        if book:
            print(book)
        else:
            print("Livre inexistant")
    else:
        print("Merci de saisir un chiffre.")


# Add ------------------------------------------------------------------------------------------------------------------

def add_books_in_selection(goncourt: Goncourt) -> None:
    """
        Add books to a given selection, after ensuring the previous selection exists.
    """
    current_selection: str = input("Quelle selection souhaitez-vous ajouter ?\n")

    if verify_is_number(current_selection):
        previous_selection: int = int(current_selection) - 1
        display_book_selection(goncourt.get_books_selection(previous_selection), previous_selection)
    else:
        print("Merci de saisir un chiffre.")
        return

    if len(goncourt.get_books_selection(previous_selection)) == 0:
        print(
            f"La sélection n°{previous_selection} doit avoir eu lieu avant d'ajouter le sélection n°{current_selection}")
        return

    else:
        ids_book_str: str = input(
            f"\nVeuillez saisir les titres retenus pour la sélection n°{current_selection} "
            f"{"(8 livres)" if int(current_selection) == 2 else "(4 livres)"} :\n")

        ids_book: list[str] = [x.strip() for x in ids_book_str.split(",")]

        for id_book in ids_book:
            if not verify_is_number(id_book) :
                print("Veuillez saisir un entier.")
                return

        if not verify_len_list_books(ids_book, int(current_selection)):
            print(f"Veuillez ressaisir la sélection -> "
                  f"{"8 entiers." if int(current_selection) == 2 else "4 entiers."}")
            return

        ids_book_int: list[int] = [int(x.strip()) for x in ids_book]
        goncourt.set_books_selection(ids_book_int, int(current_selection))
        print("La sélection a été ajoutée.")


def add_votes_in_selection(goncourt: Goncourt, selection_nb: int) -> None:
    """
        Add votes for each book in a given selection.
    :param selection_nb: The selection number for which votes should be added.
    """
    votes: dict[int, int] = {}

    if len(goncourt.get_books_selection(3)) > 0:
        for book in goncourt.get_books_selection(selection_nb):
            vote_nb = int(input(f"Saisissez le nombre de votes pour le livre '{book.title}' : "))
            votes[book.id_book] = vote_nb

        success = goncourt.selection_dao.update_vote_selection(selection_nb, votes)

        if success:
            print(f"Les votes pour la sélection n°{selection_nb} ont été enregistrés avec succès.\n")
        else:
            print("Erreur lors de l'enregistrement des votes.\n")


# Ask ------------------------------------------------------------------------------------------------------------------

def ask_choice_president() -> str:
    """
        Ask the president what action they want to perform.
    :return: The chosen menu option.
    """
    print("\nQue voulez-vous faire ?\n")
    choice: str = input("[1] afficher la liste des académiciens\n"
                        "[2] afficher la liste des livres d'une selection\n"
                        "[3] afficher les votes de la sélection n°3 et le lauréat\n"
                        "[4] afficher les détails d'un livre\n"
                        "[5] ajouter la liste des livres retenus lors d'une sélection\n"
                        "[6] ajouter les votes de la sélection n°3\n"
                        "[7] session terminée\n")
    return choice


def ask_choice_user() -> str:
    """
        Ask a regular user or an academy member what action they want to perform.
    :return: The chosen menu option.
    """
    print("\nQue voulez-vous faire ?\n")
    choice: str = input("[1] afficher la liste des livres d'une selection\n"
                        "[2] afficher les détails d'un livre\n"
                        "[3] afficher les votes des livres de la sélection 3\n"
                        "[4] session terminée\n")
    return choice


# Utils ----------------------------------------------------------------------------------------------------------------

def verify_is_number(input: str) -> bool:
    """
        Verify that the user's input is a valid number.
    :param input: The value entered by the user
    :return: True if the input contains only digits, otherwise False.
    """
    return input.strip().isdigit()


def verify_len_list_books(ids_book_list: list[str], selection_nb):
    """
        Check whether the number of selected books matches the expected amount
    for the given selection number.

    Selection rules:
      - Selection 2 must contain 8 books.
      - Selection 3 must contain 4 books.
    :param ids_book_list:  List of book IDs provided by the user.
    :param selection_nb: The selection number (typically 2 or 3).
    :return: True if the list length matches the selection rules, otherwise False.
    """
    return (selection_nb == 2 and len(ids_book_list) == 8) or (selection_nb == 3 and len(ids_book_list) == 4)


# Main -----------------------------------------------------------------------------------------------------------------

def main() -> None:
    """
        Main entry point of the application.
        Handles authentication, role-based menus, and user interactions.
    """
    goncourt: Goncourt = Goncourt()

    # Ask for the user's identity
    identity: str = input("Entrez votre nom : \n").strip()

    # Check if the user is the president of the Goncourt academy
    if goncourt.verify_is_president(identity):
        print("Bonjour Président")

        # President menu loop
        while True:

            # Ask which action the president wants to perform
            choice = ask_choice_president()

            # Match the user's choice with the corresponding operation
            match choice:
                case '1':
                    # Display the complete list of academy members
                    display_academy_member_list(goncourt.get_all_academy_members())

                case '2':
                    # Display books from a chosen selection
                    selection_choice: str = input("\nQuelle selection souhaitez-vous afficher ?\n")
                    if verify_is_number(selection_choice):
                        selection_choice_int = int(selection_choice)
                        display_book_selection(goncourt.get_books_selection(selection_choice_int), selection_choice_int)
                    else:
                        print("Merci de saisir un chiffre.")

                case '3':
                    # Display selection #3 votes and the winner
                    display_votes_selection(goncourt, 3)
                    display_winner(goncourt)

                case '4':
                    # Display selection #1, then request a specific book to show its details
                    display_book_selection(goncourt.get_books_selection(1), 1)
                    display_book_details(goncourt)

                case '5':
                    # Add books to a selection (after verifying the previous one exists)
                    add_books_in_selection(goncourt)

                case '6':
                    # Show books from selection #3, then allow the president to input votes
                    display_book_selection(goncourt.get_books_selection(3), 3)
                    add_votes_in_selection(goncourt, 3)

                case '7':
                    # Exit the president session
                    break

    else:
        # User is either an academy member or a normal user
        print(f"Bonjour {"Académicien" if goncourt.verify_is_academy_member(identity) else "Utilisateur"}")

        # Standard user menu loop
        while True:

            # Ask which action the user wants to perform
            choice = ask_choice_user()
            match choice:
                case '1':
                    # Display books from a selection chosen by the user
                    selection_choice: str = input("\nQuelle selection souhaitez-vous afficher ?\n")
                    if verify_is_number(selection_choice):
                        selection_choice_int = int(selection_choice)
                        display_book_selection(goncourt.get_books_selection(selection_choice_int), selection_choice_int)
                    else:
                        print("Merci de saisir un chiffre.")
                case '2':
                    # Display selection #1, then show detailed info for a selected book
                    display_book_selection(goncourt.get_books_selection(1), 1)
                    display_book_details(goncourt)
                case '3':
                    # Display votes and the winner for selection #3
                    display_votes_selection(goncourt, 3)
                    display_winner(goncourt)
                case '4':
                    # Exit the user session
                    break

    print("Au revoir")


if __name__ == '__main__':
    main()
