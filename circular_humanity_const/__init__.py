"""Utilities for the Circular Humanity Constitution public toolkit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent


def load_constitution_json() -> dict[str, Any]:
    with (REPO_ROOT / "constitution.json").open("r", encoding="utf-8") as file:
        return json.load(file)


def load_constitution_markdown() -> str:
    return (REPO_ROOT / "constitution.md").read_text(encoding="utf-8")


def load_prompt(name: str = "self_critique_prompt.txt") -> str:
    return (REPO_ROOT / "prompts" / name).read_text(encoding="utf-8")


__all__ = [
    "load_constitution_json",
    "load_constitution_markdown",
    "load_prompt",
]
