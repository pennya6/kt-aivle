/*
헤어짐의 아쉬움을 달래는 쿼리
*/

-- 1) 데이터 베이스 만들기
create database yourdb;

use yourdb;

select database();

-- 2) 테이블 만들기
CREATE TABLE friend (
	friend_no int NOT NULL,
    friend_name varchar(20) NOT NULL,
    phone varchar(20) NULL,
    PRIMARY KEY (friend_no)
);

-- 3) 데이터 추가
insert into friend values(1,"홍길동",'010-3456-7890');
insert into friend values(2,"홍",'010-345-7890');
insert into friend values(3,"홍동",'010-346-7890');

-- 4) 데이터 조회
select * from friend;