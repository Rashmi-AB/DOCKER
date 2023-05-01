CREATE TABLE students (
    regno VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    vaccination_status ENUM('Yes', 'No')
);

INSERT INTO students (regno, name, vaccination_status)
VALUES ('1234', 'John Doe', 'Yes'),
       ('5678', 'Jane Doe', 'No');
