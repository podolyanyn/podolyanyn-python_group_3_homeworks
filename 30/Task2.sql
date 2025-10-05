-- 1. Ім’я та прізвище співробітників з псевдонімами
SELECT first_name AS "Ім'я",
       last_name  AS "Прізвище"
FROM employees;

-- 2. Унікальні ідентифікатори відділів
SELECT DISTINCT department_id
FROM employees;

-- 3. Усі дані про співробітників, відсортовані за ім’ям у порядку спадання
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. Ім’я, прізвище, зарплата і пенсійний фонд (12% від зарплати)
SELECT first_name AS "Ім'я",
       last_name  AS "Прізвище",
       salary,
       ROUND(salary * 0.12, 2) AS "Пенсійний фонд"
FROM employees;

-- 5. Максимальна і мінімальна зарплата
SELECT MAX(salary) AS "Максимальна зарплата",
       MIN(salary) AS "Мінімальна зарплата"
FROM employees;

-- 6. Місячна зарплата (округлено до двох знаків після коми)
SELECT first_name AS "Ім'я",
       last_name  AS "Прізвище",
       ROUND(salary / 12.0, 2) AS "Місячна зарплата"
FROM employees;