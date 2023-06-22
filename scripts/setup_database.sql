-- Setup our mysql database.
-- create database,
-- create user, assign password and grant previledges

CREATE DATABASE IF NOT EXISTS internhub_db;
CREATE USER IF NOT EXISTS 'internhub'@'localhost' IDENTIFIED BY 'internhub_dev';
GRANT ALL PRIVILEGES ON `internhub_db`.* TO 'internhub'@'localhost';
FLUSH PRIVILEGES;