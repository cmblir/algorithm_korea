SELECT 
    history_id, 
    car_id, 
    date_format(start_date, '%Y-%m-%d') AS start_date, 
    date_format(end_date, '%Y-%m-%d') AS end_date,
    CASE
        WHEN DATEDIFF(end_date, start_date) >= 29 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE start_date >= DATE '2022-09-01' 
  AND start_date < DATE '2022-10-01'
ORDER BY history_id DESC