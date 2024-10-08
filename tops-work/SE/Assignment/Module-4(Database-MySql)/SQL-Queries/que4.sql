/*
Que4. From the following table, write a SQL query to find orders that are delivered by a salesperson with ID. 5001. Return ord_no, ord_date, purch_amt.
*/

--Sample table: orders

mysql> select * from orders;
+--------+-----------+------------+-------------+-------------+
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
+--------+-----------+------------+-------------+-------------+
|  70001 |     150.5 | 2012-10-05 |        3005 |        5002 |
|  70002 |     65.26 | 2012-10-05 |        3002 |        5001 |
|  70003 |    2480.4 | 2012-10-10 |        3009 |        5003 |
|  70004 |     110.5 | 2012-08-17 |        3009 |        5003 |
|  70005 |    2400.6 | 2012-07-27 |        3007 |        5001 |
|  70007 |     948.5 | 2012-09-10 |        3005 |        5002 |
|  70008 |      5760 | 2012-09-10 |        3002 |        5001 |
|  70009 |    270.65 | 2012-09-10 |        3001 |        5005 |
|  70010 |   1983.43 | 2012-10-10 |        3004 |        5006 |
|  70011 |     75.29 | 2012-08-17 |        3003 |        5007 |
|  70012 |    250.45 | 2012-06-27 |        3008 |        5002 |
|  70013 |    3045.6 | 2012-04-25 |        3002 |        5001 |
+--------+-----------+------------+-------------+-------------+

mysql> select ord_no as order_no,ord_date as order_date,purch_amt as purchase_amt from orders where salesman_id = 5001;
+----------+------------+--------------+
| order_no | order_date | purchase_amt |
+----------+------------+--------------+
|    70002 | 2012-10-05 |        65.26 |
|    70005 | 2012-07-27 |       2400.6 |
|    70008 | 2012-09-10 |         5760 |
|    70013 | 2012-04-25 |       3045.6 |
+----------+------------+--------------+

