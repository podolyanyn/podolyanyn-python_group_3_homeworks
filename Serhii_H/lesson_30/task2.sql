-- write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
-- write a query to get the unique department ID from the employee table
-- write a query to get all employee details from the employee table ordered by first name, descending
-- write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
-- write a query to get the maximum and minimum salary from the employees table
-- write a query to get a monthly salary (round 2 decimal places) of each and every employee


SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;


SELECT DISTINCT department_id
FROM employees;


SELECT *
FROM employees
ORDER BY first_name DESC;


SELECT
    first_name || ' ' || last_name AS Name,
    salary,
    salary * 0.12 AS PF
FROM employees;


SELECT MAX(salary) AS max_salary,
       MIN(salary) AS min_salary
FROM employees;


SELECT first_name || ' ' || last_name AS Name,
    ROUND(salary / 12.0, 2) AS monthly_salary
FROM employees;