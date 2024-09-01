#CREATE DATABASE learnvista_db;

USE learnvista_db;

#CREATE TABLE users (
#id INT AUTO_INCREMENT PRIMARY KEY,
#first_name VARCHAR(100) NOT NULL,
#last_name VARCHAR(100) NOT NULL,
#email VARCHAR(500) NOT NULL,
#password VARCHAR(255) NOT NULL,
#country VARCHAR(100) NOT NULL,
#phone VARCHAR(20),
#dob DATE,
#role ENUM("student", "instructor", "admin") NOT NULL
#);

#SHOW TABLES;


#DESC users;


CREATE TABLE users (
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(500) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    country VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    dob DATE NOT NULL,
    role ENUM('student', 'instructor', 'admin') NOT NULL
);

ALTER TABLE users
    MODIFY COLUMN email VARCHAR(500) PRIMARY KEY NOT NULL ,
    MODIFY COLUMN first_name VARCHAR(100) NOT NULL,
    MODIFY COLUMN last_name VARCHAR(100) NOT NULL,
    MODIFY COLUMN password VARCHAR(255) NOT NULL,
    MODIFY COLUMN country VARCHAR(100) NOT NULL,
    MODIFY COLUMN phone VARCHAR(20),
    MODIFY COLUMN dob DATE NOT NULL,
    MODIFY COLUMN role ENUM('student', 'instructor', 'admin') NOT NULL;


