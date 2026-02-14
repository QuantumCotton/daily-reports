# Platform Builder Research Log

> ESH Mail - Our own bulk email sending platform with self-healing reputation management

## Vision
Build a competitive bulk email platform that solves the #1 problem in cold email: **reputation fragility**.

**The Innovation:**
- Bad lists don't destroy reputation
- System auto-detects reputation drops
- Internal warmup emails auto-send to restore score
- Reputation is self-healing, not fragile

## Market Opportunity
- **Competitors:** Instantly, Lemlist, Mailshake, Quickmail
- **Instantly pricing:** $297/month for 50 accounts = $3,564/year
- **Our target:** $97/month average pricing
- **Revenue potential:**
  - 100 customers: $116,400/year
  - 1,000 customers: $1.16M/year

## Research Questions (Answered 2026-02-14)

### 1. Email Reputation APIs ✅

**Google Postmaster Tools API:**
- **Access:** REST API available at `developers.google.com/workspace/gmail/postmaster`
- **Metrics available:** Spam rate, domain reputation, IP reputation, delivery errors, feedback loop, authentication (SPF/DKIM/DMARC), encryption
- **Cost:** FREE
- **Limitations:** V2 API may be limited; some data only available via UI

**Microsoft SNDS (Smart Network Data Services):**
- **Access:** Requires account + IP verification at `sendersupport.olc.protection.outlook.com`
- **Metrics available:** IP health, spam complaints, filter results, blocked status, activity on IP
- **Cost:** FREE
- **Setup:** Log in with Microsoft Account, request access for IPs, receive verification email

**Third-party Reputation APIs:**
- **Return Path / 250ok:** Acquired by Validity in 2019, no longer standalone. Now part of Everest platform
- **GlockApps:** All-in-one deliverability testing, spam score checking, domain/IP analytics
- **Pricing:** Specific pricing not easily found; likely enterprise contracts
- **Alternative:** Use Google/Microsoft APIs directly (free) + build internal monitoring

**Key Reputation Metrics:**
- Spam score
- Complaint rate
- Bounce rate
- Delivery errors
- IP reputation score
- Domain reputation score
- Encryption success rate
- Feedback loop data

---

### 2. Domain Warmup Protocols ✅

**Industry-Standard Warmup Schedules:**

**New Domain (brand new):**
- Day 1-7: 20-30 emails/day
- Week 2: Gradually increase to 50-100/day
- Week 3-4: 100-200/day
- Month 2: 300-500/day
- **Goal:** Near 100% open rate, 30%+ reply rate

**Example Warmup Schedule (Inboxroad):**
- Day 1: 100 emails
- Day 2: 150 emails
- Day 3: 200 emails
- Day 4: 250 emails
- Day 5: 300 emails
- Day 6: 350 emails
- Day 7: 400 emails
- Day 8: 450 emails
- Day 9: 500 emails
- Day 10: 600 emails
- Day 11: 700 emails
- Day 12: 800 emails
- ... gradual ramp to 5000+ by Day 30

**Provider-Specific Limits:**
- **Gmail Workspace:** 2,000 messages/day (pay version)
- **Yahoo:** 500 emails/day maximum
- **Outlook:** Via SNDS monitoring

**IP Warmup Best Practices:**
- Start with dedicated IP, warm gradually (same schedule as domain)
- Shared IPs: harder to control reputation, ESPs may not grant SNDS access
- Consistency is key — daily sending, not burst patterns

**Warmup Automation Tools:**
- Warmy.io
- Mailwarm
- Folderly (subdomain/IP warmup + spam fixes if reputation drops)
- Mailreach.co

---

### 3. SMTP & Inbox Providers ✅

**AWS SES:**
- **Cost:** $0.10 per 1,000 emails after 62,000 free/month (when sending from EC2/Lambda)
- **Dedicated IP:** $24.95/month
- **Virtual Deliverability Manager:** $0.07 per 1,000 emails
- **Attachment fees:** $0.12/GB
- **Warmup:** Required manual process via API tickets

**SendGrid:**
- **Pricing:** ~5-10x more than AWS SES for similar volumes
- **Features:** Email marketing platform, API + SMTP
- **Deliverability:** Good, built-in reputation management

**Mailgun:**
- **Pricing:** Competitive to SendGrid (5-10x more than SES)
- **Features:** REST API, SMTP relay, IP pools
- **Deliverability:** IP pool management

**Postmark:**
- **Positioning:** Premium, transactional email focus
- **Deliverability:** Excellent (reputation-focused)
- **Pricing:** Higher per-email cost, but better inbox placement

**Inbox Providers:**
- **Gmail:** Postmaster Tools API (free)
- **Outlook/Hotmail:** SNDS (free)
- **Yahoo:** 500/day limit, limited monitoring
- **AOL:** Hard to monitor, stricter filters

---

### 4. Mails.ai Architecture (Reference) ❌

**Status:** Limited current info found. Mails.ai may not be actively operating or has minimal public presence.

**What we know:**
- Positioning: Bulk email platform with AI fine-tuning of sending strategies
- Feature: Send thousands/day while preserving sender reputation
- Feature: Link sender accounts, AI optimizes delivery

**Need:** Wayback Machine research to find archived docs/architecture details

---

### 5. Cost Model & Pricing ✅

**Competitor Pricing (2026):**

| Platform | Entry Price | Tier | Features |
|----------|--------------|-------|----------|
| **Instantly** | $37/month | Growth | Unlimited accounts, 5,000 emails/month |
| Instantly | $97/month | Hypergrowth | More accounts, higher volume |
| **Lemlist** | $49-55/month | Starter | Per-seat pricing, AI ice-breaker |
| Lemlist | $99/month | Business | More seats, advanced features |
| **Mailshake** | $29/month | Entry | Best value for small teams |
| Mailshake | $199/month | Scale | Up to 50,000 emails |

**Infrastructure Costs (for our platform):**

**Domains:**
- Registration: $10-15/year (.com)
- Renewal: Same
- Subdomains: Free (create as many as needed)

**IPs:**
- Dedicated IP (AWS SES): $24.95/month
- Shared IP: Included in SMTP provider cost

**SMTP (per 1,000 emails):**
- AWS SES: $0.10
- SendGrid: $0.50-1.00 (estimated)
- Mailgun: $0.50-1.00 (estimated)

**Inboxes:**
- Gmail Workspace: $6-12/user/month
- Outlook: Often bundled with Microsoft 365

**Margin Calculation (at $97/month price point):**

Assume 50 accounts customer (Growth tier):

| Cost Item | Monthly Cost | Annual Cost |
|-----------|--------------|-------------|
| SMTP (50,000 emails @ $0.10/1k) | $5 | $60 |
| Domains (50 subdomains @ $1/year amortized) | $4.17 | $50 |
| Dedicated IPs (if needed) | $24.95 | $299 |
| Inboxes (50 Gmail accounts @ $6/mo) | $300 | $3,600 |
| Hosting/Infra | $20 | $240 |
| **Total Cost** | **$354** | **$4,249** |

**Revenue:** $97/month × 12 = $1,164/year
**Margin:** ($1,164 - $4,249) = **-3,085 (LOSS)**

**Issue:** At $97/month, we lose money on inbox costs alone if we provide the inboxes.

**Revised Pricing Model (CUSTOMER brings their own inboxes):**

| Cost Item | Monthly Cost | Annual Cost |
|-----------|--------------|-------------|
| SMTP (50,000 emails @ $0.10/1k) | $5 | $60 |
| Domains (50 subdomains) | $4.17 | $50 |
| Hosting/Infra | $20 | $240 |
| **Total Cost** | **$29.17** | **$350** |

**Revenue:** $97/month × 12 = $1,164/year
**Margin:** ($1,164 - $350) = **$814/year (70% margin)**

**Conclusion:** We must NOT provide inboxes. Customers bring their own. This is the SaaS model.

---

### 6. Competitor Analysis ✅

**Instantly.ai:**
- **Strengths:** Unlimited accounts, AI deliverability tools, 450M+ B2B lead database
- **Weaknesses:** $9/month extra for AI credits, pricing confusing (base plan + add-ons)
- **Our edge:** Transparent pricing, internal warmup (their cost), direct lead_bank.db integration

**Lemlist:**
- **Strengths:** Personalization, AI ice-breaker, email finder/verifier
- **Weaknesses:** Per-seat pricing ($55/month starter), expensive for teams
- **Our edge:** Flat pricing, built for lead gen (not generic sales)

**Mailshake:**
- **Strengths:** Best entry price ($29/month), good for small teams
- **Weaknesses:** Limited advanced features, lower volume caps
- **Our edge:** Self-healing reputation, bad-list-proof architecture

---

### 6. Competitor Analysis
- [ ] Instantly: features, weaknesses, pricing gaps
- [ ] Lemlist: what they're doing right/wrong
- [ ] Mailshake: enterprise features, gaps
- [ ] Quickmail: simplicity vs power

## Architecture Ideas (MVP)

### Core Components
1. **Reputation Monitor** (track Google/Postmaster, MS/SNDS scores)
2. **Domain Manager** (warmup schedules, age tracking)
3. **Queue System** (manage email sending at scale)
4. **Internal Warmup Bot** (auto-send when score drops)
5. **Lead Import** (direct from lead_bank.db)
6. **Tracking** (opens, clicks, replies, bounces)

### Tech Stack Options
- **Backend:** Python (FastAPI) or Node.js
- **Database:** PostgreSQL (scale better than SQLite for this)
- **Queue:** Redis + Celery or BullMQ
- **SMTP:** AWS SES or SendGrid (to start)
- **Monitoring:** Prometheus + Grafana

## Prototype Plan (Phase 2)

1. Single domain + 50 inboxes test
2. Basic reputation monitoring
3. Manual warmup (automate later)
4. Send to small test list
5. Track deliverability, opens, replies

## Revenue Model (Draft)

| Tier | Accounts/month | Price/month | Margin |
|-------|---------------|--------------|---------|
| Starter | 10 | $47 | 60% |
| Growth | 50 | $97 | 70% |
| Scale | 100 | $197 | 75% |
| Hypersend | 500+ | $497 | 80% |

**Why undercut:**
- We're the infrastructure AND the provider
- Internal warmup costs $0
- Competitors mark up account reselling

## Next Actions
- [ ] Study Mails.ai (Wayback Machine)
- [ ] Research reputation APIs
- [ ] Document domain warmup best practices
- [ ] Design internal warmup email flow
- [ ] Cost out infrastructure for first 100 customers

## Status
**Phase:** Active Research
**Started:** 2026-02-14
**Cycle time:** Every 30 minutes (background work)
**Priority:** Back-burner (don't block lead gen ops)

---

_Last updated: 2026-02-14_
