SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS 출고일자,
    CASE
        WHEN DATEDIFF(OUT_DATE, '2022-5-1') <= 0 THEN '출고완료'
        WHEN DATEDIFF(OUT_DATE, '2022-5-1') > 0 THEN '출고대기'
        ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;