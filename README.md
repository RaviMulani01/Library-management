# Library-management

# Create Database Coonection for this Project
# Create One database and create this two table inside it
<!-- Update the field in Connection.py -->

# Create Table for Book Issued
CREATE TABLE `book_issued` (
  `book_id` varchar(20) NOT NULL,
  `issued_book_to` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) 

# Create Table for Books
CREATE TABLE `books` (
   `book_id` varchar(20) NOT NULL,
   `book_title` varchar(30) DEFAULT NULL,
   `book_author` varchar(30) DEFAULT NULL,
   `book_status` varchar(30) DEFAULT NULL,
   PRIMARY KEY (`book_id`)
 ) 