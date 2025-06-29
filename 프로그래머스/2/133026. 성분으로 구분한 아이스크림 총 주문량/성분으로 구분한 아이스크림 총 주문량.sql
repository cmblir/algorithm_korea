-- 코드를 입력하세요
SELECT i.ingredient_type, sum(f.total_order) as total_order
FROM first_half f
join icecream_info i ON (i.flavor = f.flavor)
group by 1
order by sum(f.total_order) asc