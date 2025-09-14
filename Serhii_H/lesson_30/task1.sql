CREATE TABLE famous_people
       (name varchar, nickname varchar, birth date, country varchar, occupation varchar, remember varchar);

INSERT INTO famous_people (name, nickname, birth, country, occupation, remember)
VALUES
    ('Charles Darwin', 'gas', '1809-02-12', 'England', 'naturalist', 'origin_of_species'),
    ('Diogenes', 'kyon', null, 'Greek', 'philosopher', 'cynicizm'),
    ('Joanne_Rowling', 'J_K_Rowling', '1965-07-31', 'England', 'author', 'Harry_Potter'),
    ('Leonardo_da_Vinci', 'da_Vinci', '1452-04-15', 'Florence', 'polymath', 'Mona_Lisa'),
    ('William_Shakespeare', 'the_bard', '1564-04-01', 'England', 'playwriter', 'Hamlet'),
    ('Adolf_Hitler', 'fuhrer', '1889-04-20', 'Germany', 'dictator', 'nazism'),
    ('Mikhail_Lermontov', 'mayeux', '1814-10-03', 'russia', 'poet', 'Demon'),
    ('Bohdan_Stupka', 'Sylvester', '1941-08-27', 'Ukraine', 'actor', 'Artist_of_Ukraine'),
    ('Vladimir_Putin', 'huilo', '1952-10-07', 'russia', 'president', 'agressor'),
    ('Volodymyr_Zelenskyy', 'Ze', '1978-01-25', 'Ukraine', 'comedian', 'president');

ALTER TABLE famous_people
RENAME TO people_and_devils;

ALTER TABLE people_and_devils
ADD  self varchar;

INSERT INTO people_and_devils
VALUES ('Albert_Einstein', 'bortze', '1879-03-14', 'Germany', 'physicist', 'relativity', 'man');

INSERT INTO people_and_devils (name, country, occupation, self)
VALUES ('Igor Kateryniuk', 'Ukraine', 'teacher','man');

UPDATE people_and_devils
SET self = 'devil'
WHERE name = 'Adolf_Hitler';

UPDATE people_and_devils
SET self = 'devil'
WHERE name = 'Vladimir_Putin';

DELETE FROM people_and_devils
WHERE name = 'Joanne_Rowling';