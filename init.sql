CREATE DATABASE IF NOT EXISTS chatdb;
USE chatdb;
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room VARCHAR(255),
    username VARCHAR(255) ,
    message TEXT ,
    created_at DATETIME
);