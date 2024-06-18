CREATE DATABASE IF NOT EXISTS News;

USE News;

CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    contents TEXT,
    publication_date DATETIME
);

INSERT INTO main_article(title,content,publication_date) values("Olivier Faure : « Il nous faut sortir de cette mauvaise histoire des gauches irréconciliables »","Le premier secrétaire du Parti socialiste regrette, dans un entretien au « Monde », la non-investiture aux élections législatives de cinq candidats de LFI, qui « dessert » le Nouveau Front populaire. Il rappelle que l’ambition de cette alliance est de rassembler au-delà des partis, en s’ouvrant à la société civile.","2024-06-17 09:51:34");
INSERT INTO main_article(title,content,publication_date) values("Législatives 2024 : « Les amis d’Eric Ciotti » alliés avec le RN, un ensemble hétéroclite où les LR sont minoritaires","Le président des Républicains, allié au Rassemblement national et banni par son camp, a investi 62 candidats, dont moins de la moitié était adhérents LR. La liste mêle d’anciens zemmouristes, des proches de Marion Maréchal, des chroniqueurs de CNews, un porte-parole de Donald Trump en France et une ex-députée macroniste. ","2024-06-17 09:51:34");