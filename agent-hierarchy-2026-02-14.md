# AGENT HIERARCHY - Updated 2026-02-14

## MY BRAIN (TIER 0)
**Model:** GLM-5
**Agent:** deep-researcher (ONLY agent with GLM-5)
**Purpose:** High-level planning, complex reasoning, orchestrator
**Count:** 1 agent

---

## TIER 1: GLM-4.7 (6 agents)
**Purpose:** High-priority tasks, complex research, strategic work
**Allocation:**
- 3 from zai router
- 3 from openai router
**Total:** 6 agents

**Use cases:**
- Critical research tasks
- Complex analysis
- Platform-builder work
- Strategy planning

---

## TIER 2: GLM-4.7 Flash (4 agents)
**Purpose:** Fast reasoning, quick research, planning
**Allocation:**
- 2 from zai router
- 2 from openai router
**Total:** 4 agents

**Use cases:**
- Quick lookups
- Summarization
- Fast analysis tasks

---

## TIER 3: GLM-4.6 (6 agents)
**Purpose:** Analysis, review, scoring work
**Allocation:**
- 3 from zai router
- 3 from openai router
**Total:** 6 agents

**Use cases:**
- Code review
- Lead scoring
- Quality control
- Content review

---

## TIER 4: GLM-4.5 Air (20 agents)
**Purpose:** Bulk processing, routine tasks, parallel work
**Allocation:**
- 10 from zai router
- 10 from openai router
**Total:** 20 agents

**Use cases:**
- Lead validation
- Email pattern checking
- Simple research
- Data cleaning

---

## TIER 5: GLM-4.5 Air (20 MORE agents)
**Purpose:** Maximum parallelization, massive batch processing
**Allocation:**
- 10 from zai router
- 10 from openai router
**Total:** 20 agents

**Use cases:**
- High-volume scraping
- Email verification batches
- Lead enrichment at scale
- Parallel web research

---

## TOTAL SWARM CAPACITY
**Tier 0:** 1 (GLM-5)
**Tier 1:** 6 (GLM-4.7)
**Tier 2:** 4 (GLM-4.7 Flash)
**Tier 3:** 6 (GLM-4.6)
**Tier 4:** 20 (GLM-4.5 Air)
**Tier 5:** 20 (GLM-4.5 Air)

**GRAND TOTAL:** 57 agents

---

## USAGE STRATEGY

1. **Use cheapest first** - Tier 4 & 5 (GLM-4.5 Air) for bulk work
2. **GLM-4.7 for important** - Tier 1 for critical research
3. **GLM-5 for me only** - deep-researcher brain, no other agent
4. **Refine with top tier** when needed - escalate from 4.5 → 4.7 → 5

## COST EFFICIENCY
- GLM-5 token cost: ~5000x GLM-4.5
- GLM-4.7 token cost: ~100x GLM-4.5
- GLM-4.5 Air: Virtually free
- **Rule:** 10 cheap agents > 1 expensive agent every time

## CURRENTLY CONFIGURED AGENTS
From openclaw.json agents.list:
1. deep-researcher (GLM-4.7) ← Should be GLM-5
2. platform-builder (GLM-4.7)
3. main (GLM-4.7)
4. coding-specialist (GLM-4.7)
5. github-reviewer (GLM-4.7)
6. seo-analyst (GLM-4.7)
7. email-quality (GLM-4.7)
8. research-analyst (GLM-4.7)
9. outreach-writer (GLM-4.7)
10. strategy-planner (GLM-4.7)
11. lead-scout (GLM-4.7)
12. lead-scout-247 (GLM-4.7)
13. creative-writer (GLM-4.7)
14. lead-generator (GLM-4.7)

**Missing:** Need to expand to 57 agents with proper model allocation
**Fix needed:** deep-researcher should use GLM-5 (zai/glm-5)

---
*Last updated: 2026-02-14 21:06 UTC by deep-researcher*
