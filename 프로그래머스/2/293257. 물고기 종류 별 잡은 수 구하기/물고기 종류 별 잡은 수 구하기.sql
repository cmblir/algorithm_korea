-- 코드를 작성해주세요
select count(*) as fish_count, fish_name
from fish_info f
join fish_name_info i on (f.fish_type = i.fish_type)
group by 2
order by 1 desc