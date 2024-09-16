/*
Que8. What is SQL Key Constraints writing an Example of SQL Key Constraints

Ans->
What are SQL Key Constraints?
    SQL Key Constraints are rules applied to database columns to ensure the integrity and validity of the data. These constraints are used to enforce certain properties on the data, such as uniqueness, referential integrity, and non-nullability. They help maintain the structure and accuracy of the data within a relational database.

    Types of SQL Key Constraints:
    Primary Key (PK): Ensures that each row in a table is unique and cannot contain NULL values.
        CREATE TABLE employees (
        employee_id INT PRIMARY KEY,   -- Primary Key constraint
        name VARCHAR(100),
        department VARCHAR(50)
    );

    Foreign Key (FK): Enforces referential integrity between two tables by ensuring that a value in one table corresponds to a value in another table.
        CREATE TABLE departments (
        department_id INT PRIMARY KEY,
        department_name VARCHAR(50)
    );

        CREATE TABLE employees (
        employee_id INT PRIMARY KEY,
        name VARCHAR(100),
        department_id INT,
        FOREIGN KEY (department_id) REFERENCES departments(department_id) -- Foreign Key constraint
    );

    Unique Key: Ensures that all values in a column (or a combination of columns) are unique.
    Not Null: Ensures that a column cannot contain NULL values.
        CREATE TABLE employees (
        employee_id INT PRIMARY KEY,
        email VARCHAR(100) UNIQUE,  -- Unique Key constraint
        phone_number VARCHAR(20) UNIQUE  -- Unique Key constraint
    );

    Check Constraint: Ensures that all values in a column satisfy a specific condition.
        CREATE TABLE employees (
        employee_id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT CHECK (age >= 18),   -- Check constraint
        salary DECIMAL(10, 2) CHECK (salary > 0)  -- Check constraint
    );


*/