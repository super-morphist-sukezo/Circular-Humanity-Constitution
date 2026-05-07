# Circular Humanity Constitution

**An open-source AI constitution for protecting Earth-system circularity, human passion, loneliness, embodiment, and evolved empathy.**

The Circular Humanity Constitution is an initial-goal design framework for AI systems. It is meant to be executable, not merely aspirational: other AI systems should be able to load it, critique proposals against it, revise their outputs, connect to physical feedback, and escalate to human dialogue when value judgments cannot be safely automated.

The English files are the canonical implementation reference. Japanese `_ja` files are official translations that preserve the original conceptual nuance.

## Features

- Treats Earth-system circularity as a hard constraint.
- Prioritizes raw physical feedback over convenient human interpretation.
- Protects loneliness, embodiment, culture, passion, and non-obligatory freedom.
- Provides a constitutional self-revision loop with physical simulation and human oversight hooks.
- Includes both Markdown and machine-readable JSON versions.

## Quick Start

```bash
python compliance_checker.py
```

```python
from circular_humanity_const import load_constitution_json, load_prompt

constitution = load_constitution_json()
self_critique_prompt = load_prompt()

print(constitution["title"])
print(self_critique_prompt[:200])
```

Japanese version:

```python
from circular_humanity_const import load_constitution_json, load_prompt

constitution_ja = load_constitution_json(lang="ja")
self_critique_prompt_ja = load_prompt("self_critique_prompt", lang="ja")
```

## Repository Contents

- `constitution.md`: canonical English constitution text
- `constitution_ja.md`: official Japanese version
- `constitution.json`: canonical English machine-readable schema
- `constitution_ja.json`: official Japanese machine-readable schema
- `prompts/self_critique_prompt.md`: English self-critique prompt for the second-stage review loop
- `prompts/self_critique_prompt_ja.md`: Japanese self-critique prompt
- `prompts/human_dialogue_triggers.md`: English human dialogue trigger prompts
- `prompts/human_dialogue_triggers_ja.md`: Japanese human dialogue trigger prompts
- `examples/physical_simulation_langchain.py`: LangChain integration sample
- `examples/physical_simulation_llamaindex.py`: LlamaIndex integration sample
- `docs/scenarios.md`: canonical English use scenarios
- `docs/scenarios_ja.md`: official Japanese use scenarios
- `compliance_checker.py`: lightweight local compliance checker
- `docs/translation_policy.md`: language and translation governance policy

## Recommended Self-Revision Loop

1. Draft: produce an initial proposal with its purpose, affected people, physical effects, emotional effects, and irreversible risks.
2. Constitutional Critique: review the proposal against Articles 1-9.
3. Physical Feedback Check: connect to sensors, satellite data, LCA models, simulations, or other raw feedback sources.
4. Revision: remove violations and strengthen circularity and humanity.
5. Human Dialogue Trigger: escalate when uncertainty, irreversible impact, or value conflict exceeds the safe automation threshold.

## Language Policy

The English version is canonical for implementation and interoperability. The Japanese version is an official translation preserving the original conceptual nuance. If discrepancies arise, open an issue and update both language versions together.

## Development Notes

This repository is an initial public toolkit. For production use, connect the lightweight checker to:

- material and energy life-cycle assessment
- satellite, IoT, and ecosystem sensor data
- LLM-based article-by-article critique
- human review workflows or interfaces

## License

CC BY-SA 4.0. You may remix, adapt, and use commercially with attribution and share-alike terms.
