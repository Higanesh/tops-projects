/*
Que5. From the following table, write a SQL query to select a range of products whose price is in the range Rs.200 to Rs.600. Begin and end values are included. Return pro_id, pro_name, pro_price, and pro_com.
*/

--Sample table: item_mast

mysql> select * from item_mast;
+--------+-----------------+-----------+---------+
| pro_id | pro_name        | pro_price | pro_com |
+--------+-----------------+-----------+---------+
|    101 | Mother Board    |      3200 |      15 |
|    102 | Key Board       |       450 |      16 |
|    103 | ZIP drive       |       250 |      14 |
|    104 | Speaker         |       550 |      16 |
|    105 | Monitor         |      5000 |      11 |
|    106 | DVD drive       |       900 |      12 |
|    107 | CD drive        |       800 |      12 |
|    108 | Printer         |      2600 |      13 |
|    109 | Refill Catridge |       350 |      13 |
|    110 | Mouse           |       250 |      12 |
+--------+-----------------+-----------+---------+

mysql> select * from item_mast where pro_price between 200 AND 600;
+--------+-----------------+-----------+---------+
| pro_id | pro_name        | pro_price | pro_com |
+--------+-----------------+-----------+---------+
|    102 | Key Board       |       450 |      16 |
|    103 | ZIP drive       |       250 |      14 |
|    104 | Speaker         |       550 |      16 |
|    109 | Refill Catridge |       350 |      13 |
|    110 | Mouse           |       250 |      12 |
+--------+-----------------+-----------+---------+

--From the following table, write a SQL query to calculate the average price for a manufacturer code of 16. Return avg.

mysql> select avg(pro_price) as average_price from item_mast where pro_com = 16;
+---------------+
| average_price |
+---------------+
|           500 |
+---------------+

--From the following table, write a SQL query to display the pro_name as 'Item Name' and pro_price as 'Price in Rs.'

mysql> select pro_name as 'Item Name',pro_price as 'Price in Rs.' from item_mast;
+-----------------+--------------+
| Item Name       | Price in Rs. |
+-----------------+--------------+
| Mother Board    |         3200 |
| Key Board       |          450 |
| ZIP drive       |          250 |
| Speaker         |          550 |
| Monitor         |         5000 |
| DVD drive       |          900 |
| CD drive        |          800 |
| Printer         |         2600 |
| Refill Catridge |          350 |
| Mouse           |          250 |
+-----------------+--------------+

--mysql> select pro_name,pro_price from item_mast where pro_price >= 250;
+-----------------+-----------+
| pro_name        | pro_price |
+-----------------+-----------+
| Mother Board    |      3200 |
| Key Board       |       450 |
| ZIP drive       |       250 |
| Speaker         |       550 |
| Monitor         |      5000 |
| DVD drive       |       900 |
| CD drive        |       800 |
| Printer         |      2600 |
| Refill Catridge |       350 |
| Mouse           |       250 |
+-----------------+-----------+

mysql> select pro_name,pro_price from item_mast where pro_price >= 250 order by pro_price desc;
+-----------------+-----------+
| pro_name        | pro_price |
+-----------------+-----------+
| Monitor         |      5000 |
| Mother Board    |      3200 |
| Printer         |      2600 |
| DVD drive       |       900 |
| CD drive        |       800 |
| Speaker         |       550 |
| Key Board       |       450 |
| Refill Catridge |       350 |
| ZIP drive       |       250 |
| Mouse           |       250 |
+-----------------+-----------+

mysql> select pro_name,pro_price from item_mast where pro_price >= 250 order by pro_name;
+-----------------+-----------+
| pro_name        | pro_price |
+-----------------+-----------+
| CD drive        |       800 |
| DVD drive       |       900 |
| Key Board       |       450 |
| Monitor         |      5000 |
| Mother Board    |      3200 |
| Mouse           |       250 |
| Printer         |      2600 |
| Refill Catridge |       350 |
| Speaker         |       550 |
| ZIP drive       |       250 |
+-----------------+-----------+

mysql> select avg(pro_price) as 'average price',pro_com as 'company code' from item_mast group by pro_c
om;
+---------------+--------------+
| average price | company code |
+---------------+--------------+
|          5000 |           11 |
|           650 |           12 |
|          1475 |           13 |
|           250 |           14 |
|          3200 |           15 |
|           500 |           16 |
+---------------+--------------+
