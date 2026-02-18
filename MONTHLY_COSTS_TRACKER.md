# MONTHLY COSTS TRACKER
# Created: 2026-02-18 00:35 UTC
# Purpose: Track all costs, calculate profit, scale as needed

---

## 📊 FIXED MONTHLY COSTS (CURRENT)

| Cost Item | Monthly Cost | Notes | Scale Trigger |
|-----------|---------------|--------|---------------|
| **VPS** | $5/month | RackNerd VPS | Fixed |
| **APIs (Z.AI)** | $30/month | 4B tokens/month | When we exceed 4B, add 3B (+$15) or 10B (+$30) |
| **Instantly** | TBD | Email warming (need to clarify) | TBD |
| **TOTAL FIXED COSTS** | **$35/month** | Current total | When needed |

---

## 📈 VARIABLE COSTS (AS NEEDED)

| Cost Item | Cost | When Needed | Decision |
|-----------|-------|-------------|-----------|
| **Google Ads** | $1,700 (spent) | $0 success - **DON'T USE** | Abandoned |
| **Instantly Scale 1** | TBD | Phase 2 (5 markets) | TBD |
| **Instantly Scale 2** | TBD | Phase 3 (15 markets) | TBD |
| **Custom SMTP** | TBD | Phase 4-5 (30-40 markets) | TBD |
| **Token Scale 1** | +$15/month | Add 3B tokens (7B total) | When lead gen scales up |
| **Token Scale 2** | +$30/month | Add 10B tokens (14B total) | National expansion (40 markets) |

---

## 💰 PROFIT CALCULATOR

### Per Contractor (Example: Josue)

| Metric | Formula | Amount |
|--------|---------|--------|
| Contractor Revenue | Input from Josue | $57,000 (example) |
| Our Commission (15%) | Revenue × 0.15 | $8,550 |
| Our Costs | Fixed + Variable | $35 |
| Our Profit | Commission - Costs | $8,515 |

### Per Market (5 Contractors)

| Metric | Formula | Amount |
|--------|---------|--------|
| Market Contractor Revenue | $57K-$98K × 5 contractors | $285,000 - $490,000 |
| Our Commission (15%) | Revenue × 0.15 | $42,750 - $73,500 |
| Our Costs | Fixed + Variable | $35 |
| Our Profit | Commission - Costs | $42,715 - $73,465 |

### 1-Year Profit (15 Contractors, 40 Markets)

| Month | Contractors | Contractor Revenue | Our Commission | Our Costs | Our Profit |
|-------|-------------|-------------------|---------------|-----------|------------|
| Month 1 | 1 | $57,000 | $8,550 | $35 | $8,515 |
| Month 3 | 5 | $285,000 - $490,000 | $42,750 - $73,500 | $35 | $42,715 - $73,465 |
| Month 6 | 15 | $855,000 - $1,470,000 | $128,250 - $220,500 | $35 | $128,215 - $220,465 |
| Month 12 | 15 | $1,710,000 - $2,940,000 | $256,500 - $441,000 | $35 | $256,465 - $440,965 |

**ARR (15% Commission):**
- Conservative: **$3.08M/year** ($256,500/month × 12)
- Aggressive: **$5.29M/year** ($441,000/month × 12)

---

## 📊 COST TRACKING SPREADSHEET

**CSV File:** ~/.openclaw/workspace/cost_profit_tracker.csv

**Columns:**
- Month
- Contractors
- Contractor_Revenue
- Our_Commission_15%
- Our_Costs_Fixed
- Our_Costs_Variable
- Our_Total_Costs
- Our_Profit
- Cumulative_Profit
- Notes

**Update Process:**
1. At end of each month, add new row
2. Input contractor revenue (ask Chris/Josue)
3. Calculate commission (15%)
4. Input costs (fixed + variable)
5. Calculate profit
6. Track cumulative profit

---

## 🚨 SCALING TRIGGERS

### Token Scaling (AI Intelligence)

| Trigger | Action | New Cost |
|----------|--------|----------|
| Hit 4B tokens/month | Add 3B tokens | +$15/month (total $50) |
| Hit 7B tokens/month | Add 10B tokens | +$30/month (total $80) |

### Email Infrastructure Scaling

| Trigger | Action | New Cost |
|----------|--------|----------|
| Phase 1 (TC only) | Instantly small plan | TBD |
| Phase 2 (5 markets) | Instantly medium plan | TBD |
| Phase 3 (15 markets) | Instantly large plan or Custom SMTP | TBD |
| Phase 4-5 (30-40 markets) | Custom SMTP infrastructure | TBD |

---

## 📝 DECISIONS NEEDED

### Clarify with Chris:
1. **Instantly Pricing:** How much for email warming? (was thinking $30/mo)
2. **Token Scaling:** When do we scale to 7B or 14B tokens?
3. **Buyout Terms:** Is $20,000 correct for website + CRM buyout?

### Update When Decided:
1. Add Instantly cost to monthly fixed costs
2. Set token scaling triggers (when to add 3B/10B tokens)
3. Confirm buyout price ($20,000 for website + CRM)

---

*Created: 2026-02-18 00:35 UTC*
*Current Monthly Costs: $35 (VPS $5 + APIs $30)*
