--No.1
SELECT a.primary_poc, w.occurred_at, w.channel, a.name
FROM web_events AS w
JOIN accounts AS a
ON w.account_id = a.id
WHERE a.name = 'Walmart'

--No2
SELECT r.name, s.name, a.name
FROM region as r
JOIN sales_reps as s
ON r.id = s.region_id
JOIN accounts as a
ON s.id = a.sales_rep_id
ORDER BY a.name

--No2 solution
SELECT r.name region, s.name rep, a.name account
FROM sales_reps s
JOIN region r
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
ORDER BY a.name;

--No3
SELECT r.name region_name, a.name acc_name, (o.total_amt_usd / (o.total + 0.01)) unit_price
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON a.id = o.account_id

-- FINAL No1
SELECT r.name region_name, s.name sales_rep, a.name acc_name
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest'
ORDER BY a.name