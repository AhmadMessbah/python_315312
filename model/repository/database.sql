create database office_db;

create table office_db.employee_tbl
(
    id     int primary key auto_increment,
    name   varchar(20),
    family varchar(20),
    age    int
);