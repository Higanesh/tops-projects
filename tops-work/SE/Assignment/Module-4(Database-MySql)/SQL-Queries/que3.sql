/*
Que3. Create table given below: Salesperson and Customer
*/

--Create table query for Salesperson table

mysql> create table Salesperson (
    -> SNo int primary key auto_increment,
    -> SName varchar(30) not null,
    -> City varchar(30) not null,
    -> Comm float(2,2)
    -> );

--O/P

mysql> describe Salesperson;

+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| SNo   | int(11)     | NO   | PRI | NULL    | auto_increment |
| SName | varchar(30) | NO   |     | NULL    |                |
| City  | varchar(30) | NO   |     | NULL    |                |
| Comm  | float(2,2)  | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+

mysql> select * from Salesperson;

+------+---------+-----------+------+
| SNo  | SName   | City      | Comm |
+------+---------+-----------+------+
| 1001 | Peel    | London    | 0.12 |
| 1002 | Serres  | San Jose  | 0.13 |
| 1003 | Axelrod | New York  | 0.10 |
| 1004 | Motika  | London    | 0.11 |
| 1007 | Rafkin  | Barcelona | 0.15 |
+------+---------+-----------+------+

-----------------------------------------------------------------------------------------------

--Create table query for Customer table

mysql> create table Customer (
    -> CNM int primary key auto_increment,
    -> CName varchar(30) not null,
    -> City varchar(30) not null,
    -> Rating int,
    -> Sno int, foreign key (Sno) references Salesperson (Sno)
    -> );

--O/P

mysql> describe customer;

+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| CNM    | int(11)     | NO   | PRI | NULL    | auto_increment |
| CName  | varchar(30) | NO   |     | NULL    |                |
| City   | varchar(30) | NO   |     | NULL    |                |
| Rating | int(11)     | YES  |     | NULL    |                |
| Sno    | int(11)     | YES  | MUL | NULL    |                |
+--------+-------------+------+-----+---------+----------------+

mysql> select * from customer;
+-----+----------+-----------+--------+------+
| CNM | CName    | City      | Rating | Sno  |
+-----+----------+-----------+--------+------+
| 201 | Hoffman  | London    |    100 | 1001 |
| 202 | Giovanne | Roe       |    200 | 1003 |
| 203 | Liu      | San Jose  |    300 | 1002 |
| 204 | Grass    | Barcelona |    100 | 1002 |
| 206 | Clemens  | London    |    300 | 1007 |
| 207 | Pereira  | Roe       |    100 | 1004 |
+-----+----------+-----------+--------+------+

--1. All orders for more than $1000.

--2. Names and cities of all salespeople in London with commission above 0.12

mysql> select Sname,City from salesperson where city = "London" AND Comm > 0.12;
Empty set (0.18 sec)

--3. All salespeople either in Barcelona or in London

mysql> select * from salesperson where city = "Barcelona" OR city = "London";
+------+--------+-----------+------+
| SNo  | SName  | City      | Comm |
+------+--------+-----------+------+
| 1001 | Peel   | London    | 0.12 |
| 1004 | Motika | London    | 0.11 |
| 1007 | Rafkin | Barcelona | 0.15 |
+------+--------+-----------+------+

--4. All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded).

mysql> select * from salesperson where Comm > 0.10 AND Comm < 0.12;
+------+--------+--------+------+
| SNo  | SName  | City   | Comm |
+------+--------+--------+------+
| 1004 | Motika | London | 0.11 |
+------+--------+--------+------+

--5. All customers excluding those with rating <= 100 unless they are located in Rome

mysql> select * from customer where city = "Rome" OR Rating > 100;

+-----+----------+----------+--------+------+
| CNM | CName    | City     | Rating | Sno  |
+-----+----------+----------+--------+------+
| 202 | Giovanne | Rome     |    200 | 1003 |
| 203 | Liu      | San Jose |    300 | 1002 |
| 206 | Clemens  | London   |    300 | 1007 |
| 207 | Pereira  | Rome     |    100 | 1004 |
+-----+----------+----------+--------+------+

--6. Write a SQL statement that displays all the information about all salespeople

mysql> select * from salesperson;
+------+---------+-----------+------+
| SNo  | SName   | City      | Comm |
+------+---------+-----------+------+
| 1001 | Peel    | London    | 0.12 |
| 1002 | Serres  | San Jose  | 0.13 |
| 1003 | Axelrod | New York  | 0.10 |
| 1004 | Motika  | London    | 0.11 |
| 1007 | Rafkin  | Barcelona | 0.15 |
+------+---------+-----------+------+

--7. Write a SQL statement that displays all the information about all salespeople

--Insert data into salesperson table

mysql> insert into salesperson (Sno,SName,City,Comm)
    -> values
    -> (5001,"James Hoog","New York",0.15),
    -> (5002,"Nail Knite","Paris",0.13),
    -> (5005,"Pit Alex","London",0.11),
    -> (5006,"Mc Lyon","Paris",0.14),
    -> (5007,"Paul Adam","Rome",0.13),
    -> (5003,"Lauson Hen","San Jose",0.12)
    -> ;

mysql> select sno as salesman_id,sname as name,city,comm as commission from salesperson;
+-------------+------------+-----------+------------+
| salesman_id | name       | city      | commission |
+-------------+------------+-----------+------------+
|        1001 | Peel       | London    |       0.12 |
|        1002 | Serres     | San Jose  |       0.13 |
|        1003 | Axelrod    | New York  |       0.10 |
|        1004 | Motika     | London    |       0.11 |
|        1007 | Rafkin     | Barcelona |       0.15 |
|        5001 | James Hoog | New York  |       0.15 |
|        5002 | Nail Knite | Paris     |       0.13 |
|        5003 | Lauson Hen | San Jose  |       0.12 |
|        5005 | Pit Alex   | London    |       0.11 |
|        5006 | Mc Lyon    | Paris     |       0.14 |
|        5007 | Paul Adam  | Rome      |       0.13 |
+-------------+------------+-----------+------------+