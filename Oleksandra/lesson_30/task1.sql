-- 1. Створення нової таблиці "students"
-- Таблиця містить інформацію про студентів.
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE
);

-- 2. Перейменування таблиці "students" на "university_students"
ALTER TABLE students RENAME TO university_students;

-- 3. Додавання нового стовпця "enrollment_date"
ALTER TABLE university_students ADD COLUMN enrollment_date TEXT;

-- 4. Вставка декількох рядків у таблицю
INSERT INTO university_students (first_name, last_name, email, enrollment_date)
VALUES
    ('Ivan', 'Petrov', 'ivan.petrov@example.com', '2022-09-01'),
    ('Maria', 'Sydorenko', 'maria.sydorenko@example.com', '2023-09-01'),
    ('Ivan', 'Petrenko', 'ivan.petrenko@example.com', '2024-09-10'),
    ('Volodimer', 'Kosubenko', 'volodimer.kosubenko@example.com', '2024-10-10');

-- 5. Оновлення даних у рядку
-- Змінюємо прізвище студента з ID 1 на "Ivanov"
UPDATE university_students
SET last_name = 'Ivanov'
WHERE student_id = 1;

-- 6. Видалення рядка
-- Видаляємо студента з ID 2
DELETE FROM university_students
WHERE student_id = 2;

-- 7. Перевірка результату
SELECT * FROM university_students;