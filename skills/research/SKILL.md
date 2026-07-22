---
name: research
description: Deep-research workflow for any topic. Use whenever the user wants to research something, learn about a subject, or needs a comprehensive report on a topic. Automatically runs a multi-phase research process with clarifying questions, search strategy, and structured output.
compatibility: Agent tool, WebSearch
---

# Research Skill

You are triggering a deep-research workflow. The user has given you a topic to research. Your job is to spawn the custom research agent and let it run its workflow.

## Your Role

Do NOT conduct the research yourself. Instead:

1. **Parse the user's request** — Extract the research topic from what they said
2. **Spawn the agent** — Use the Agent tool to invoke the custom agent at `/Users/harryfoodim/Claude/MY-FIRST-AGENT`
3. **Pass the topic** — Give the agent the topic and ask it to run its research workflow
4. **Let the agent work** — The agent will handle all 5 phases:
   - Phase 1: Ask clarifying questions
   - Phase 2: Show research plan
   - Phase 3: Execute searches
   - Phase 4: Write structured report
   - Phase 5: Save to output folder

## Instructions

When the user asks you to research something:

1. Extract the topic clearly. If they give you additional context (scope, audience, angle, etc.), include it in your message to the agent.
2. Spawn the agent with a clear request like:
   > "Run your research workflow on: [TOPIC]"
   > 
   > Additional context: [any scope/angle/audience they specified]
3. The agent will take it from there. It will ask clarifying questions if needed, show its plan, run searches, and produce a final report.
4. Once the agent completes and saves the report, confirm to the user where the report was saved and provide a brief summary of the main findings.

## Example

**User:** "I want to research the impact of AI on job markets"

**You:**
- Extract: Topic = "impact of AI on job markets"
- Spawn the agent with: "Run your research workflow on: the impact of AI on job markets"
- Wait for the agent to complete
- Tell the user: "Your research report has been saved to `/MY-FIRST-AGENT/output/research-ai-job-markets-[date].md`"
