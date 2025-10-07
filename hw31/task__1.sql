-- task1.sql
-- 1. Створення таблиці employees
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department_id INTEGER
);

-- 2. Створення таблиці departments
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    depart_name TEXT
);

-- 3. Перейменування стовпця (якщо потрібно)
-- SQLite не підтримує пряме перейменування стовпця у старих версіях
-- Для нових версій можна так:
-- ALTER TABLE departments RENAME COLUMN old_name TO depart_name;

-- 4. Додавання нового стовпця
ALTER TABLE employees ADD COLUMN salary REAL;

-- 5. Вставка даних
INSERT INTO departments (department_id, depart_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(101, 'John', 'Doe', 1, 50000),
(102, 'Jane', 'Smith', 2, 60000),
(103, 'Alice', 'Brown', 3, 55000);

-- 6. Оновлення даних
UPDATE employees
SET salary = salary * 1.1
WHERE department_id = 2;

-- 7. Видалення записів
DELETE FROM employees
WHERE employee_id = 103;

-- 8. Приклад JOIN з правильним стовпцем depart_name
SELECT e.first_name || ' ' || e.last_name AS full_name,
       e.department_id,
       d.depart_name,
       e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id;