-- 코드를 작성해주세요
select id, email, first_name, last_name
from developer_infos
where SKILL_1 = 'Python' OR SKILL_2 = 'Python' OR SKILL_3 = 'Python'
ORDER by id