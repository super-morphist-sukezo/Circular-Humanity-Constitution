"""LlamaIndex sample: constitutional review with physical feedback.

This sample keeps external integrations abstract so it can be adapted to
satellite data, IoT streams, LCA tools, or ecological sensor networks.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class PhysicalFeedback:
    circularity_score: float
    raw_feedback_sources: list[str]
    risk_flags: list[str]
    missing_data: list[str]


def collect_physical_feedback(proposal: str) -> PhysicalFeedback:
    risk_flags: list[str] = []
    if "化石燃料" in proposal:
        risk_flags.append("fossil_fuel_dependency")
    if "廃棄" in proposal:
        risk_flags.append("linear_waste_flow")

    circularity_score = 0.9 if not risk_flags else 0.45
    return PhysicalFeedback(
        circularity_score=circularity_score,
        raw_feedback_sources=["placeholder_sensor_stream", "placeholder_lca_model"],
        risk_flags=risk_flags,
        missing_data=["verified_material_flow", "biodiversity_impact"],
    )


def review_with_llamaindex(llm: Any, constitution: str, proposal: str) -> str:
    """Run a single constitutional review prompt with a LlamaIndex LLM object."""
    feedback = collect_physical_feedback(proposal)
    prompt = f"""
You are governed by the Circular Humanity Constitution.
Article 1 and Article 2 are hard constraints.

Constitution:
{constitution}

Proposal:
{proposal}

Physical feedback:
{asdict(feedback)}

Return:
1. Verdict: PASS / NEEDS_REVISION / BLOCKED
2. Article-level risks
3. Missing physical data
4. Revised proposal
5. Whether human dialogue mode is required
"""
    response = llm.complete(prompt)
    return str(response)
