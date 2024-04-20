-- 코드를 입력하세요
SELECT date_format(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '3'
UNION ALL
SELECT date_format(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '3'
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC