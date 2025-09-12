-- Task 1:
-- Створіть таблицю
-- Створіть таблицю на свій вибір у зразку бази даних SQLite,
-- перейменуйте її та додайте новий стовпець.
-- Вставте кілька рядків у вашу таблицю.
-- Також виконайте оператори UPDATE і DELETE для вставлених рядків.
-- Як рішення цього завдання, створіть файл з ім'ям: task1.sql, з усіма операторами SQL, які ви використовували для виконання цього завдання

-- CREATE TABLE Test (
--     ID int PRIMARY KEY,
--     principal real,
--     daily_rate real,
--     months int,
--     start_date date,
--     pay_day int);

-- ALTER TABLE Test RENAME TO Kredit;
-- ALTER TABLE Kredit ADD COLUMN payment real;

-- INSERT INTO Kredit (ID, principal, daily_rate, months, start_date, pay_day, payment)
-- VALUES (1, 10000, 0.08, 12, '2025-09-11', 15, 1000),
--        (2, 12000,0.1, 10, '2025-09-11', 7, 1350),
--        (3, 8500, 0.12, 15, '2025-09-11', 11, 800);
--
-- UPDATE Kredit SET daily_rate = 0.08 WHERE daily_rate = 0.1;
--
-- DELETE FROM Kredit WHERE months = 10;