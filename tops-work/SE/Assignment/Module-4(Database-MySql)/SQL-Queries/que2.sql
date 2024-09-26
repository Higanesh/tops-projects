/*
Que2. Create table given below: Employee and IncentiveTable
*/

--1. Create table query for Employee table

mysql> create table Employee (
    -> Employee_id int primary key auto_increment,
    -> First_name varchar(20),
    -> Last_name varchar(20),
    -> Salary varchar(20),
    -> Joining_date varchar(20),
    -> Department varchar(20)
    -> );

--O/P

mysql> describe employee;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| Employee_id  | int(11)     | NO   | PRI | NULL    | auto_increment |
| First_name   | varchar(20) | YES  |     | NULL    |                |
| Last_name    | varchar(20) | YES  |     | NULL    |                |
| Salary       | varchar(20) | YES  |     | NULL    |                |
| Joining_date | varchar(20) | YES  |     | NULL    |                |
| Department   | varchar(20) | YES  |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+

mysql> select * from employee;
+-------------+------------+-----------+---------+-----------------------+------------+
| Employee_id | First_name | Last_name | Salary  | Joining_date          | Department |
+-------------+------------+-----------+---------+-----------------------+------------+
|           1 | John       | Abraham   | 1000000 | 01-JAN-13 12:00:00 AM | Banking    |
|           2 | Michael    | Clarke    | 800000  | 01-JAN-13 12:00:00 AM | Insurance  |
|           3 | Roy        | Thomas    | 700000  | 01-FEB-13 12:00:00 AM | Banking    |
|           4 | Tom        | Jose      | 600000  | 01-FEB-13 12:00:00 AM | Insurance  |
|           5 | Jerry      | Pinto     | 650000  | 01-JAN-13 12:00:00 AM | Insurance  |
|           6 | Philip     | Mathew    | 750000  | 01-JAN-13 12:00:00 AM | Services   |
|           7 | TestName1  | 123       | 650000  | 01-JAN-13 12:00:00 AM | Services   |
|           8 | TestName2  | Lname%    | 600000  | 01-FEB-13 12:00:00 AM | Insurance  |
+-------------+------------+-----------+---------+-----------------------+------------+
-----------------------------------------------------------------------------------------------
--2. Create table query for Incentive table

mysql> create table Incentive (
    -> Employee_ref_id int,
    -> Incentive_date varchar(20),
    -> Incentive_amount varchar(20),
    -> FOREIGN KEY (Employee_ref_id) REFERENCES employee(Employee_id)
    -> );

--O/P

mysql> describe incentive;
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| Employee_ref_id  | int(11)     | YES  | MUL | NULL    |       |
| Incentive_date   | varchar(20) | YES  |     | NULL    |       |
| Incentive_amount | varchar(20) | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+

mysql> select * from incentive;
+-----------------+----------------+------------------+
| Employee_ref_id | Incentive_date | Incentive_amount |
+-----------------+----------------+------------------+
|               1 | 01-FEB-13      | 5000             |
|               2 | 01-FEB-13      | 3000             |
|               3 | 01-FEB-13      | 4000             |
|               1 | 01-JAN-13      | 4500             |
|               2 | 01-JAN-13      | 3500             |
+-----------------+----------------+------------------+

--3. Get First_Name from employee table using Tom name “Employee Name”.

mysql> select First_name as Employee_name from employee where First_name = "Tom";
+---------------+
| Employee_name |
+---------------+
| Tom           |
+---------------+

--4. Get FIRST_NAME, Joining Date, and Salary from employee table.

mysql> select First_name,Joining_date,Salary from employee;
+------------+-----------------------+---------+
| First_name | Joining_date          | Salary  |
+------------+-----------------------+---------+
| John       | 01-JAN-13 12:00:00 AM | 1000000 |
| Michael    | 01-JAN-13 12:00:00 AM | 800000  |
| Roy        | 01-FEB-13 12:00:00 AM | 700000  |
| Tom        | 01-FEB-13 12:00:00 AM | 600000  |
| Jerry      | 01-JAN-13 12:00:00 AM | 650000  |
| Philip     | 01-JAN-13 12:00:00 AM | 750000  |
| TestName1  | 01-JAN-13 12:00:00 AM | 650000  |
| TestName2  | 01-FEB-13 12:00:00 AM | 600000  |
+------------+-----------------------+---------+

--5. Get all employee details from the employee table order by First_Name Ascending and Salary descending?

mysql> select * from employee order by First_name Asc;
+-------------+------------+-----------+---------+-----------------------+------------+
| Employee_id | First_name | Last_name | Salary  | Joining_date          | Department |
+-------------+------------+-----------+---------+-----------------------+------------+
|           5 | Jerry      | Pinto     | 650000  | 01-JAN-13 12:00:00 AM | Insurance  |
|           1 | John       | Abraham   | 1000000 | 01-JAN-13 12:00:00 AM | Banking    |
|           2 | Michael    | Clarke    | 800000  | 01-JAN-13 12:00:00 AM | Insurance  |
|           6 | Philip     | Mathew    | 750000  | 01-JAN-13 12:00:00 AM | Services   |
|           3 | Roy        | Thomas    | 700000  | 01-FEB-13 12:00:00 AM | Banking    |
|           7 | TestName1  | 123       | 650000  | 01-JAN-13 12:00:00 AM | Services   |
|           8 | TestName2  | Lname%    | 600000  | 01-FEB-13 12:00:00 AM | Insurance  |
|           4 | Tom        | Jose      | 600000  | 01-FEB-13 12:00:00 AM | Insurance  |
+-------------+------------+-----------+---------+-----------------------+------------+

mysql> select * from employee order by Salary desc;
+-------------+------------+-----------+---------+-----------------------+------------+
| Employee_id | First_name | Last_name | Salary  | Joining_date          | Department |
+-------------+------------+-----------+---------+-----------------------+------------+
|           1 | John       | Abraham   | 1000000 | 01-JAN-13 12:00:00 AM | Banking    |
|           2 | Michael    | Clarke    |  800000 | 01-JAN-13 12:00:00 AM | Insurance  |
|           6 | Philip     | Mathew    |  750000 | 01-JAN-13 12:00:00 AM | Services   |
|           3 | Roy        | Thomas    |  700000 | 01-FEB-13 12:00:00 AM | Banking    |
|           5 | Jerry      | Pinto     |  650000 | 01-JAN-13 12:00:00 AM | Insurance  |
|           7 | TestName1  | 123       |  650000 | 01-JAN-13 12:00:00 AM | Services   |
|           4 | Tom        | Jose      |  600000 | 01-FEB-13 12:00:00 AM | Insurance  |
|           8 | TestName2  | Lname%    |  600000 | 01-FEB-13 12:00:00 AM | Insurance  |
+-------------+------------+-----------+---------+-----------------------+------------+

--6. Get employee details from employee table whose first name contains ‘J’.

mysql> select * from employee where first_name LIKE 'j%';
+-------------+------------+-----------+---------+-----------------------+------------+
| Employee_id | First_name | Last_name | Salary  | Joining_date          | Department |
+-------------+------------+-----------+---------+-----------------------+------------+
|           1 | John       | Abraham   | 1000000 | 01-JAN-13 12:00:00 AM | Banking    |
|           5 | Jerry      | Pinto     |  650000 | 01-JAN-13 12:00:00 AM | Insurance  |
+-------------+------------+-----------+---------+-----------------------+------------+

--7. Get department wise maximum salary from employee table order by salary ascending?

mysql> select department,max(salary) as maximum_salary from employee group by department order by s
alary;
+------------+----------------+
| department | maximum_salary |
+------------+----------------+
| Services   |         750000 |
| Insurance  |         800000 |
| Banking    |        1000000 |
+------------+----------------+

--8. Select first_name, incentive amount from employee and incentives table forthose employees who have incentives and incentive amount greater than 3000


--9. Create After Insert trigger on Employee table which insert records in view table

