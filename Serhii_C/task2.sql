--Як рішення для апаратного забезпечення, створіть файл з назвою: task2.sql з усіма SQL-запитами:
--апишіть запит для відображення імен (ім'я, прізвище) з використанням псевдонімів "Ім'я",
-- "Прізвище" з таблиці співробітників;

select first_name, last_name
from second_employee
--напишіть запит для отримання унікального ідентифікатора відділу з таблиці співробітників;
select DISTINCT department_id
from second_employee
ORDER BY department_id ASC;
--напишіть запит для отримання всіх відомостей про співробітників з таблиці співробітників, відсортованих за іменем, за спаданням;
SELECT *
FROM second_employee
ORDER BY first_name DESC;
--напишіть запит для отримання імен (ім'я, прізвище), зарплати, пенсійного фонду всіх співробітників (пенсійний фонд розраховується як 12% від зарплати);
SELECT first_name,last_name,salary,salary*0.12 AS Pension_Fund
from second_employee;
--напишіть запит для отримання максимальної та мінімальної зарплати з таблиці співробітників;
SELECT MAX(salary) as max_salary,min(salary) as min_salary
from second_employee;
--напишіть запит для отримання місячної зарплати (округлення до 2 знаків після коми) кожного співробітника.
SELECT first_name,last_name,round(salary/12,2) as month_salary
FROM second_employee