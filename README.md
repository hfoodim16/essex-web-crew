# Essex Web Crew

A Claude Code **agent team** that runs like a mini web agency. Each run it scouts
Essex County, NJ trade businesses that need a website, scores them, pauses for Harry's
approval, then builds a full review-ready pitch package for the top 3: a research
dossier, a working website mockup (built the "Corey Blake workflow" way), and a
personalized outreach email.

**The team never contacts anyone.** Everything lands on disk for Harry to review;
Harry generates the real images and sends outreach himself.

## Layout

```
CLAUDE.md                 Shared playbook (all teammates read this)
KICKOFF.md                How to run — dry run + full run prompts
.claude/
  settings.local.json     Enables agent teams (experimental flag)
  agents/                 Teammate roles: scout, analyst, builder, copywriter, critic
pipeline/
  rubric.md               Candidate scoring rubric
  candidates.md           Scout output → Analyst scoring (regenerated each run)
templates/
  email-voice.md          Outreach email voice guide
  package-checklist.md    Critic's sign-off gate ($10K Checklist + email checks)
prospects/
  <slug>/                 One folder per approved prospect:
    dossier.md · mockup/ · screenshots/ · outreach-email.md · audit.md
```

## The team

| Role | Does |
|------|------|
| **scout** | Finds 10–15 qualifying businesses (free web tools). |
| **analyst** | Scores them, researches the top 3, writes dossiers, pitches the shortlist. |
| **builder** ×3 | Each builds one prospect's mockup (Corey Blake recipe), owns its own folder. |
| **copywriter** | Writes the personalized outreach email + one-pager. |
| **critic** | Audits every mockup against the $10K Checklist and every email; loops until sign-off. |

The lead session orchestrates, enforces the approval pause, and assembles results.

## Run it

See `KICKOFF.md`. Do the dry run first — agent teams are experimental and token-heavy.
