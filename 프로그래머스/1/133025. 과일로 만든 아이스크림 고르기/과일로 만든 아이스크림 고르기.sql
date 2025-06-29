-- 코드를 입력하세요
SELECT i.flavor
FROM first_half f
LEFT JOIN icecream_info i ON (i.flavor = f.flavor)
WHERE f.total_order >= 3000 and i.ingredient_type = 'fruit_based'
ORDER BY f.total_order desc