/*
    ● Write SQL query to solve the problem given below
    Consider a database containing two tables named as Customer and Salesman
    For this you need to create a Customer table
    In Customer table attributes are customer id, customer name, city, grade and
    salesman id

    Eg:
    Table : Customer

        +-------------+----------------+------------+-------+-------------+
        | customer_id | cust_name      | city       | grade | salesman_id |
        +-------------+----------------+------------+-------+-------------+
        |        3001 | Brad Guzan     | London     |  NULL |        5005 |
        |        3002 | Nick Rimando   | New York   |   100 |        5001 |
        |        3003 | Jozy Altidor   | Moscow     |   200 |        5007 |
        |        3004 | Fabian Johnson | Paris      |   300 |        5006 |
        |        3005 | Graham Zusi    | California |   200 |        5002 |
        |        3007 | Brad Davis     | New York   |   200 |        5001 |
        |        3008 | Julian Green   | London     |   300 |        5002 |
        |        3009 | Geoff Cameron  | Berlin     |   100 |        5003 |
        +-------------+----------------+------------+-------+-------------+

    In Salesman table attributes will be salesman id, name, city and commission
    Eg:
    Table : Salesman

        +-------------+------------+----------+------------+
        | salesman_id | name       | city     | commission |
        +-------------+------------+----------+------------+
        |        5001 | James Hoog | New York |       0.15 |
        |        5002 | Nail Knite | Paris    |       0.13 |
        |        5003 | Lauson Hen | San Jose |       0.12 |
        |        5005 | Pit Alex   | London   |       0.11 |
        |        5006 | Mc Lyon    | Paris    |       0.14 |
        |        5007 | Paul Adam  | Rome     |       0.13 |
        +-------------+------------+----------+------------+

    From the above given tables write a SQL query to find the salesperson(s) and the
    customer(s) represented here. Return the Customer Name, City, Salesman,
    commission.
    NOTE : Make sure you have to use join concept to solve the query
    Make sure to make your code clean kneat
*/
                                |-----------------|
                                |Table : Salesman |
                                |-----------------|
mysql> create table Salesman (
    -> salesman_id int not null,
    -> name varchar(30) not null,
    -> city varchar(20) not null,
    -> commission float not null
    -> );

mysql> describe salesman;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| salesman_id | int(11)     | NO   |     | NULL    |       |
| name        | varchar(30) | NO   |     | NULL    |       |
| city        | varchar(20) | NO   |     | NULL    |       |
| commission  | float       | NO   |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

mysql> insert into salesman (salesman_id,name,city,commission)
    -> values
    -> (5001,"James Hoog","New York",0.15),
    -> (5002,"Nail Knite","Paris",0.13),
    -> (5005,"Pit Alex","London",0.11),
    -> (5006,"Mc Lyon","Paris",0.14),
    -> (5007,"Paul Adam","Rome",0.13),
    -> (5003,"Lauson Hen","San Jose",0.12)
    -> ;

mysql> select * from salesman;
+-------------+------------+----------+------------+
| salesman_id | name       | city     | commission |
+-------------+------------+----------+------------+
|        5001 | James Hoog | New York |       0.15 |
|        5002 | Nail Knite | Paris    |       0.13 |
|        5003 | Lauson Hen | San Jose |       0.12 |
|        5005 | Pit Alex   | London   |       0.11 |
|        5006 | Mc Lyon    | Paris    |       0.14 |
|        5007 | Paul Adam  | Rome     |       0.13 |
+-------------+------------+----------+------------+

                                |-----------------|
                                |Table : Customer |
                                |-----------------|

mysql> create table Customer (
    -> customer_id int not null primary key auto_increment,
    -> cust_name varchar(30) not null,
    -> city varchar(20) not null,
    -> grade int,
    -> salesman_id int not null,
    -> foreign key (salesman_id) references salesman (salesman_id)
    -> );

mysql> describe customer;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| customer_id | int(11)     | NO   | PRI | NULL    | auto_increment |
| cust_name   | varchar(30) | NO   |     | NULL    |                |
| city        | varchar(20) | NO   |     | NULL    |                |
| grade       | int(11)     | YES  |     | NULL    |                |
| salesman_id | int(11)     | NO   | MUL | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+

mysql> insert into customer (customer_id,cust_name,city,grade,salesman_id)
    -> values
    -> (3002,"Nick Rimando","New York",100,5001),
    -> (3007,"Brad Davis","New York",200,5001),
    -> (3005,"Graham Zusi","California",200,5002),
    -> (3008,"Julian Green","London",300,5002),
    -> (3004,"Fabian Johnson","Paris",300,5006),
    -> (3009,"Geoff Cameron","Berlin",100,5003),
    -> (3003,"Jozy Altidor","Moscow",200,5007),
    -> (3001,"Brad Guzan","London",NULL,5005)
    -> ;

mysql> select * from customer;
+-------------+----------------+------------+-------+-------------+
| customer_id | cust_name      | city       | grade | salesman_id |
+-------------+----------------+------------+-------+-------------+
|        3001 | Brad Guzan     | London     |  NULL |        5005 |
|        3002 | Nick Rimando   | New York   |   100 |        5001 |
|        3003 | Jozy Altidor   | Moscow     |   200 |        5007 |
|        3004 | Fabian Johnson | Paris      |   300 |        5006 |
|        3005 | Graham Zusi    | California |   200 |        5002 |
|        3007 | Brad Davis     | New York   |   200 |        5001 |
|        3008 | Julian Green   | London     |   300 |        5002 |
|        3009 | Geoff Cameron  | Berlin     |   100 |        5003 |
+-------------+----------------+------------+-------+-------------+ 

                                |-----------------|
                                |  Table : Output |
                                |-----------------|


mysql> select customer.cust_name,customer.city,salesman.salesman_id,salesman.commission
    -> from customer
    -> left join salesman on customer.salesman_id = salesman.salesman_id
    -> union
    -> select customer.cust_name,customer.city,salesman.salesman_id,salesman.commission
    -> from customer
    -> right join salesman on customer.salesman_id = salesman.salesman_id
    -> ;
+----------------+------------+-------------+------------+
| cust_name      | city       | salesman_id | commission |
+----------------+------------+-------------+------------+
| Brad Guzan     | London     |        5005 |       0.11 |
| Nick Rimando   | New York   |        5001 |       0.15 |
| Jozy Altidor   | Moscow     |        5007 |       0.13 |
| Fabian Johnson | Paris      |        5006 |       0.14 |
| Graham Zusi    | California |        5002 |       0.13 |
| Brad Davis     | New York   |        5001 |       0.15 |
| Julian Green   | London     |        5002 |       0.13 |
| Geoff Cameron  | Berlin     |        5003 |       0.12 |
+----------------+------------+-------------+------------+
8 rows in set (0.18 sec)