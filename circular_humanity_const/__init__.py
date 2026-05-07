"""Utilities for the Circular Humanity Constitution public toolkit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent


def _suffix(lang: str) -> str:
    if lang == "en":
        return ""
    if lang == "ja":
        return "_ja"
    raise ValueError(f"Unsupported language: {lang!r}. Expected 'en' or 'ja'.")


def load_constitution_json(lang: str = "en") -> dict[str, Any]:
    with (REPO_ROOT / f"constitution{_suffix(lang)}.json").open("r", encoding="utf-8") as file:
        return json.load(file)


def load_constitution_markdown(lang: str = "en") -> str:
    return (REPO_ROOT / f"constitution{_suffix(lang)}.md").read_text(encoding="utf-8")


def load_prompt(name: str = "self_critique_prompt", lang: str = "en") -> str:
    path = Path(name)
    if path.suffix:
        return (REPO_ROOT / "prompts" / path.name).read_text(encoding="utf-8")
    return (REPO_ROOT / "prompts" / f"{name}{_suffix(lang)}.md").read_text(encoding="utf-8")


__all__ = [
    "load_constitution_json",
    "load_constitution_markdown",
    "load_prompt",
]
