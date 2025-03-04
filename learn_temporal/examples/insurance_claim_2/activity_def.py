# -*- coding: utf-8 -*-

import typing as T
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


@dataclasses.dataclass
class VerifyClaimOutput:
    receive_claim_output: ReceiveClaimOutput
    approved: bool


@activity.defn(name="verify_claim")
async def verify_claim(
    input: ReceiveClaimOutput,
) -> VerifyClaimOutput:
    """Step 2: Verify Claim"""
    print(f"--- Run receive_claim, {input = } ---")
    is_approved = (
        input.claim_amount < 5000
    )  # Simple rule: Auto-approve claims under $5000
    output = VerifyClaimOutput(
        receive_claim_output=input,
        approved=is_approved,
    )
    print(f"{output = }")
    return output


@dataclasses.dataclass
class ProcessPayoutOutput:
    verify_claim_output: VerifyClaimOutput
    payment_id: T.Optional[str]


@activity.defn(name="process_payout")
async def process_payout(
    input: VerifyClaimOutput,
) -> ProcessPayoutOutput:
    """Step 3: Process Payout"""
    print(f"--- Run process_payout, {input = } ---")
    if input.approved:
        payment_id = f"PAYMENT-{random.randint(1000, 9999)}"
        output = ProcessPayoutOutput(verify_claim_output=input, payment_id=payment_id)
    else:
        output = ProcessPayoutOutput(verify_claim_output=input, payment_id=None)
    print(f"{output = }")
    return output
