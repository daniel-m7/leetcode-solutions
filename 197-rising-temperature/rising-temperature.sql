/* Write your PL/SQL query statement below */
SELECT today.id
FROM Weather today 

WHERE EXISTS (
    select 1 
    from Weather yesterday
    where today.temperature > yesterday.temperature
    and today.recordDate = yesterday.recordDate + 1
)