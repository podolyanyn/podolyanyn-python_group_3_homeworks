-- 1. Запит для відображення імен (first_name, last_name) з псевдонімами "First Name" та "Last Name".
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- 2. Запит для отримання унікальних ідентифікаторів відділів (department_id) з таблиці працівників.
SELECT DISTINCT department_id
FROM employees;

-- 3. Запит для отримання всіх даних про працівників, відсортованих за іменем (first_name) у спадному порядку.
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. Запит для отримання імен, зарплати та PF (пенсійний фонд, 12% від зарплати) для всіх працівників.
SELECT first_name, last_name, salary, salary * 0.12 AS PF
FROM employees;

-- 5. Запит для отримання максимальної та мінімальної зарплати з таблиці працівників.
SELECT MAX(salary) AS maximum_salary, MIN(salary) AS minimum_salary
FROM employees;

-- 6. Запит для отримання щомісячної зарплати (округленої до 2 знаків після коми) для кожного працівника.
SELECT first_name, last_name, ROUND(CAST(salary / 12.0 AS REAL), 2) AS monthly_salary
FROM employees;
