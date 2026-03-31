-- Write your query below
-- SELECT DISTINCT ON (student_id)
--     student_id,
--     exam_id,
--     score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id;

select student_id, MIN(exam_id) exam_id, score
from exam_results e
where score = (select MAX(score) from exam_results where student_id = e.student_id)
group by student_id, score
order by student_id