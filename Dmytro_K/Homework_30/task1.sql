CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL
);

ALTER TABLE employees RENAME TO staff;

ALTER TABLE staff ADD COLUMN salary INTEGER;

INSERT INTO staff (name, position, salary) VALUES ('Іван', 'Менеджер', 12000);
INSERT INTO staff (name, position, salary) VALUES ('Олена', 'Аналітик', 15000);
INSERT INTO staff (name, position, salary) VALUES ('Петро', 'Розробник', 18000);

UPDATE staff SET salary = 16000 WHERE name = 'Олена';

DELETE FROM staff WHERE name = 'Петро';

