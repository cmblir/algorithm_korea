-- 코드를 작성해주세요
select count(*) as fish_count, month(time) as month
from fish_info
group by 2
order by 2 asc