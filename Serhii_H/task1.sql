-- Task 1
-- write a query in SQL to display the first name, last name, department number, and department name for each employee

SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees AS e
LEFT JOIN departments AS d
     ON e.department_id = d.department_id;

-- Task 2
-- write a query in SQL to display the first and last name, department, city, and state province for each employee

SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees AS e
LEFT JOIN departments AS d
     ON e.department_id = d.department_id
LEFT JOIN locations AS l
     ON d.location_id = l.location_id;

-- Task 3
-- write a query in SQL to display the first name, last name, department number, and department name,
-- for all employees for departments 80 or 40

SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees AS e
INNER JOIN departments AS d
      ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- Task 4
-- write a query in SQL to display all departments including those where does not have any employee

SELECT d.depart_name, e.first_name, e.last_name
FROM departments AS d
LEFT JOIN employees AS e
     ON d.department_id = e.department_id;

-- Task 5
-- write a query in SQL to display the first name of all employees including the first name of their manager

SELECT e.first_name AS employee, m.first_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
     ON e.manager_id = m.employee_id;

-- Task 6
-- write a query in SQL to display the job title, full name (first and last name ) of the employee,
-- and the difference between the maximum salary for the job and the salary of the employee

SELECT j.job_title,
       e.first_name || ' ' || e.last_name AS full_name,
       (j.max_salary - e.salary) AS diffirence
FROM employees AS e
INNER JOIN jobs AS j
      ON e.job_id = j.job_id;

-- Task 7
-- write a query in SQL to display the job title and the average salary of employees

SELECT j.job_title,
       AVG(e.salary) AS average_salary
FROM employees AS e
JOIN jobs AS j
     ON e.job_id = j.job_id
GROUP BY j.job_title;

-- Task 8
-- write a query in SQL to display the full name (first and last name),
-- and salary of those employees who work in any department located in London

SELECT e.first_name || ' ' || e.last_name AS full_name,
       e.salary
FROM employees AS e
INNER JOIN departments AS d
      ON e.department_id = d.department_id
INNER JOIN locations AS l
      ON d.location_id = l.location_id
WHERE l.city = 'London';

-- Task 9
-- write a query in SQL to display the department name and the number of employees in each department

SELECT d.depart_name,
       COUNT(e.employee_id) AS number_of_employees
FROM departments AS d
LEFT JOIN employees AS e
     ON d.department_id = e.department_id
GROUP BY d.depart_name;