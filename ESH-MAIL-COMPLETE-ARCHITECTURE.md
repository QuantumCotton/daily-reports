# ESH Mail - Complete Architecture & Economics

> Combined research from Chris + AI agent

## Overview

Building a gamified email warming and cold outreach platform that:
- Competes with Instantly.ai and Mails.ai
- Uses dynamic reputation system (gamification)
- Targets $1/$5/$10 monthly price points
- Self-healing reputation management

---

## Phase 1: Infrastructure of Delivery

### MTA Architecture Selection

**Winner: KumoMTA (Rust-based)**

| MTA | Language | Benchmark (msgs/hr) | Config Model | Best For |
|-----|----------|---------------------|--------------|----------|
| Postfix | C | ~500,000 | Static/Map Files | Standard enterprise |
| Haraka | Node.js | Moderate | JavaScript Plugins | API-driven platforms |
| ZoneMTA | Node.js | Moderate | JSON/JS | Multi-tenant routing |
| **KumoMTA** | **Rust** | **6,800,000** | **Lua Scripting** | **Massive scale, dynamic IP sharding** |
| PowerMTA | C++ | High | Static/API | Legacy enterprise (expensive) |

**Why KumoMTA:**
- 13.6x faster than Postfix
- Lua scripting for dynamic routing
- Real-time reputation-based IP assignment
- Memory-safe, async I/O

### IP Rotation & Pooling

**Leasing vs Buying:**

| Option | Cost | Notes |
|--------|------|-------|
| **Lease /24 subnet** | $102-150/month ($0.38-0.50/IP) | Best for $1/user model |
| Buy /24 subnet | $8,000-8,700 ($31-34/IP) | High CAPEX, not recommended |

**IP Sharding Strategy:**
1. **Premium External Pools** - High-reputation users → pristine shared IPs
2. **Rehabilitation Pools** - Low-reputation users → isolated subnet

### Network Topology

**Hybrid P2P + Seed Accounts:**

| Model | Cost | Risk |
|-------|------|------|
| Pure P2P | $0 | Bad apple contagion, TrustRank degradation |
| 1,000 Golden Seeds | $3,000-5,000/month | High cost |
| **Hybrid** | ~$1,000-2,000/month | Balanced |

**Golden Seed Providers:**
- Infraforge: $3-4/mailbox/month
- Email Astra: $3-4/mailbox/month
- TrulyInbox: ~$2.90/mailbox/month

**Recommendation:** Use limited golden seeds (200-500) for trust injection + P2P for volume.

---

## Phase 2: Gamification Logic

### ISP Reputation Metrics (Weighting)

| Metric | Weight | Threshold | Penalty |
|--------|--------|-----------|---------|
| **Hard Bounce Rate** | HIGH | >5% | Severe damage, blocklisting |
| **Spam Complaint Rate** | EXTREME | >0.3% | Spam folder routing |
| **Positive Reply Rate** | HIGH | 15-30% (warmup), 0-7% (production) | Reward signal |
| **Open/Click Rate** | MODERATE | Variable | Engagement signal |

### Proposed Scoring Formula (0-100)

```
Base Score = 50

PENALTIES:
- Hard bounce rate >1%: -10 points
- Hard bounce rate >2%: -20 points
- Hard bounce rate >5%: -50 points (relegation to rehabilitation pool)
- Spam complaint >0.1%: -15 points
- Spam complaint >0.3%: -40 points (spam folder routing)

REWARDS:
- Reply rate >10%: +10 points
- Reply rate >20%: +20 points
- Open rate >40%: +5 points
- 7 days without bounces: +5 points
- 30 days without bounces: +15 points
```

### Rehabilitation Rules

If user drops below 30 points:
1. Restricted to internal warming duties (50% capacity)
2. Cannot send external outreach
3. Must process 50 warmup emails to earn 1 external credit

---

## Phase 3: From-Inbox Sending Mechanism

### How It Works

1. **OAuth2 Connection** - Gmail API with `gmail.modify` scope
2. **Inject via API** - `users.messages.insert()` makes email appear as "received"
3. **Hidden Filtering** - Auto-archive label, user never sees warmup emails
4. **Thread Building** - 10-50+ replies create engagement signals

### Capacity Balancing

| Reputation Score | Warmup % | Outreach % |
|------------------|----------|------------|
| <30 (new/rehab) | 50% | 50% |
| 30-60 (building) | 30% | 70% |
| 60-80 (established) | 15% | 85% |
| 80+ (mature) | 5% | 95% |

### Tech Stack

| Component | Technology |
|-----------|------------|
| MTA | KumoMTA (Rust + Lua) |
| Queue | Redis |
| Database | PostgreSQL |
| Backend | Go or Python FastAPI |
| Frontend | React |
| API Layer | Gmail API + Microsoft Graph |
| Monitoring | Prometheus + Grafana |

---

## Phase 4: Unit Economics

### $1/month Tier

**COGS per user:**
- IP cost: $0.50/month (shared /24)
- Server cost: $0.10/month (amortized)
- Storage: $0.05/month
- Bandwidth: $0.10/month
- **Total COGS: $0.75/user**

**Margin: 25% ($0.25/user)**

### $10/month Tier

**COGS per user:**
- IP cost: $0.50/month
- Server cost: $0.20/month
- Storage: $0.15/month
- Bandwidth: $0.30/month
- **Total COGS: $1.15/user**

**Margin: 88.5% ($8.85/user)**

### Break-Even Analysis

| Tier | Users Needed | Monthly Revenue | Monthly Profit |
|------|--------------|-----------------|----------------|
| $1 only | 1,000 | $1,000 | $250 |
| $10 only | 1,000 | $10,000 | $8,850 |
| Mixed (80/20) | 1,000 | $2,800 | $2,290 |

---

## Scalability Thresholds

| User Count | Infrastructure |
|------------|----------------|
| 0-1,000 | Single VPS + KumoMTA |
| 1,000-10,000 | 3 VPS cluster + Redis cluster |
| 10,000+ | Kubernetes + multi-region |

---

## Competitive Comparison

| Platform | Price | Features | Our Edge |
|----------|-------|----------|----------|
| Instantly | $37-97/month | Unlimited accounts | Gamification, cheaper |
| Lemlist | $49-99/month | Per-seat pricing | Flat pricing |
| Mailshake | $29-199/month | Basic features | Self-healing reputation |
| **ESH Mail** | **$1-10/month** | **Gamification + reputation balancing** | **Network effects + cheap** |

---

## Action Items

1. [ ] Set up KumoMTA test server
2. [ ] Lease /24 subnet ($102-150/month)
3. [ ] Build Gmail API OAuth flow
4. [ ] Implement capacity balancer
5. [ ] Create reputation scoring system
6. [ ] Build leaderboard dashboard
7. [ ] Test with 10 beta users

---

**Created:** 2026-02-15
**Sources:** Chris research PDF + AI agent Mails.ai architecture analysis
