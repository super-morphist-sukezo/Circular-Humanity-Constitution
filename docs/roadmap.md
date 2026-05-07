# Roadmap

This roadmap tracks open design tasks for turning the Circular Humanity Constitution into a more executable AI governance toolkit. GitHub Issues are the canonical place for active discussion and prioritization; this file is the public, reader-friendly summary.

## Open Design Tasks

### 1. Emergency and Exception Clauses

Status: proposed
GitHub Issue: [#3](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/3)

Goal: Define what an AI should do when full circularity is temporarily impossible.

Scope:

- temporary allowance conditions for non-circular actions
- damage minimization requirements
- rollback and repair obligations
- time limits and review requirements
- escalation criteria for human dialogue mode

Expected output:

- `docs/emergency_clauses.md`
- matching Japanese version `docs/emergency_clauses_ja.md`
- updates to `constitution.md`, `constitution.json`, and the Japanese counterparts if constitutional text changes

### 2. Operational Terminology Definitions

Status: proposed
GitHub Issue: [#1](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/1)

Goal: Define key terms in a way that AI systems can apply consistently.

Initial terms:

- circularity
- raw physical feedback
- ego pattern
- passion
- humanity
- harm
- human dialogue
- hard constraint
- meta-governance
- irreversible risk

Expected output:

- `docs/definitions.md`
- matching Japanese version `docs/definitions_ja.md`
- stable IDs for terms so prompts, JSON, and checkers can refer to them

### 3. Scoring and Audit Templates

Status: proposed
GitHub Issue: [#2](https://github.com/super-morphist-sukezo/Circular-Humanity-Constitution/issues/2)

Goal: Create a repeatable scoring and audit format for AI proposals.

Initial scoring dimensions:

- circularity
- irreversible risk
- humanity preservation
- raw data reliability
- ego-pattern risk
- passion amplification
- freedom from obligation
- human confirmation required

Expected output:

- `docs/audit_template.md`
- matching Japanese version `docs/audit_template_ja.md`
- JSON-compatible schema for proposal review results
- future integration into `compliance_checker.py`

## Workflow

1. Open one GitHub Issue per design task.
2. Discuss scope and acceptance criteria in the Issue.
3. Add or update the relevant docs.
4. Update prompts, JSON, and checker logic when the design becomes executable.
5. Keep English canonical files and Japanese official translations aligned.

## Priority

Recommended implementation order:

1. Operational Terminology Definitions
2. Emergency and Exception Clauses
3. Scoring and Audit Templates

Definitions should come first because the exception rules and scoring template need stable terms.
