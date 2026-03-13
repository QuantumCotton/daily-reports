# Leads Database Query Guide

Database: leads_consolidated.db
Total records: 87,746
Unique emails: 4,019
Coverage: 4.6%

## Common Queries

### Find all leads in a city
SELECT * FROM leads WHERE city = 'Stuart' LIMIT 10;

### Find leads by category
SELECT * FROM leads WHERE category LIKE '%Property%' LIMIT 10;

### Find leads with email
SELECT * FROM leads WHERE email != '' LIMIT 10;

### Find leads by state
SELECT * FROM leads WHERE state = 'FL' LIMIT 10;

### Count by category
SELECT category, COUNT(*) FROM leads GROUP BY category;

### Count by city ( top 20 )
SELECT city, COUNT(*) as count FROM leads GROUP BY city ORDER BY count DESC LIMIT 20;

### Find leads with phone
SELECT * FROM leads WHERE phone != '' LIMIT 10;
