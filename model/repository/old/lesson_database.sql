create database mft;

create table mft.lesson_tbl
(
    id     int primary key auto_increment,
    title varchar(20),
    week_day date,
    start_date date,
    start_time time,
    end_time time
);