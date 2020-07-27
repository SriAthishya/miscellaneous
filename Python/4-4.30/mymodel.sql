CREATE TABLE employees(emp_no INT(11) PRIMARY KEY, DOB DATE, first_name VARCHAR(14), last_name VARCHAR(16), gender CHAR(1), DOJ DATE);

create table departments(dept_no char(4) primary key,dept_name varchar(40));

CREATE TABLE dept_emp (emp_no VARCHAR (12) REFERENCES employees (emp_no),dept_no CHAR (4) REFERENCES departments (dept_no),
from_date DATE (30),to_date DATE (10));

select * from dept_emp;
