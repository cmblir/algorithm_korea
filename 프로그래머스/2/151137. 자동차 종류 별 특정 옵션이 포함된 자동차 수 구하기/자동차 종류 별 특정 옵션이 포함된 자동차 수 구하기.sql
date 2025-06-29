-- 코드를 입력하세요
SELECT car_type, count(*) as cars
from car_rental_company_car
where regexp_like(options, '통풍시트|열선시트|가죽시트')
group by 1
order by 1
