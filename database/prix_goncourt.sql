-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 11 déc. 2025 à 12:03
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `prix_goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `academy_member`
--

DROP TABLE IF EXISTS `academy_member`;
CREATE TABLE IF NOT EXISTS `academy_member` (
  `id_academy_member` int NOT NULL AUTO_INCREMENT,
  `is_president` tinyint(1) DEFAULT NULL,
  `id_person` int DEFAULT NULL,
  PRIMARY KEY (`id_academy_member`),
  KEY `id_person` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `academy_member`
--

INSERT INTO `academy_member` (`id_academy_member`, `is_president`, `id_person`) VALUES
(1, 1, 16),
(2, 0, 17),
(3, 0, 18),
(4, 0, 19),
(5, 0, 20),
(6, 0, 21),
(7, 0, 22),
(8, 0, 23),
(9, 0, 24),
(10, 0, 25);

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `id_author` int NOT NULL AUTO_INCREMENT,
  `biography` text,
  `id_person` int DEFAULT NULL,
  PRIMARY KEY (`id_author`),
  KEY `id_person` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`id_author`, `biography`, `id_person`) VALUES
(1, 'Nathacha Appanah est née en 1973 aux Seychelles. La nuit au cœur est son dernier roman, explorant les thèmes de la mémoire et de l’exil.', 1),
(2, 'Emmanuel Carrère est né en 1957 à Paris. Kolkhoze est son dernier roman, mêlant histoire familiale et souvenirs personnels.', 2),
(3, 'David Deneufgermain est écrivain et journaliste. L’adieu au visage est son nouveau récit sur le deuil et la mémoire.', 3),
(4, 'David Diop est né en 1966 à Paris. Où s’adosse le ciel explore la migration et l’identité à travers des personnages en quête de reconstruction.', 4),
(5, 'Ghislaine Dunant est auteure suisse. Un amour infini est son dernier roman, une fresque intime sur la passion et les épreuves de l’amour.', 5),
(6, 'Né en 1990, Paul Gasnier est journaliste. La collision est son premier récit, un roman sur le deuil et les fractures sociales.', 6),
(7, 'Yanick Lahens est née en 1953 en Haïti. Passagères de nuit est son dernier roman poétique sur la solitude et la mémoire.', 7),
(8, 'Caroline Lamarche est née en 1955 en Belgique. Le Bel Obscur est son nouveau roman, explorant le passé, la famille et la quête de liberté.', 8),
(9, 'Hélène Laurain est romancière. Tambora est son dernier roman inspiré du volcan Tambora et de ses répercussions sur la vie quotidienne.', 9),
(10, 'Charif Majdalani est né en 1960 au Liban. Le Nom des rois est son dernier roman, une fresque historique et familiale interrogeant le pouvoir et l’héritage.', 10),
(11, 'Laurent Mauvignier est né en 1967 à Tours. La Maison vide explore la mémoire, le deuil et les histoires personnelles d’une famille.', 11),
(12, 'Alfred de Montesquiou est né en 1963 à Paris. Le Crépuscule des hommes est son dernier roman sur les violences et injustices de l’histoire contemporaine.', 12),
(13, 'Guillaume Poix est écrivain. Perpétuité est son dernier récit, une plongée dans le système judiciaire et ses effets sur les individus.', 13),
(14, 'Maria Pourchet est née en 1980. Tressaillir est son dernier roman sur les émotions intenses et les relations humaines.', 14),
(15, 'David Thomas est romancier. Un frère est son dernier récit, un portrait poignant sur le lien fraternel et les conflits personnels.', 15);

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id_book` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `description` text,
  `publication_date` date DEFAULT NULL,
  `pages_nb` int DEFAULT NULL,
  `ISBN` varchar(50) DEFAULT NULL,
  `price` decimal(4,2) DEFAULT NULL,
  `id_editor` int NOT NULL,
  `id_author` int NOT NULL,
  PRIMARY KEY (`id_book`),
  KEY `id_author` (`id_author`),
  KEY `id_editor` (`id_editor`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO `book` (`id_book`, `title`, `description`, `publication_date`, `pages_nb`, `ISBN`, `price`, `id_editor`, `id_author`) VALUES
(1, 'La nuit au cœur', 'Trois femmes victimes de violences conjugales se croisent. Le récit explore leurs parcours, les violences qu’elles ont subies et les liens qui se tissent entre elles, dans une réflexion sur le féminicide et la mémoire intime.', '2025-08-21', 288, '9782073080028', 21.00, 1, 1),
(2, 'Kolkhoze', 'À travers quatre générations, ce roman mêle histoire familiale et souvenirs personnels, retraçant les trajectoires de ceux qui ont connu l’exil, la guerre et les bouleversements de l’Histoire. Un récit dense sur la mémoire et l’héritage.', '2025-08-28', 560, '9782818061985', 24.00, 2, 2),
(3, 'L’adieu au visage', 'Après un amour perdu, un personnage explore les blessures laissées par le deuil et la séparation. Un récit introspectif qui interroge la mémoire, les souvenirs et la reconstruction personnelle.', '2025-08-20', 262, '9782381340647', 21.10, 3, 3),
(4, 'Où s’adosse le ciel', 'Un roman sur la migration et l’identité, suivant plusieurs personnages cherchant à se reconstruire dans un monde en mouvement. Le récit questionne la famille, l’appartenance et la résilience face aux bouleversements.', '2025-08-14', 363, '9782260057307', 22.50, 4, 4),
(5, 'Un amour infini', 'Ce récit intime explore la passion et l’attachement entre deux êtres. L’auteure décrypte les complexités de l’amour et ses épreuves, offrant une fresque sensible sur les relations humaines.', '2025-08-20', 170, '9782226498687', 19.90, 5, 5),
(6, 'La collision', 'En 2012, en plein centre-ville de Lyon, une femme décède brutalement, percutée par un jeune garçon en moto cross qui fait du rodéo urbain à 80 km/h.\nDix ans plus tard, son fils, devenu journaliste, observe comment ce type de drame fracture la société. Il décide de retracer le parcours du motard et les circonstances de l’accident.\nPaul Gasnier révèle deux destins parallèles qui s’ignorent jusqu’au jour où ils se rencontrent, explorant les familles et les manquements collectifs qui rendent l’irréparable possible. Un récit en forme d’enquête littéraire.', '2025-08-21', 160, '9782073101228', 19.00, 1, 6),
(7, 'Passagères de nuit', 'Deux personnages solitaires se croisent dans la nuit. Le roman poétique explore la mémoire, les souvenirs enfouis et les moments d’intimité, tout en décrivant le cheminement intérieur des protagonistes.', '2025-08-28', 223, '9782848055701', 20.00, 6, 7),
(8, 'Le Bel Obscur', 'Une femme revient sur sa vie pour interroger son passé, sa famille et sa sexualité. Le récit aborde la reconstruction personnelle et la quête de liberté à travers une narration introspective.', '2025-08-22', 229, '9782021603439', 20.00, 7, 8),
(9, 'Tambora', 'Inspiré du volcan Tambora, le roman suit plusieurs personnages confrontés aux catastrophes naturelles et à leurs conséquences sur le quotidien, mêlant destin individuel et événements historiques.', '2025-08-28', 192, '9782378562588', 18.50, 8, 9),
(10, 'Le Nom des rois', 'Fresque historique et familiale, le roman explore le pouvoir, l’héritage et le destin des hommes à travers plusieurs générations, tout en interrogeant les dynamiques sociales et politiques.', '2025-08-20', 216, '9782234097278', 20.00, 9, 10),
(11, 'La Maison vide', 'Une maison vide devient le théâtre de souvenirs, d’absences et d’histoires personnelles. Le roman explore la mémoire familiale, les relations complexes et le deuil à travers plusieurs générations.', '2025-08-28', 752, '9782707356741', 25.00, 10, 11),
(12, 'Le Crépuscule des hommes', 'À travers différents personnages, le roman traite des violences et injustices contemporaines, mettant en lumière les fractures sociales et les choix difficiles auxquels sont confrontés les individus.', '2025-08-28', 384, '9782221267660', 22.00, 11, 12),
(13, 'Perpétuité', 'Le récit plonge dans le système judiciaire et ses effets sur la vie des individus. Il interroge la culpabilité, le châtiment et la rédemption, à travers un personnage confronté aux conséquences de ses actes.', '2025-08-21', 336, '9782073105455', 22.00, 12, 13),
(14, 'Tressaillir', 'Le roman explore les émotions intenses et les relations humaines, abordant les tensions quotidiennes, les conflits personnels et la fragilité des liens entre les personnages.', '2025-08-20', 324, '9782234097155', 21.90, 9, 14),
(15, 'Un frère', 'Portrait d’un lien fraternel, le récit aborde la fraternité, la loyauté et les conflits personnels au sein de la famille, offrant une réflexion intime sur les relations fraternelles.', '2025-08-22', 139, '9782823623376', 19.50, 13, 15);

-- --------------------------------------------------------

--
-- Structure de la table `book_selection`
--

DROP TABLE IF EXISTS `book_selection`;
CREATE TABLE IF NOT EXISTS `book_selection` (
  `id_book_selection` int NOT NULL AUTO_INCREMENT,
  `id_selection` int DEFAULT NULL,
  `id_book` int DEFAULT NULL,
  `vote` int DEFAULT '0',
  PRIMARY KEY (`id_book_selection`),
  KEY `id_book` (`id_book`),
  KEY `id_selection` (`id_selection`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `book_selection`
--

INSERT INTO `book_selection` (`id_book_selection`, `id_selection`, `id_book`, `vote`) VALUES
(1, 1, 1, 0),
(2, 1, 2, 0),
(3, 1, 3, 0),
(4, 1, 4, 0),
(5, 1, 5, 0),
(6, 1, 6, 0),
(7, 1, 7, 0),
(8, 1, 8, 0),
(9, 1, 9, 0),
(10, 1, 10, 0),
(11, 1, 11, 0),
(12, 1, 12, 0),
(13, 1, 13, 0),
(14, 1, 14, 0),
(15, 1, 15, 0);

-- --------------------------------------------------------

--
-- Structure de la table `editor`
--

DROP TABLE IF EXISTS `editor`;
CREATE TABLE IF NOT EXISTS `editor` (
  `id_editor` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_editor`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `editor`
--

INSERT INTO `editor` (`id_editor`, `name`) VALUES
(1, 'Gallimard'),
(2, 'P.O.L'),
(3, 'Marchialy'),
(4, 'Julliard'),
(5, 'Albin Michel'),
(6, 'Sabine Wespieser'),
(7, 'Seuil'),
(8, 'Verdier'),
(9, 'Stock'),
(10, 'Les Éditions de Minuit'),
(11, 'Robert Laffont'),
(12, 'Verticales'),
(13, 'L’Olivier');

-- --------------------------------------------------------

--
-- Structure de la table `main_character`
--

DROP TABLE IF EXISTS `main_character`;
CREATE TABLE IF NOT EXISTS `main_character` (
  `id_main_character` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `id_book` int NOT NULL,
  PRIMARY KEY (`id_main_character`),
  KEY `id_book` (`id_book`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `main_character`
--

INSERT INTO `main_character` (`id_main_character`, `name`, `id_book`) VALUES
(1, '3 femmes', 1),
(2, '3 enfants', 2),
(3, 'la mère', 2),
(4, 'un psychiatre', 3),
(5, 'Bilal Seck', 4),
(6, 'Ounifer', 4),
(7, 'un astrophysicien', 5),
(8, 'une mère de famille', 5),
(9, 'une femme', 6),
(10, 'son fils', 6),
(11, 'Elizabeth Dubreuil', 7),
(12, 'Régina', 7),
(13, 'une femme', 8),
(14, 'son mari', 8),
(15, 'une mère', 9),
(16, 'ses 2 filles', 9),
(17, 'l\'auteur', 10),
(18, 'Marguerite', 11),
(19, 'Marie-Ernestine', 11),
(20, 'Le narrateur', 11),
(21, 'Joseph Kessel', 12),
(22, 'Elsa Triolet', 12),
(23, 'Martha Gellhorn', 12),
(24, 'John Dos Passos', 12),
(25, 'Pierre', 13),
(26, 'Houda', 13),
(27, 'Laurent', 13),
(28, 'Maëva', 13),
(29, 'une femme', 14),
(30, 'David', 15),
(31, 'Edouard', 15);

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

DROP TABLE IF EXISTS `person`;
CREATE TABLE IF NOT EXISTS `person` (
  `id_person` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `last_name`, `first_name`) VALUES
(1, 'Appanah', 'Nathacha'),
(2, 'Carrère', 'Emmanuel'),
(3, 'Deneufgermain', 'David'),
(4, 'Diop', 'David'),
(5, 'Dunant', 'Ghislaine'),
(6, 'Gasnier', 'Paul'),
(7, 'Lahens', 'Yanick'),
(8, 'Lamarche', 'Caroline'),
(9, 'Laurain', 'Hélène'),
(10, 'Majdalani', 'Charif'),
(11, 'Mauvignier', 'Laurent'),
(12, 'de Montesquiou', 'Alfred'),
(13, 'Poix', 'Guillaume'),
(14, 'Pourchet', 'Maria'),
(15, 'Thomas', 'David'),
(16, 'Decoin', 'Didier'),
(17, 'Chandernagor', 'Françoise'),
(18, 'Ben Jelloun', 'Tahar'),
(19, 'Assouline', 'Pierre'),
(20, 'Claudel', 'Philippe'),
(21, 'Constant', 'Paule'),
(22, 'Schmitt', 'Éric-Emmanuel'),
(23, 'Laurens', 'Camille'),
(24, 'Bruckner', 'Pascal'),
(25, 'Angot', 'Christine');

-- --------------------------------------------------------

--
-- Structure de la table `selection`
--

DROP TABLE IF EXISTS `selection`;
CREATE TABLE IF NOT EXISTS `selection` (
  `id_selection` int NOT NULL AUTO_INCREMENT,
  `selection_date` date DEFAULT NULL,
  `selection_nb` int DEFAULT NULL,
  PRIMARY KEY (`id_selection`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `selection`
--

INSERT INTO `selection` (`id_selection`, `selection_date`, `selection_nb`) VALUES
(1, '2025-09-03', 1),
(2, '2025-10-07', 2),
(3, '2025-10-28', 3);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `academy_member`
--
ALTER TABLE `academy_member`
  ADD CONSTRAINT `academy_member_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `author`
--
ALTER TABLE `author`
  ADD CONSTRAINT `author_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`id_author`) REFERENCES `author` (`id_author`),
  ADD CONSTRAINT `book_ibfk_2` FOREIGN KEY (`id_editor`) REFERENCES `editor` (`id_editor`);

--
-- Contraintes pour la table `book_selection`
--
ALTER TABLE `book_selection`
  ADD CONSTRAINT `book_selection_ibfk_1` FOREIGN KEY (`id_book`) REFERENCES `book` (`id_book`),
  ADD CONSTRAINT `book_selection_ibfk_2` FOREIGN KEY (`id_selection`) REFERENCES `selection` (`id_selection`);

--
-- Contraintes pour la table `main_character`
--
ALTER TABLE `main_character`
  ADD CONSTRAINT `main_character_ibfk_1` FOREIGN KEY (`id_book`) REFERENCES `book` (`id_book`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
