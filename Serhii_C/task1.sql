CREATE TABLE kripaks(
    id INT PRIMARY KEY , first_name VARCHAR(100), last_name VARCHAR(100),
    department VARCHAR(100), salary INT);
ALTER TABLE kripaks
ADD column date DATE;

ALTER TABLE kripaks
RENAME column date to hire_date;

ALTER TABLE kripaks
RENAME to new_employee

INSERT INTO new_employee (id, first_name , last_name ,
    department , salary,hire_date ) VALUES (1,'Vasya','Petrenko','IT',
                                            100000,'1991-08-24');


DELETE FROM  new_employee;

DROP TABLE new_employee
drop table kripaks
drop table workers

CREATE TABLE kripaks(
    id INT PRIMARY KEY , first_name VARCHAR(100), last_name VARCHAR(100),
    department VARCHAR(100), salary INT,hire_date DATE);

INSERT INTO kripaks (id, first_name , last_name ,
    department , salary,hire_date ) VALUES (1,'Vasya','Petrenko','IT',
                                            100000,'1991-08-24');

INSERT INTO kripaks (id, first_name , last_name ,
    department , salary,hire_date ) VALUES (2,'Petro','Vaskin','IT',
                                            101000,'1981-07-15');

INSERT INTO kripaks (id, first_name , last_name ,
    department , salary,hire_date ) VALUES (3,'Sasha','Piskin','Sales',
                                            100000,'1992-08-24');

INSERT INTO kripaks (id, first_name , last_name ,
    department , salary,hire_date ) VALUES (4,'Masha','Zopko','Sales',
                                            100000,'1991-08-29');

UPDATE kripaks
SET salary = salary*1.2

DELETE FROM kripaks
WHERE department is not 'IT'

DELETE FROM  kripaks;

DROP TABLE kripaks

create table second_employee(employee_id PRIMARY KEY ,first_name ,last_name ,email ,
phone_number ,hire_date ,job_id ,salary ,commission_pct ,manager_id ,department_id ,Avg_Salary )

insert into second_employee(employee_id ,first_name ,last_name ,email ,
phone_number ,hire_date ,job_id ,salary ,commission_pct ,manager_id ,department_id ,Avg_Salary)
SELECT employee_id ,first_name ,last_name ,email ,
phone_number ,hire_date ,job_id ,salary ,commission_pct ,manager_id ,department_id ,Avg_Salary
from employees

select *
from second_employee
where first_name like 'Alex%'

select*
from second_employee
where salary  between 12000 and 22000


select first_name, last_name,department_id, salary
from second_employee
ORDER BY department_id ASC ,salary  DESC

select first_name, last_name,department_id, salary,job_id
FROM second_employee
WHERE EXISTS(SELECT 1 FROM MIN_SALARY where job_id = second_employee.job_id)
