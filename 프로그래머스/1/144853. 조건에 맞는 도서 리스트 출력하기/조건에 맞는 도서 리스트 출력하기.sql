-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
FROM book
WHERE published_date >= DATE '2021-01-01' 
  AND published_date < DATE '2022-01-01' and category = '인문'
order by published_date asc