--Завдання 1

--Об'єднання

--Використовуйте зразок бази даних SQLite hr.db (ту саму базу даних, яку ви використовували
-- в попередньому уроці для домашніх завдань)

--Як рішення для HW, створіть файл з назвою: task1.sql з усіма SQL-запитами:

--напишіть запит на SQL для відображення імені, прізвища,номера відділу та назви відділу для кожного співробітника
SELECT e.first_name || ' ' || e.last_name as full_name,e.department_id,d.depart_name FROM employees AS e
     JOIN departments AS d
    ON e.department_id=d.department_id;
--напишіть запит на SQL для відображення імені та прізвища, відділу, міста та штату, області для кожного співробітника
SELECT e.first_name || ' ' || e.last_name as full_name,d.depart_name,l.city,l.state_province FROM test_employees AS e
JOIN
test_departments as d on e.department_id = d.department_id
JOIN test_locations as l on d.location_id = l.location_id;
--напишіть запит на SQL для відображення імені, прізвища, номера відділу та назви відділу для всіх співробітників для відділів 80 або 40
SELECT e.first_name || ' ' || e.last_name as full_name,e.department_id,d.depart_name FROM test_employees AS e
JOIN test_departments as d on e.department_id = d.department_id
WHERE e.department_id = 80 or e.department_id = 40;
--напишіть запит на SQL для відображення всіх відділів, включаючи ті, де немає жодного співробітника
SELECT d.depart_name, e.first_name || ' ' || e.last_name AS full_name FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id;



--напишіть запит на SQL для відображення імені всіх співробітників, включаючи ім'я їхнього керівника

SELECT e.first_name || ' ' || e.last_name as full_name,e.manager_id, d.first_name || ' ' || d.last_name as full_boss_name FROM test_employees as e
JOIN test_employees as d on d.employee_id= e.manager_id;



--напишіть запит на SQL для відображення посади, повного імені (ім'я та прізвище) співробітника та різниці між максимальною зарплатою для посади та зарплатою співробітника
SELECT j.job_id,j.job_title,e.first_name || ' ' || e.last_name as full_name,j.max_salary-e.salary FROM test_jobs as j
join test_employees as e on j.job_id = e.job_id
GROUP BY e.job_id
;

--напишіть запит на SQL для відображення посади та середньої зарплати співробітників
SELECT j.job_id ,AVG(e.salary)
FROM test_jobs AS j
join test_employees as e on j.job_id = e.job_id
group by e.job_id;
--напишіть запит на SQL для відображення повне ім'я (ім'я та прізвище), а також зарплата тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні
SELECT e.first_name || ' ' || e.last_name as full_name, e.salary,e.department_id FROM test_employees AS e
JOIN test_departments as d on e.department_id = d.department_id
WHERE d.location_id=2400;


--написати запит у SQL для відображення назви відділу та кількості співробітників у кожному відділі
SELECT d.depart_name ,COUNT(e.department_id)
FROM test_departments AS d
join test_employees as e on d.department_id = e.department_id
group by e.department_id

