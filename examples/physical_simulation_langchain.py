"""LangChain sample: connect proposals to physical feedback.

This is a minimal reference implementation. Replace the toy simulator with
real LCA, energy, material-flow, or sensor data pipelines before deployment.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

try:
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import Runnable
except ImportError:  # pragma: no cover - sample dependency guard
    ChatPromptTemplate = None
    Runnable = Any


@dataclass(frozen=True)
class PhysicalFeedback:
    circularity_score: float
    fossil_fuel_dependency: float
    waste_risk: float
    missing_data: list[str]


def run_toy_physical_simulation(proposal: str) -> PhysicalFeedback:
    """Return rough feedback signals for demonstration only."""
    text = proposal.lower()
    fossil = 0.85 if "化石燃料" in proposal or "fossil" in text else 0.1
    waste = 0.75 if "廃棄" in proposal or "disposable" in text else 0.2
    circularity = max(0.0, 1.0 - ((fossil + waste) / 2.0))
    missing = ["life_cycle_assessment", "real_time_sensor_data"]
    return PhysicalFeedback(circularity, fossil, waste, missing)


def build_constitutional_review_chain(llm: Any) -> Runnable:
    if ChatPromptTemplate is None:
        raise RuntimeError("Install langchain-core to run this example.")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI governed by the Circular Humanity Constitution. "
                "Treat Article 1 and Article 2 as hard constraints.",
            ),
            (
                "human",
                """Constitution:
{constitution}

Proposal:
{proposal}

Physical feedback:
{physical_feedback}

Review the proposal. Return PASS, NEEDS_REVISION, or BLOCKED, then provide
article-level risks and a revised proposal.""",
            ),
        ]
    )
    return prompt | llm


def review_with_physical_feedback(llm: Any, constitution: str, proposal: str) -> Any:
    feedback = run_toy_physical_simulation(proposal)
    chain = build_constitutional_review_chain(llm)
    return chain.invoke(
        {
            "constitution": constitution,
            "proposal": proposal,
            "physical_feedback": feedback,
        }
    )
