-- 코드를 입력하세요
SELECT b.book_id, a.author_name, date_format(b.published_date, '%Y-%m-%d') as published_date
from book b
inner join author a on (a.author_id = b.author_id)
where b.category = '경제'
order by b.published_date asc