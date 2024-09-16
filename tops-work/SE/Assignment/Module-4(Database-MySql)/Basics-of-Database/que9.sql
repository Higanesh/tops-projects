/*
Que9. What is save Point? How to create a save Point write a Query?

Ans-> A Savepoint in SQL is a feature that allows you to set a specific point within a transaction, to which you can later roll back if needed. Savepoints help in partially rolling back a transaction without affecting the entire transaction. They are useful when you want to undo a part of a transaction rather than rolling back the entire transaction.

How to Create a Savepoint:
    1. Start a Transaction: A savepoint can only be created inside a transaction.
    2. Define Savepoint: Use the SAVEPOINT keyword to define a savepoint within the transaction.
    3. Rollback to Savepoint: If needed, you can roll back the transaction to a specific savepoint using the ROLLBACK TO command.
    4. Commit the Transaction: After finishing the required operations, the transaction can be committed using COMMIT.
*/
--Example of Using Savepoints in SQL:
    -- Start a transaction
    BEGIN TRANSACTION;

    -- Insert into the employees table
    INSERT INTO employees (employee_id, name, department, salary)
    VALUES (1, 'John', 'IT', 6000);

    -- Create a savepoint after the first insertion
    SAVEPOINT savepoint1;

    -- Insert another record
    INSERT INTO employees (employee_id, name, department, salary)
    VALUES (2, 'Alice', 'HR', 5000);

    -- Create another savepoint after the second insertion
    SAVEPOINT savepoint2;

    -- Insert a third record (this operation might fail)
    INSERT INTO employees (employee_id, name, department, salary)
    VALUES (3, 'Mark', 'Sales', -3000);  -- Negative salary, which is incorrect

    -- If an error occurs, roll back to savepoint2
    ROLLBACK TO savepoint2;

    -- The third insertion is rolled back, but the first two insertions remain

    -- Now, commit the transaction to save the valid changes
    COMMIT;
