CREATE DATABASE college_db;
USE college_db;

CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(20)
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(50)
);

CREATE TABLE Tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    task_name VARCHAR(100),
    status VARCHAR(20)
);
INSERT INTO Users (username, password, role)
VALUES ('admin', 'admin123', 'admin');

INSERT INTO Students (name, email, course)
VALUES ('Rahul', 'rahul@gmail.com', 'BCA');

INSERT INTO Tasks (student_id, task_name, status)
VALUES (1, 'AI Assignment', 'Pending');

SELECT * FROM Users;
SELECT * FROM Students;
SELECT * FROM Tasks;

SELECT * FROM Students WHERE course='BCA';

