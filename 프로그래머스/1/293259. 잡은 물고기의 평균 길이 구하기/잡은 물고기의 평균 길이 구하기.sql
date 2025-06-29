-- 코드를 작성해주세요
WITH le AS (
select 
    CASE 
        WHEN LENGTH IS NULL THEN 10
        ELSE LENGTH
    END AS length
from fish_info)

select round(avg(length), 2) as average_length
from le