create database mft;

create table mft.person(
    id int primary key auto_increment,
    name varchar(20),
    family varchar(20)

);

create table mft.car(
    id int primary key auto_increment,
    name varchar(20),
    model int
);

create table mft.sell(
    id int primary key auto_increment,
    person_id int,
    car_id int,
    price int,
    sell_date date
);


select *
from mft.sell
join mft.person on person.id=mft.sell.person_id
join mft.car on car.id =  mft.sell.car_id;