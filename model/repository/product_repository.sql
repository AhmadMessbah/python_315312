create database mft;

create table mft.product_tbl
(
    id         int primary key auto_increment,
    name       varchar(30),
    brand      varchar(30),
    model      varchar(30),
    barcode    varchar(10),
    buy_price  int,
    sell_price int
);