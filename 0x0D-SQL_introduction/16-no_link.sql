-- list all rows of second_table
-- except rows without name values
-- records listed in descending order
SELECT score, name
FROM second_table 
WHERE name IS NOT NULL AND name  <> ''
ORDER BY score DESC;
