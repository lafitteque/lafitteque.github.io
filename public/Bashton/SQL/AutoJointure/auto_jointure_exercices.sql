CREATE TABLE employe (
  id INT PRIMARY KEY,
  nom VARCHAR(100),
  prenom VARCHAR(100),
  salaire INT,
  superieur INT,
  FOREIGN KEY (superieur) REFERENCES employe(id)
);

INSERT INTO employe (id, nom, prenom, salaire, superieur) VALUES
(1, 'MARIN', 'Marie', 5042, 1),   -- chef se réfère à lui-même
(2, 'RENIN', 'Étienne', 3755, 1),
(3, 'DUCHENE', 'Guillaume', 2780, 2),
(4, 'MADOVIE', 'Guy', 2930, 2),
(5, 'PALTRUC', 'Lucie', 2880, 2),
(6, 'LEMEUR', 'Sophie', 3200, 6),
(7, 'BOUCHET', 'Alain', 2800, 6),
(8, 'GUILLOU', 'Anne', 2900, 6),
(9, 'DUBOIS', 'Karine', 3300, 9),
(10, 'LE GALL', 'Jean', 3000, 9),
(11, 'MOREAU', 'Claire', 3100, 9),
(12, 'LEROY', 'Paul', 3500, 12),
(13, 'GARNIER', 'Isabelle', 2900, 12),
(14, 'FONTAINE', 'Marc', 3050, 12),
(15, 'LE GUEVEL', 'Nathalie', 3400, 15),
(16, 'THOMAS', 'Pierre', 2950, 15),
(17, 'ROUSSEL', 'Sophie', 3000, 15);
