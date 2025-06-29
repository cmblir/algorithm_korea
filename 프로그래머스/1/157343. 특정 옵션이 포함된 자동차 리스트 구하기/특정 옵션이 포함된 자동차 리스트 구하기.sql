-- 코드를 입력하세요
SELECT *
FROM car_rental_company_car
where regexp_like(options, '네비게이션')
order by car_id desc