/*
    Nicholas Schmid
    Assignment 10.3
    WhatABook: Database and Table Creation

    Adapted from:
    Title: whatabook.init.sql
    Author: Professor Krasso
    Date: 16 July 2020
    Description: WhatABook database initialization script.
*/

-- Drop the database if it alrady exists
DROP DATABASE IF EXISTS whatabook;

-- Recreate the WhatABook database
CREATE DATABASE whatabook;

-- Select the new database
USE whatabook

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

/*
    insert store record - 1 location required
*/
INSERT INTO store(locale)
    VALUES('1600 Pennsylvania Ave NW, Washington, D.C. 20006');

/*
    insert book records - 9 required
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Hitchhikers Guide to the Galaxy', 'Douglas Adams', 'The meaning of life, the universe, and everything is 42.');

INSERT INTO book(book_name, author, details)
    VALUES('Fight Club', 'Chuck Palahniuk', 'It has been, like, 25 years. Can we talk about it?');

INSERT INTO book(book_name, author, details)
    VALUES('Choke', 'Chuck Palaniuk', 'Fight Club was better.');

INSERT INTO book(book_name, author, details)
    VALUES('The Restaurant at the End of the Universe', 'Douglas Adams', 'Sequel to Hitchhikers Guide to the Galaxy.');

INSERT INTO book(book_name, author, details)
    VALUES('Journey to the Center of the Earth', 'Jules Verne', 'A better title than, Spelunking to the Core.');

INSERT INTO book(book_name, author, details)
    VALUES('Sherlock Holmes', 'Arthur Conan Doyle', 'Elementary, my dear Watson, is never actually said by Homles.');

INSERT INTO book(book_name, author, details)
    VALUES('The Time Machine', 'H.G. Wells', 'They had flux capacitors in Victorian England.');

INSERT INTO book(book_name, author, details)
    VALUES('The War of the Worlds', 'H.G. Wells', 'Where are Will Smith and Jeff Goldblum when you need them?');

INSERT INTO book(book_name, author, details)
    VALUES('20,000 Leagues Under the Sea', 'Jules Verne', 'Submersible ship vs giant squid.');

/*
    insert users - 3 required
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('James', 'Bond');

INSERT INTO user(first_name, last_name)
    VALUES('Jason', 'Bourne');

INSERT INTO user(first_name, last_name)
    VALUES('Maxwell', 'Smart');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'James'), 
        (SELECT book_id FROM book WHERE book_name = 'Fight Club')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jason'),
        (SELECT book_id FROM book WHERE book_name = '20,000 Leagues Under the Sea')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Maxwell'),
        (SELECT book_id FROM book WHERE book_name = 'Sherlock Holmes')
    );
