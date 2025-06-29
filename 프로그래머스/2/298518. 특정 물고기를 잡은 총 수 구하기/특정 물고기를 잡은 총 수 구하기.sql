-- 코드를 작성해주세요
select count(*) as fish_count
from fish_info i
join fish_name_info n ON (i.fish_type = n.fish_type)
where regexp_like(n.fish_name, 'BASS|SNAPPER')