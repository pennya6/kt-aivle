/*
커피 한잔과 쿼리 한줄의 여유
*/

use myshop2019;

select database();

-- 1) 쿼리 1 시각화
select customer_name as 고객명, phone as 전화번호,repeat('🧡',cast(point/10000  as unsigned int))  as 포인트
from customer
where city in("대전","인천") and point>0
order by 3 desc;	

-- 2) 쿼리 2(피벗, 크로스탭)
select city,
	sum(if (gender='F',point,0))as 여자,
    sum(if (gender='M',point,0))as 남자, 
    sum(point) as 전체포인트
from customer
group by city;


select gender as 성별,
	sum(if (city='서울',point,0))as 서울,
    sum(if (city='부산',point,0))as 부산, 
    sum(if (city='광주',point,0))as 광주,
    sum(if (city='수원',point,0))as 수원, 
    sum(point) as 전체포인트
from customer
group by gender;