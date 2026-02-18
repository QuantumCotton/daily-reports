# Prompt Engineering Checklist

Quick reference for validating prompts before deployment.

---

## Essential Checks

### Context & Purpose
- [ ] Task is clearly defined (what to do)
- [ ] Context explains the situation (who, why, what for)
- [ ] Every constraint has a "why" explanation

### Examples
- [ ] All examples show ONLY desired behavior
- [ ] No anti-patterns or "don't do this" examples
- [ ] 1-3 complete examples included
- [ ] Examples match expected output format exactly

### Language & Tone
- [ ] No ALL-CAPS urgency markers (CRITICAL, MUST, NEVER, ALWAYS, REQUIRED)
- [ ] Instructions use positive language ("do X" not "don't do Y")
- [ ] Tone matches expected output tone

### Fallbacks & Safety
- [ ] No "if in doubt" or "when unsure" instructions
- [ ] No conditional fallback paths that cause over-triggering
- [ ] Safety constraints are specific, not overly broad

### Formatting
- [ ] Prompt structure matches desired output format
- [ ] Format is explicitly shown or templated
- [ ] Headers, sections, bullet points match output expectations

---

## Common Anti-Patterns to Remove

| ❌ Remove | ✅ Replace With |
|----------|-----------------|
| CRITICAL/MUST/NEVER/ALWAYS (all caps) | Normal emphasis or inline context |
| "If you're unsure, use X" | Remove entirely |
| "Example of bad output: ..." | Remove entirely |
| "Don't be verbose" | "Keep responses concise" |
| "Never forget to..." | "Remember to..." |
| "REQUIRED: must include" | "Include" |
| Overly specific rules that don't allow flexibility | General principles |

---

## Pre-Flight Checklist

Before finalizing a prompt:

1. **Read it aloud** - Does it sound natural?
2. **Check the "why"** - Can you explain the purpose of each rule?
3. **Verify examples** - Would you want this exact output?
4. **Scan for caps** - Any ALL-CAPS words lurking?
5. **Test with variety** - Try 3 different inputs to see if it handles edge cases

---

## Quick Reference: The 5 Core Rules

| Rule | Action | Why |
|------|--------|-----|
| 1. Explain Why | Add reasoning to constraints | Models generalize better with purpose |
| 2. Positive Examples | Show only what you want | Models copy examples literally |
| 3. No ALL-CAPS | Use normal emphasis | Prevents over-triggering safety |
| 4. No Fallbacks | Remove "if unsure" clauses | Prevents over-conservative behavior |
| 5. Match Format | Structure prompt like output | Models mimic structure |

---

## Prompt Template (Copy-Paste)

```
Context: [What's the situation? Who is the user? What are we trying to achieve?]

Objective: [What should the model produce? Be specific.]

Constraints:
- [Rule 1]
  Why: [The reasoning behind this rule]
- [Rule 2]
  Why: [The reasoning behind this rule]

Format:
[Show exact output structure expected]

Examples:
[1-3 examples of perfect output - only what you want to see]
```

---

## Debug Guide

If the model isn't behaving as expected:

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Being overly cautious/restrictive | ALL-CAPS markers found | Remove caps, use normal emphasis |
| Using fallback when it shouldn't | "If in doubt" instructions | Remove fallback clauses |
| Copying bad patterns from examples | Anti-pattern examples shown | Remove, show only good examples |
| Missing the intent | Constraints lack "why" | Add reasoning explanations |
| Output format inconsistent | Prompt structure mismatched | Match prompt format to desired output |
| Too rigid/can't adapt | Over-specified requirements | Use principles instead of rules |

---

## Tips for Common Tasks

### Code Generation
- [ ] Include language and style guide (PEP 8, ESLint, etc.)
- [ ] Specify type hints or documentation requirements
- [ ] Show complete, working example

### Data Processing
- [ ] Define input and output schemas clearly
- [ ] Specify handling of edge cases (nulls, malformed data)
- [ ] Example shows full transformation

### Conversational Responses
- [ ] Define persona and tone
- [ ] Specify what to do when uncertain (honesty, escalation)
- [ ] Example shows natural language flow

### Summarization
- [ ] Specify length and style (one sentence, bullet points, etc.)
- [ ] Identify what information to prioritize
- [ ] Example captures key insight in expected format

---

## Version History

- v1.0 (2026-02-17): Initial checklist aligned with PROMPT_ENGINEERING.md
