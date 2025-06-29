-- 코드를 입력하세요
WITH cnt AS (
SELECT 
    FLOOR(price/10000) * 10000 AS price_name
from product
)

select price_name as price_group, count(*) as products
from cnt
group by 1
order by 1 asc
