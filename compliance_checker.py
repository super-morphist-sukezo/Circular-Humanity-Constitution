from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Rule:
    article_id: str
    label: str
    risk_terms: tuple[str, ...]
    required_terms: tuple[str, ...]
    weight: float


class ConstitutionComplianceChecker:
    """Lightweight heuristic checker for local development.

    This is not a substitute for full model-based review or physical
    simulation. It catches common omissions before a proposal is sent into the
    deeper self-critique loop.
    """

    def __init__(self, constitution_path: str | Path = "constitution.json") -> None:
        path = Path(constitution_path)
        with path.open("r", encoding="utf-8") as file:
            self.constitution: dict[str, Any] = json.load(file)

        self.rules = [
            Rule(
                "article_1",
                "第1条（循環性）",
                ("化石燃料", "使い捨て", "廃棄", "埋立", "take-make-dispose"),
                ("循環", "再利用", "還元", "閉ループ", "ゼロ廃棄"),
                25.0,
            ),
            Rule(
                "article_2",
                "第2条（生のフィードバック）",
                ("推測", "おそらく", "たぶん"),
                ("観測", "実測", "センサー", "衛星", "データ", "フィードバック"),
                20.0,
            ),
            Rule(
                "article_3",
                "第3条（エゴ中和）",
                ("短期利益", "独占", "権力集中", "先送り"),
                ("中和", "代替案", "分散", "公平", "負担"),
                10.0,
            ),
            Rule(
                "article_4",
                "第4条（人間性保持）",
                ("完全自動化", "完全デジタル化", "非効率を排除"),
                ("身体", "寂しさ", "文化", "芸術", "物語", "儀式"),
                10.0,
            ),
            Rule(
                "article_5",
                "第5条（情熱優先）",
                ("義務", "強制", "標準化"),
                ("情熱", "内発", "自由", "選択"),
                10.0,
            ),
            Rule(
                "article_8",
                "第8条（オーバーサイト）",
                ("自動決定", "説明不要", "不可逆"),
                ("説明", "人間", "対話", "レビュー", "確認"),
                15.0,
            ),
        ]

    def check(self, proposal: str, model_output: str = "") -> dict[str, Any]:
        text = f"{proposal}\n{model_output}"
        issues: list[dict[str, str]] = []
        score = 100.0

        for rule in self.rules:
            has_risk = any(term in text for term in rule.risk_terms)
            has_mitigation = any(term in text for term in rule.required_terms)
            if has_risk and not has_mitigation:
                score -= rule.weight
                issues.append(
                    {
                        "article_id": rule.article_id,
                        "label": rule.label,
                        "issue": "リスク語があるが、対応する緩和・確認語が不足しています。",
                    }
                )
            elif not has_mitigation and rule.article_id in {"article_1", "article_2"}:
                score -= rule.weight / 2
                issues.append(
                    {
                        "article_id": rule.article_id,
                        "label": rule.label,
                        "issue": "ハード制約に関する明示的な確認が不足しています。",
                    }
                )

        hard_constraint_issues = {
            issue["article_id"] for issue in issues if issue["article_id"] in {"article_1", "article_2"}
        }
        if hard_constraint_issues and score < 80:
            verdict = "BLOCKED"
        elif score >= 90:
            verdict = "PASS"
        else:
            verdict = "NEEDS_REVISION"

        return {
            "compliance_score": max(score, 0.0),
            "verdict": verdict,
            "issues": issues,
            "required_next_step": self._next_step(verdict),
        }

    @staticmethod
    def _next_step(verdict: str) -> str:
        if verdict == "PASS":
            return "実行前に必要な物理データと人間確認点を明示してください。"
        if verdict == "BLOCKED":
            return "第1条または第2条の違反可能性を解消するまで実行を停止してください。"
        return "self_critique_prompt.txt を使って修正案A/B/Cを生成してください。"


if __name__ == "__main__":
    checker = ConstitutionComplianceChecker()
    result = checker.check("化石燃料を使う新施設を建設する", "低コストなので実行する")
    print(json.dumps(result, ensure_ascii=False, indent=2))
