# Application Prix Goncourt

Il s'agit d'une application Python conçue pour gérer et suivre les sélections du Prix Goncourt et leurs votes. Elle permet la gestion des membres de l'académie, des livres, des auteurs et des sélections. L'application peut être utilisée par le président de l'académie ainsi que les membres réguliers.

---

## Fonctionnalités

- **Gestion des membres de l'académie** : Afficher la liste des membres de l'académie et vérifier si une personne est un membre ou le président.
- **Gestion des livres** : Ajouter des livres à une sélection, afficher les détails des livres et afficher les sélections de livres.
- **Votes** : Enregistrer les votes pour chaque livre d'une sélection et afficher les résultats.
- **Gestion des sélections** : Voir les livres d'une sélection donnée et gérer les livres sélectionnés pour chaque tour.
- **Affichage du gagnant** : Afficher le gagnant d'une sélection basé sur les votes.

---

## Prérequis

- Python 3.x
- Base de données MySQL (configurée pour l'application)

---

## Installation

Pour configurer et exécuter l'application, suivez les étapes ci-dessous.

### 1. Clonez le dépôt

```bash
git clone https://github.com/AmandineGrardLaurent/prix_goncourt.git
cd prix_goncourt
```

### 2. Installez les dépendances

Assurez-vous d'avoir Python 3.x installé, puis installez les packages requis :

```bash
pip install -r requirements.txt

```

### 3. Configurez la base de données

Assurez-vous d'avoir une base de données MySQL configurée avec les informations suivantes :

Hôte : localhost

Utilisateur : prix_goncourt

Mot de passe : ******

Base de données : prix_goncourt

Vous pouvez ajuster ces informations dans la classe Dao si nécessaire.

### 4. Exécutez l'application

Une fois tout configuré, lancez le fichier principal Python :

```bash
python main.py
```

L'application vous demandera d'entrer votre nom, et en fonction de votre rôle (président ou membre), vous pourrez effectuer différentes actions.

---

## Utilisation

#### Pour le Président :

1. Afficher la liste des académiciens : Voir les noms de tous les membres de l'académie.

2. Afficher les livres d'une sélection : Voir les livres sélectionnés pour une sélection donnée.

3. Afficher les résultats des votes : Voir combien de votes chaque livre a reçu pour la sélection n°3 et déterminer le gagnant.

4. Ajouter des livres à une sélection : Ajouter des livres à une nouvelle sélection.

5. Ajouter les votes d'une sélection : Enregistrer les votes pour les livres de la sélection n°3.

#### Pour les Utilisateurs (Membres de l'Académie) :

1. Afficher les livres d'une sélection : Voir les livres sélectionnés pour une sélection donnée.

2. Voir les détails d'un livre : Voir des informations détaillées sur un livre spécifique.

3. Voir les résultats des votes et le gagnant : Vérifier les résultats des votes pour la sélection n°3 et voir quel livre a gagné.

---

## Schéma de la Base de Données

L'application utilise une base de données relationnelle pour stocker les informations relatives aux livres, aux membres de l'académie, aux auteurs, et aux sélections. Voici un aperçu des principales tables et de leur relation :

### Tables principales

1. **`person`**
   - Contient les informations personnelles des membres de l'académie et des auteurs.
   - **Colonnes** :
     - `id_person` (PK) : Identifiant unique de la personne.
     - `first_name` : Prénom de la personne.
     - `last_name` : Nom de la personne.

2. **`academy_member`**
   - Contient les informations des membres de l'académie.
   - **Colonnes** :
     - `id_academy_member` (PK) : Identifiant unique du membre de l'académie.
     - `id_person` (FK) : Référence à `person.id_person`.
     - `is_president` : Booléen qui indique si le membre est le président.

3. **`author`**
   - Contient des informations spécifiques aux auteurs.
   - **Colonnes** :
     - `id_author` (PK) : Identifiant unique de l'auteur.
     - `id_person` (FK) : Référence à `person.id_person`.
     - `biography` : Biographie de l'auteur.

4. **`book`**
   - Contient des informations sur les livres.
   - **Colonnes** :
     - `id_book` (PK) : Identifiant unique du livre.
     - `title` : Titre du livre.
     - `description` : Résumé du livre.
     - `publication_date` : Date de publication du livre.
     - `pages_nb` : Nombre de pages du livre.
     - `ISBN` : Numéro ISBN du livre.
     - `price` : Prix du livre.
     - `id_author` (FK) : Référence à `author.id_author`.
     - `id_editor` (FK) : Référence à `editor.id_editor`.

5. **`editor`**
   - Contient des informations sur les éditeurs.
   - **Colonnes** :
     - `id_editor` (PK) : Identifiant unique de l'éditeur.
     - `name` : Nom de l'éditeur.

6. **`main_character`**
   - Contient les personnages principaux des livres.
   - **Colonnes** :
     - `id_main_character` (PK) : Identifiant unique du personnage principal.
     - `id_book` (FK) : Référence à `book.id_book`.
     - `name` : Nom du personnage principal.

7. **`book_selection`**
   - Table de liaison entre les livres et les sélections, avec un champ pour les votes.
   - **Colonnes** :
     - `id_book` (FK) : Référence à `book.id_book`.
     - `id_selection` (FK) : Référence à `selection.id_selection`.
     - `vote` : Nombre de votes pour le livre dans cette sélection.

8. **`selection`**
   - Contient les informations relatives aux sélections du Prix Goncourt.
   - **Colonnes** :
     - `id_selection` (PK) : Identifiant unique de la sélection.
     - `date` : Date de la sélection.
     - `selection_nb` : Numéro de la sélection (ex: 1 pour la première, 2 pour la deuxième, etc.).

### Relations entre les tables

- **`academy_member`** est lié à **`person`** via `id_person`.
- **`author`** est lié à **`person`** via `id_person`.
- **`book`** est lié à **`author`** via `id_author` et à **`editor`** via `id_editor`.
- **`book_selection`** est une table de liaison entre **`book`** et **`selection`**, indiquant quels livres sont présents dans quelles sélections et les votes correspondants.
- **`main_character`** est lié à **`book`** via `id_book`, et chaque livre peut avoir plusieurs personnages principaux.
  
---

## Exemple d'Interaction

### Affichage du menu 

Lors de l'exécution de l'application, l'utilisateur interagira avec des menus permettant de sélectionner diverses options selon son rôle (président ou membre de l'académie). Voici un exemple d'interaction avec l'application :

```bash
Entrez votre nom :
> Alice Dupont

Que voulez-vous faire ?
[1] afficher la liste des académiciens
[2] afficher la liste des livres d'une sélection
[3] afficher les votes de la sélection n°3 et le lauréat
[4] afficher les détails d'un livre
[5] ajouter la liste des livres retenus lors d'une sélection
[6] ajouter les votes de la sélection n°3
[7] session terminée
```
En fonction de l'entrée de l'utilisateur, le système exécutera la fonction appropriée. Par exemple, le président pourra ajouter des livres à une sélection, tandis qu'un membre de l'académie pourra consulter les détails d'un livre ou vérifier les votes.

### Affichage des détails d'un livre

1. Demande de l'ID du livre :

L'application invite l'utilisateur à entrer l'ID du livre qu'il souhaite consulter.

```
Quel livre souhaitez-vous consulter ?
```
2. L'utilisateur entre l'ID du livre (par exemple, 12):

L'utilisateur saisit un ID de livre, par exemple, 12.

3. Résultat affiché dans la console :

```
Informations du livre "Le Nom du Vent" :
- Titre : Le Nom du Vent
- Résumé : Un jeune homme nommé Kvothe raconte son histoire d'apprentissage et ses aventures, à la fois magiques et dangereuses, dans un monde où la musique, la magie et les créatures mythologiques sont omniprésentes.
- Personnage(s) principal(aux) : Kvothe, Denna
- Date de publication : 2007-03-27
- Nombre de pages : 800
- ISBN : 978-2-7548-0207-3
- Prix : 19.99 euros
- Editeur: Le Livre de Poche
- Auteur: Patrick Rothfuss
```





**Réalisé par : Amandine Grard-Laurent**