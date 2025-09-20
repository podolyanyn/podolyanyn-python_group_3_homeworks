--  =============================================================================   TASK 1
-- SELECT first_name, last_name, employees.department_id, departments.depart_name FROM employees
--     JOIN departments ON employees.department_id=departments.department_id;

--  =============================================================================   TASK 2
-- SELECT e.first_name, e.last_name, d.depart_name, l.city FROM employees AS e JOIN departments as d JOIN locations as l
--     ON e.department_id=d.department_id AND d.location_id=l.location_id;

--  =============================================================================   TASK 3
-- SELECT first_name, last_name, employees.department_id, departments.depart_name
--     FROM employees
--     JOIN departments ON employees.department_id=departments.department_id
--         WHERE employees.department_id=40 or employees.department_id=80;

--  =============================================================================   TASK 4
-- SELECT d.department_id, d.depart_name FROM departments as d
--     LEFT JOIN employees ON employees.department_id = d.department_id
--         WHERE employees.employee_id IS NULL;


--  =============================================================================   TASK 5
-- SELECT e.first_name AS employee_firstname, managers.first_name AS managers_firstname FROM employees as e
--     JOIN employees AS managers
--         ON e.manager_id = managers.employee_id;

--  =============================================================================   TASK 6

-- SELECT
--     e.first_name || ' ' || e.last_name AS full_name,
--     j.job_title,
--     j.max_salary - e.salary AS salary_difference
--     FROM employees AS e
--     JOIN jobs as j
--         ON e.job_id=j.job_id;

--  =============================================================================   TASK 7
-- SELECT j.job_title, AVG(e.salary) AS average_salary FROM employees as e
--     JOIN jobs AS j
--         ON e.job_id = j.job_id
--         GROUP BY j.job_title;


--  =============================================================================   TASK 8
-- SELECT
--     e.first_name || ' ' || e.last_name as full_name,
--     e.salary
--     FROM employees as e
--     JOIN departments as d ON e.department_id = d.department_id
--     JOIN locations as l ON d.location_id = l.location_id
--         WHERE l.city='London';

--  =============================================================================   TASK 9
-- SELECT d.depart_name, COUNT(e.first_name) as employees_count FROM departments as d
--     JOIN employees as e ON e.department_id = d.department_id
--     GROUP BY d.depart_name;



