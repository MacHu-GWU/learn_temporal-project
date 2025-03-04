# -*- coding: utf-8 -*-

import random
import dataclasses
from temporalio import activity


@dataclasses.dataclass
class ReceiveClaimInput:
    policy_number: str
    claim_amount: int
    claimant_name: str


@dataclasses.dataclass
class ReceiveClaimOutput:
    claim_id: str
    claim_handler: str
    policy_number: str
    claim_amount: int
    claimant_name: str


@activity.defn(name="receive_claim")
async def receive_claim(
    input: ReceiveClaimInput,
) -> ReceiveClaimOutput:
    """
    Step 1: Receive Claim Request,
    """
    print(f"--- Run receive_claim, {input = } ---")
    claim_id = f"CLAIM-{random.randint(1000, 9999)}"
    # Random claim handler assignment
    claim_handler = random.choice(["Alice", "Bob", "Charlie"])
    output = ReceiveClaimOutput(
        claim_id=claim_id,
        claim_handler=claim_handler,
        policy_number=input.policy_number,
        claim_amount=input.claim_amount,
        claimant_name=input.claimant_name,
    )
    print(f"{output = }")
    return output
