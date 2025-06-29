-- 코드를 입력하세요
SELECT mcdp_cd as '진료과코드', count(*) as '5월예약건수'
from appointment
where apnt_ymd between date '2022-05-01' and date '2022-05-31'
group by 1
order by count(*) asc, mcdp_cd asc
