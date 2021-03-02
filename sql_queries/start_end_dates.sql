SELECT *
FROM  (
   SELECT DISTINCT ON (searchs)
          id, searchs, date AS first_date
   FROM   tweets
   ORDER  BY searchs, date
   ) f
JOIN (
   SELECT DISTINCT ON (searchs)
          searchs, date AS last_date
   FROM   tweets
   ORDER  BY searchs, date DESC
   ) l USING (searchs);