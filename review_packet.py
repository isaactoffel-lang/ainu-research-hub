"""A synthetic handoff checklist for a research reviewer."""

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Assumption:
    claim: str
    evidence: str
    challenge: str


@dataclass(frozen=True)
class ResearchPacket:
    thesis: str
    assumptions: tuple[Assumption, ...]
    open_question: str


def review_blockers(packet):
    """Return gaps that make a packet hard for another analyst to review."""
    gaps = []
    if not packet.thesis.strip():
        gaps.append("State the thesis")
    if not packet.assumptions:
        gaps.append("Record a decision-driving assumption")
    for assumption in packet.assumptions:
        if not assumption.claim.strip():
            gaps.append("State the assumption")
        if not assumption.evidence.strip():
            gaps.append("Attach evidence for the assumption")
        if not assumption.challenge.strip():
            gaps.append("Explain what would weaken the assumption")
    if not packet.open_question.strip():
        gaps.append("Give the reviewer an open question")
    return tuple(gaps)


def main():
    assumption = Assumption(
        claim="Projects with secured offtake face less demand uncertainty",
        evidence="",
        challenge="A weak counterparty could make that protection unreliable",
    )
    packet = ResearchPacket(
        thesis="Contract quality should drive the order of diligence",
        assumptions=(assumption,),
        open_question="How much protection survives a counterparty default?",
    )

    if review_blockers(packet) != ("Attach evidence for the assumption",):
        raise AssertionError("Missing evidence was not isolated")
    print("PASS | Returned an unsupported assumption for revision")

    sourced = replace(assumption, evidence="Illustrative offtake terms")
    if review_blockers(replace(packet, assumptions=(sourced,))):
        raise AssertionError("The revised packet still has structural gaps")
    print("PASS | Marked the revised packet ready for human review")


if __name__ == "__main__":
    main()
