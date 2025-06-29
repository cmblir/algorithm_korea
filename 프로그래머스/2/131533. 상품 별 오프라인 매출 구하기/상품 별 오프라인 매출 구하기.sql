-- 코드를 입력하세요
SELECT p.product_code, SUM(p.price * o.sales_amount) as sales
from product p
join offline_sale o on (o.product_id = p.product_id)
group by p.product_code
order by sum(p.price * o.sales_amount) desc, p.product_code asc