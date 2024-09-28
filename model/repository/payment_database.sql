create database mft;

create table mft.payment_tbl
(
    id int primary key auto_increment,
    account_id int,
    amount int,
    date_time datetime,
    person varchar(20)
);