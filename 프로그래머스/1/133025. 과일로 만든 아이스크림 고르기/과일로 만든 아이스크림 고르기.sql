SELECT
    f.flavor
FROM
    first_half f
    JOIN icecream_info i
    USING(flavor)
WHERE
    i.ingredient_type='fruit_based'
    AND f.total_order >= 3000
ORDER BY 
    f.total_order DESC;