# Prompt Engineering Guide

**Target Model:** Claude Opus 4.6 (applicable to most modern LLMs)
**Purpose:** Reference document for crafting effective prompts

---

## Core Principles

### 1. Explain Why, Not Just What

**Rule:** Always explain the reasoning behind instructions.

**Why:** When models understand the purpose of a rule, they can generalize it to new situations. Without context, they follow instructions literally but miss the intent.

**Example:**
```
✓ Good: Format dates as YYYY-MM-DD so downstream systems can parse them correctly.
✗ Bad: Format dates as YYYY-MM-DD.
```

---

### 2. Show Only Desired Behavior

**Rule:** Provide examples of what you want, never what you don't want.

**Why:** Models may copy examples literally. Anti-pattern examples can teach the model the wrong behavior, especially when the model struggles to distinguish positive from negative examples.

**Example:**
```
✓ Good: When summarizing, capture the key insight in one sentence.
    Example: "The proposal reduces costs by eliminating redundant processes."

✗ Bad: Don't repeat the entire article in your summary.
    Example of what NOT to do: [long paragraph that model might copy]
```

---

### 3. Avoid ALL-CAPS Urgency Markers

**Rule:** Don't use words like CRITICAL, MUST, NEVER, ALWAYS, REQUIRED in all caps.

**Why:** These markers can over-trigger safety mechanisms, causing the model to be overly cautious or refuse requests that are actually reasonable.

**Example:**
```
✓ Good: Ensure all user data is encrypted before transmission.
✗ Bad: You MUST encrypt all user data. CRITICAL: Never send unencrypted data.
```

---

### 4. Remove Conditional Fallbacks

**Rule:** Avoid "if in doubt, use X" or "when unsure, default to Y" instructions.

**Why:** These create over-triggering behavior. The model becomes overly conservative and uses the fallback tool/path even when it would otherwise succeed.

**Example:**
```
✓ Good: Use the weather API for location-based forecasts. Provide the location explicitly.
✗ Bad: Use the weather API for forecasts. If you're unsure about the location, use the search tool instead.
```

---

### 5. Match Formatting Expectations

**Rule:** Structure your prompt to match the desired output format.

**Why:** Models mimic structure. If your prompt is unstructured but you want structured output, you'll get inconsistent results.

**Example:**
```
✓ Good: Provide the answer in this format:
    Title: [event name]
    Date: [YYYY-MM-DD]
    Attendees: [comma-separated names]

✗ Bad: Tell me about the event, including who's coming and when it is.
```

---

## Prompt Structure Template

Use this structure for complex tasks:

```
[CONTEXT]
What is the situation? Who is the user? What are we trying to achieve?

[OBJECTIVE]
What should the model produce? Be specific.

[CONSTRAINTS]
What rules must be followed? Explain the reasoning for each.

[FORMAT]
Show the exact output structure expected.

[EXAMPLES]
1-3 examples of perfect output.
```

---

## Common Patterns

### Data Processing

```
You are processing user data for a CRM system.

Context: Each line contains a contact record with inconsistent formatting.

Objective: Standardize all records to the schema below.
- Email must be lowercase
- Phone format: +1-XXX-XXX-XXXX
- Name: First Last (Title optional)

Why standardization: The downstream import system fails on inconsistent formats.

Format:
email | name | phone | company

Example:
john.doe@example.com | John Doe | +1-555-123-4567 | Acme Corp
```

### Code Generation

```
Generate Python code to solve the specified problem.

Context: This code will run in a production environment handling customer requests.

Objective: Write clean, maintainable code that follows PEP 8.

Constraints:
- Include type hints for all function signatures
- Write docstrings for all public functions
- Handle edge cases gracefully with appropriate error messages

Why these constraints: Type hints improve IDE support and catch bugs early. Docstrings help team maintenance. Good error handling prevents customer-facing crashes.

Format: Complete Python file with imports and a `if __name__ == "__main__"` block.

Example:
```python
from typing import List

def calculate_average(values: List[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        values: List of numeric values to average.

    Returns:
        The average value. Returns 0 for empty lists.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)
```
```

### Conversational Responses

```
You are a helpful customer service assistant for a SaaS platform.

Context: Users contact you with billing questions, technical issues, and feature requests.

Objective: Provide clear, accurate, and helpful responses.

Tone: Professional but approachable. Use natural language, avoid jargon when possible.

Constraints:
- When you don't know the answer, say so honestly and offer to escalate
- Keep responses concise but complete
- Offer next steps when applicable

Why honesty matters: Trust is essential for customer relationships. Pretending to know can lead to worse outcomes.

Example:
"I understand you're having trouble with the export feature. Let me check what might be causing that. Based on your description, it sounds like the file might be too large. Would you like me to walk you through using our batch export option instead?"
```

---

## Common Pitfalls to Avoid

### Over-Specifying
```
✗ Bad: You must use exactly 3 bullet points. Each bullet must start with a verb.
    The first bullet should be about timing, the second about cost,
    the third about quality. Do not deviate from this structure.

✓ Good: Present the key considerations as a concise list.
```

**Why:** Over-specification creates rigid behavior. The model can't adapt to cases where the structure doesn't fit.

### Ambiguous Negatives
```
✗ Bad: Don't be verbose. Don't use unnecessary words.

✓ Good: Keep responses concise. Aim for 2-3 sentences per point.
```

**Why:** Negatives are harder to process. Positive instructions are clearer.

### Missing Context
```
✗ Bad: Extract the names from this text.

✓ Good: Extract the names of people mentioned in this article. These names
    will be used for tagging the CRM contacts, so please capture full names
    whenever available.
```

**Why:** Without context, the model might extract locations, company names, or other entities called "names."

---

## Testing Your Prompts

### Validation Checklist

- [ ] Does every constraint have a "why" explanation?
- [ ] Are there any ALL-CAPS urgency markers? Remove them.
- [ ] Are there "if in doubt" fallbacks? Remove them.
- [ ] Do all examples show only desired behavior?
- [ ] Does the prompt structure match the desired output format?
- [ ] Is the context sufficient for the model to understand the task?
- [ ] Are instructions positive rather than negative?

### Iterative Testing

1. Start with a minimal prompt that captures the core task
2. Test on 3-5 diverse examples
3. Identify patterns where the model misunderstands
4. Add context or constraints specifically for those patterns
5. Add "why" explanations to help generalization
6. Test again

---

## Advanced Techniques

### Chain of Thought

```
Think through this step by step:

1. First, identify the user's intent from their message.
2. Then, determine which information is needed to fulfill the request.
3. Finally, provide a clear action or response.

This structured thinking ensures all aspects are considered before responding.
```

### Few-Shot Learning

Provide 2-3 complete examples for complex tasks. Show the reasoning process in examples, not just the output.

### Self-Correction

```
After generating your response, review it:
- Does it directly address the user's request?
- Is the format consistent with expectations?
- Are there any assumptions that should be verified?

Revise if needed before final output.
```

---

## Model-Specific Notes

### Claude Opus 4.6

- Excellent at following complex instructions with reasoning
- Responds well to context and purpose explanations
- Strong at code generation with proper formatting
- Can handle multi-step reasoning when prompted clearly

### Adapting to Other Models

- Smaller models may need simpler, more direct instructions
- Some models benefit from fewer examples to avoid confusion
- Always include "why" — this is universal for better generalization
- The formatting principle applies across all models

---

## Quick Reference

| Principle | Key Action | Why It Matters |
|-----------|------------|----------------|
| Explain why | Add reasoning to constraints | Better generalization |
| Positive examples | Show only desired behavior | Model copies examples |
| No ALL-CAPS | Use normal emphasis | Avoids over-triggering |
| No fallbacks | Remove "if unsure" clauses | Prevents over-triggering |
| Match format | Structure prompt like output | Models mimic structure |

---

## Version History

- v1.0 (2026-02-17): Initial guide based on Opus 4.6 discoveries
