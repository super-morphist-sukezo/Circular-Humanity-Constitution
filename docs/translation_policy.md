# Translation Policy

The Circular Humanity Constitution uses English as the canonical implementation language and Japanese as an official translation.

## Canonical Files

- `README.md`
- `constitution.md`
- `constitution.json`
- `prompts/self_critique_prompt.md`
- `prompts/human_dialogue_triggers.md`
- `docs/scenarios.md`

These files are the primary reference for implementation, interoperability, and integrations with other AI systems.

## Official Japanese Files

- `README_ja.md`
- `constitution_ja.md`
- `constitution_ja.json`
- `prompts/self_critique_prompt_ja.md`
- `prompts/human_dialogue_triggers_ja.md`
- `docs/scenarios_ja.md`

The Japanese files are official translations, not informal notes. They preserve the original conceptual nuance of the project and should remain aligned with the canonical English files.

## Synchronization Rules

1. Article IDs must remain stable across languages, such as `article_1` and `article_9`.
2. Changes to hard constraints, amendment rules, prompts, or execution protocols should update both English and Japanese files in the same pull request whenever possible.
3. If a discrepancy is found, open an issue describing the affected file, article ID, and proposed resolution.
4. If language versions conflict during implementation, use the English canonical version temporarily, then resolve both versions through review.
5. Japanese wording may preserve nuance that English cannot fully carry; such cases should be noted in issues or commit messages rather than silently flattened.

## JSON Design

The English and Japanese JSON files are separate to keep each file easy for AI systems and developer tools to load without language mixing. Correspondence is maintained through stable IDs and article numbers.
