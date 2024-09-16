/*
Que10. What is trigger and how to create a Trigger in SQL?

Ans-> A Trigger in SQL is a special kind of stored procedure that automatically executes (or "fires") in response to specific events on a particular table or view. Triggers are often used to maintain data integrity, enforce business rules, or audit changes to the data.

CREATE TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
BEGIN
    -- SQL statements to execute when the trigger fires
END;

*/


    