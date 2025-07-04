-- 코드를 입력하세요
SELECT board_id, writer_id, title, price,
    CASE
        when status = 'DONE' THEN '거래완료'
        when status = 'RESERVED' THEN '예약중'
        else '판매중'
    end as status
from used_goods_board
where created_date = '2022-10-05'
order by 1 desc