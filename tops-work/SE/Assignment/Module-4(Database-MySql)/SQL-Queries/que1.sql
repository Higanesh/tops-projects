/*
Que1. Create Table Name : Student and Exam
*/

--Create table query for Student table

mysql> CREATE TABLE student (
        Rollno INT(11) NOT NULL AUTO_INCREMENT,
        Name VARCHAR(50) NOT NULL,
        Branch VARCHAR(20) NOT NULL,
        PRIMARY KEY (Rollno)
    );

--O/P

mysql> describe Student;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| Rollno | int(11)     | NO   | PRI | NULL    | auto_increment |
| Name   | varchar(50) | NO   |     | NULL    |                |
| Branch | varchar(20) | NO   |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+

mysql> select * from student;
+--------+--------+--------------------+
| Rollno | Name   | Branch             |
+--------+--------+--------------------+
|      1 | Jay    | Computer Science   |
|      2 | Suhani | Electronic and Com |
|      3 | Kriti  | Electronic and Com |
+--------+--------+--------------------+
-----------------------------------------------------------------------------------------------
--Create table query for Exam table

mysql> CREATE TABLE Exam (
        Rollno INT(11),
        S_code VARCHAR(20) NOT NULL,
        Marks INT(11),
        P_code VARCHAR(20) NOT NULL,
        FOREIGN KEY (Rollno) REFERENCES Student(Rollno)
    );

--O/P

mysql> describe Exam;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| Rollno | int(11)     | YES  | MUL | NULL    |       |
| S_code | varchar(20) | NO   |     | NULL    |       |
| Marks  | int(11)     | YES  |     | NULL    |       |
| P_code | varchar(20) | NO   |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+

mysql> select * from Exam;
+--------+--------+-------+--------+
| Rollno | S_code | Marks | P_code |
+--------+--------+-------+--------+
|      1 | CS11   |    50 | CS     |
|      1 | CS12   |    60 | CS     |
|      2 | EC101  |    66 | EC     |
|      2 | EC102  |    70 | EC     |
|      3 | EC101  |    45 | EC     |
|      3 | EC102  |    50 | EC     |
+--------+--------+-------+--------+