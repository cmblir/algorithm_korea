-- 코드를 작성해주세요
select sum(score) as score, e.emp_no, e.emp_name, e.position, e.email
from hr_department d
join hr_employees e on (d.dept_id = e.dept_id)
join hr_grade g on (e.emp_no = g.emp_no)
where year = '2022'
group by 2,3,4,5
order by 1 desc
limit 1