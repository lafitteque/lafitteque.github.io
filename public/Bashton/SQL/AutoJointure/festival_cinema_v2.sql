-- Création des tables
CREATE TABLE realisateur (id INT PRIMARY KEY, nom VARCHAR(100), prenom VARCHAR(100), annee_naissance INT);
CREATE TABLE film (id INT PRIMARY KEY, titre VARCHAR(255), id_realisateur INT, remake_de INT, annee_sortie INT, note FLOAT, FOREIGN KEY(id_realisateur) REFERENCES realisateur(id), FOREIGN KEY(remake_de) REFERENCES film(id));
CREATE TABLE salle (id INT PRIMARY KEY, prix INT, nb_places INT);
CREATE TABLE programmation (
    id_film INT, 
    id_salle INT, 
    creneau INT,
    PRIMARY KEY (id_film, id_salle, creneau),
    FOREIGN KEY(id_film) REFERENCES film(id), 
    FOREIGN KEY(id_salle) REFERENCES salle(id)
    );

-- Insertion des réalisateurs
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (1, 'Delacruz', 'Jacob', 1973);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (2, 'Harrison', 'Victoria', 1941);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (3, 'Gomez', 'Keith', 1967);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (4, 'Cox', 'Timothy', 1975);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (5, 'Romero', 'Sherri', 1956);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (6, 'Graham', 'Teresa', 1954);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (7, 'Miller', 'Kristin', 1985);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (8, 'Smith', 'Jason', 1958);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (9, 'Jordan', 'Rachel', 1983);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (10, 'Weeks', 'Steve', 1954);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (11, 'Oneal', 'Amber', 1952);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (12, 'Love', 'Tina', 1952);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (13, 'Santos', 'Stephanie', 1946);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (14, 'Powell', 'Brendan', 1959);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (15, 'Moore', 'Mathew', 1961);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (16, 'Smith', 'Brittney', 1963);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (17, 'Smith', 'Denise', 1955);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (18, 'Guzman', 'Jason', 1977);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (19, 'Love', 'Scott', 1961);
INSERT INTO realisateur (id, nom, prenom, annee_naissance) VALUES (20, 'Bailey', 'Rebecca', 1968);

-- Insertion des films
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (1, 'Balle perdue', 19, 2020, 4.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (2, 'Local tour', 18, 2007, 4.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (3, 'Une classe sans nom', 9, 1986, 2.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (4, 'Le bouc chauve', 20, 2010, 4.0, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (5, 'Born to die', 10, 2012, 2.7, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (6, 'Living pool', 3, 2015, 4.6);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (7, 'Au coin de la fournaise', 4, 2000, 2.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (8, 'Election day', 19, 1995, 3.6, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (9, 'Lady walf', 10, 2020, 3.6, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (10, 'Born to die again', 8, 1982, 2.2, 5);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (11, 'Iron arm', 13, 2021, 4.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (12, 'Y-Women', 5, 2001, 2.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (13, 'Versus plus', 15, 2022, 3.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (14, 'Le tout venant', 3, 2013, 2.9, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (15, 'Faire le beau', 5, 2020, 4.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (16, 'Ouaf ouaf', 9, 1995, 4.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (17, 'Le spectacle', 3, 1988, 3.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (18, 'Surréel', 11, 1990, 4.0, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (19, 'Hot dogs', 4, 1998, 4.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (20, 'Miami 68', 10, 1980, 2.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (21, 'Air Force 11', 10, 2006, 2.4, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (22, 'Rimbaut 2', 19, 2011, 2.2, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (23, 'Inaction Man - Le film', 11, 2019, 2.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (24, 'Amour fulgurant', 15, 2003, 2.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (25, 'Night and Day', 2, 1987, 2.9, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (26, 'The legend of Marmia', 1, 1986, 2.2, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (27, 'Miami 68 - Remake', 17, 1983, 4.2, 20);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (28, 'Across the board', 15, 1983, 2.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (29, 'Education weapon', 7, 1991, 2.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (30, 'Le suricate', 1, 2020, 2.7, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (31, 'Zombies vs. chiens', 12, 2006, 2.9, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (32, 'La ville de la terreur', 4, 2004, 2.7, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (33, 'Les quatres soeurs', 3, 1983, 3.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (34, 'Science for all', 17, 2019, 3.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (35, 'Zombies vs. chiens - Remake', 4, 2009, 3.3, 31);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (36, 'Small city, big trouble', 4, 2020, 2.3, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (37, 'Enemy number one', 10, 2001, 2.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (38, 'Land lord', 18, 2007, 3.4, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (39, 'The thingy', 5, 1990, 3.6, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (40, 'Almost poor', 5, 1980, 3.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (41, 'The safe place', 16, 2009, 3.9, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (42, 'Public enemy', 9, 2013, 2.8, 37);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (43, 'Meet me', 13, 2023, 3.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (44, 'John Lemon - Acid life', 6, 1997, 2.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (45, 'The base of data', 15, 2004, 3.6, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (46, 'The quad tree', 8, 1987, 2.8, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (47, 'Hanoy towers', 16, 2004, 2.1, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (48, 'Call myself', 15, 2020, 3.5, null);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (49, 'Recursive call', 6, 2008, 2.7, 48);
INSERT INTO film (id, titre, id_realisateur, annee_sortie, note, remake_de) VALUES (50, 'Object oriented', 7, 2005, 4.6, null);

-- Insertion des salles
INSERT INTO salle (id, prix, nb_places) VALUES (1, 12, 150);
INSERT INTO salle (id, prix, nb_places) VALUES (2, 15, 150);
INSERT INTO salle (id, prix, nb_places) VALUES (3, 9, 200);
INSERT INTO salle (id, prix, nb_places) VALUES (4, 13, 100);
INSERT INTO salle (id, prix, nb_places) VALUES (5, 10, 50);
INSERT INTO salle (id, prix, nb_places) VALUES (6, 7, 250);
INSERT INTO salle (id, prix, nb_places) VALUES (7, 15, 50);
INSERT INTO salle (id, prix, nb_places) VALUES (8, 14, 120);
INSERT INTO salle (id, prix, nb_places) VALUES (9, 15, 200);
INSERT INTO salle (id, prix, nb_places) VALUES (10, 14, 120);

-- Insertion des programmations
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (33, 10, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (45, 7, 3);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (25, 1, 2);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (15, 8, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (3, 8, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (5, 3, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (47, 1, 3);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (14, 7, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (40, 10, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (20, 2, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (16, 5, 4);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (35, 6, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (46, 10, 2);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (34, 1, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (1, 5, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (15, 8, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (6, 10, 4);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (6, 4, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (32, 9, 4);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (24, 8, 2);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (34, 5, 3);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (39, 6, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (11, 6, 14);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (39, 2, 2);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (18, 9, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (1, 9, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (41, 10, 14);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (24, 1, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (31, 5, 14);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (48, 1, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (23, 10, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (34, 7, 1);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (5, 8, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (16, 4, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (44, 2, 4);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (38, 4, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (29, 1, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (17, 8, 3);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (27, 10, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (22, 9, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (6, 6, 11);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (39, 6, 13);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (38, 3, 3);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (5, 1, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (25, 8, 14);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (23, 9, 14);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (38, 3, 4);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (11, 3, 12);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (48, 6, 2);
INSERT INTO programmation (id_film, id_salle, creneau) VALUES (6, 1, 3);