create database mft;

create table mft.user_tbl
(
   id int primary key auto_increment,
    name varchar (30) ,
    family varchar (30),
    birth_date datetime ,
    password int,
    username varchar(30),
    is_active varchar(30)

);