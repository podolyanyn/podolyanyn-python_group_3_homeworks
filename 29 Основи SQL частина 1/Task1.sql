-- 1. Створення таблиці customers
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
);

-- 2. Перейменування таблиці на clients
ALTER TABLE customers RENAME TO clients;

-- 3. Додавання нового стовпця email
ALTER TABLE clients ADD COLUMN email TEXT;

-- 4. Вставка кількох рядків
INSERT INTO clients (name, age, email) VALUES ('IGOR',  32, 'igor@example.com');
INSERT INTO clients (name, age, email) VALUES ('Nazar', 25, 'nazar@example.com');
INSERT INTO clients (name, age, email) VALUES ('Petro', 40, 'petro@example.com');

-- 5. Оновлення даних
UPDATE clients SET age = 31 WHERE name = 'Igor';

-- 6. Видалення рядка
DELETE FROM clients WHERE name = 'Nazar';

-- 7. Перевірка даних
SELECT * FROM clients;
