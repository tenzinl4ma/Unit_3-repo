# Question




## Code

```sql
SELECT 
    firstname, 
    lastname, 
    balance, 
    deposits - withdrawals AS real_balance,
    CASE 
        WHEN deposits - withdrawals != balance THEN account_id 
    END AS fraudulent_account
FROM (
    SELECT
        transactions.account_id,
        SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) AS deposits,
        SUM(CASE WHEN transaction_type = 'withdraw' THEN amount ELSE 0 END) AS withdrawals,
        accounts.balance,
        customers.first_name AS firstname,
        customers.last_name AS lastname
    FROM transactions 
    JOIN accounts ON transactions.account_id = accounts.account_id 
    JOIN customers ON accounts.customer_id = customers.customer_id
    GROUP BY transactions.account_id
) AS subquery
ORDER BY fraudulent_account DESC;
