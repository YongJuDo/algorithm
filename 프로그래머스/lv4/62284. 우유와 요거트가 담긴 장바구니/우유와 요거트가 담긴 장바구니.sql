-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Yogurt', 'Milk')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) > 1