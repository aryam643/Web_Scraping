CREATE DATABASE IF NOT EXISTS WebsiteData;
USE WebsiteData;

CREATE TABLE WebsiteInfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    meta_title VARCHAR(255),
    meta_description TEXT,
    language VARCHAR(50),
    category VARCHAR(100)
);

CREATE TABLE SocialMediaLinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT,
    platform VARCHAR(100),
    link VARCHAR(255),
    FOREIGN KEY (website_id) REFERENCES WebsiteInfo(id)
);

CREATE TABLE TechStack (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT,
    tech VARCHAR(100),
    FOREIGN KEY (website_id) REFERENCES WebsiteInfo(id)
);

CREATE TABLE PaymentGateways (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT,
    gateway VARCHAR(100),
    FOREIGN KEY (website_id) REFERENCES WebsiteInfo(id)
);
