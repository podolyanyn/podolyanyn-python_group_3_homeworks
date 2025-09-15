-- Task 2:
--  Joins
--  Використовуйте зразок бази даних SQLite hr.db (ту саму базу даних, яку ви використовували на попередньому занятті для виконання домашнього завдання)
-- В якості рішення для ДЗ створіть файл з назвою: task1.sql з усіма SQL-запитами:

-- 1. напишіть запит на мові SQL для відображення імені, прізвища, номера відділу та назви відділу для кожного співробітника
-- SELECT first_name, last_name, e.department_id, d.depart_name
-- FROM employees e
--     JOIN departments d ON e.department_id = d.department_id;

-- 2. написати запит на мові SQL, який виводить ім'я та прізвище, відділ, місто та провінцію для кожного співробітника
-- SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
-- FROM employees e
--     JOIN departments d ON e.department_id = d.department_id
--     JOIN locations l ON d.location_id = l.location_id;

-- 3. написати запит на мові SQL, який виводить ім'я, прізвище, номер відділу та назву відділу для всіх співробітників для відділів 80 або 40
-- SELECT first_name, last_name, e.department_id, d.depart_name
-- FROM employees e
--     JOIN departments d ON e.department_id = d.department_id
-- WHERE d.department_id IN (80, 40);

-- 4. написати запит на мові SQL, щоб вивести всі відділи, включаючи ті, в яких немає жодного співробітника
-- SELECT depart_name
-- FROM departments;

-- 5. написати запит на мові SQL для виведення імені всіх співробітників, включаючи ім'я їхнього керівника
-- SELECT e1.first_name, e2.first_name AS manager_first_name
-- FROM employees e1
--     LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;

-- 6. написати запит на мові SQL для виведення назви посади, ПІБ (ім'я та прізвище) працівника, а також різницю між максимальною зарплатою для цієї посади та зарплатою працівника
-- SELECT j.job_title, e.first_name || ' ' || e.last_name AS full_name, (j.max_salary - e.salary) AS delta_salary
-- FROM employees AS e
--     JOIN jobs AS j ON e.job_id = j.job_id;

-- 7. написати запит на мові SQL для виведення назви посади та середньої заробітної плати працівників
-- SELECT j.job_title, avg(e.salary) AS average_salary
-- FROM jobs j
--     JOIN employees e ON j.job_id = e.job_id
-- GROUP BY j.job_title;


-- 8. написати запит на мові SQL, який виводить повне ім'я (ім'я та прізвище) та заробітну плату тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні
-- SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary
-- FROM employees e
--     JOIN departments d ON e.department_id = d.department_id
--     JOIN locations l ON d.location_id = l.location_id
-- WHERE city = 'London';

-- 9. написати запит на мові SQL для виведення назви відділу та кількості працівників у кожному відділі
-- SELECT d.depart_name, COUNT(*) AS count_employees
-- FROM departments AS d
--     JOIN employees AS e ON d.department_id = e.department_id
-- GROUP BY d.depart_name;
