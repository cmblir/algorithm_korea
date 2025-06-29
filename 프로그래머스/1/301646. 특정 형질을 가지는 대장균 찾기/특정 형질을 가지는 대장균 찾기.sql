SELECT COUNT(*) AS count
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0 -- 2번째 비트 형질 X
  AND ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0);
-- 1번 3번 비트 형질 보유 