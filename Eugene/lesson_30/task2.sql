SELECT first_name AS "First name", last_name AS "Last name"
FROM employees;

SELECT DISTINCT department_id
FROM employees;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name, last_name, salary, (salary * 0.12) AS PF
FROM employees;

SELECT MAX(salary) AS "Max salary", MIN(salary) AS "Min salary"
FROM employees;

SELECT first_name, last_name, ROUND(salary / 12, 2) AS "Monthly salary"
FROM employees;