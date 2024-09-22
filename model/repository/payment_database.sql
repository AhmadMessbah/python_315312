create database payment_db;

create table payment_db.payment_tbl
(
    id int primary key auto_increment,
    amount int,
    date varchar(20),
    person varchar(20)
);