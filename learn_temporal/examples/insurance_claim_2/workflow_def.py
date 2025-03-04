# -*- coding: utf-8 -*-

import typing as T
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from .activity_def import (
        ReceiveClaimInput,
        ReceiveClaimOutput,
        receive_claim,
        VerifyClaimOutput,
        verify_claim,
        ProcessPayoutOutput,
        process_payout,
    )


@workflow.defn(name="insurance_claim_workflow")
class InsuranceClaimWorkflow:
    @workflow.run
    async def run(
        self,
        receive_claim_input: ReceiveClaimInput,
    ) -> ProcessPayoutOutput:
        receive_claim_output = await workflow.execute_activity(
            receive_claim,
            receive_claim_input,
            start_to_close_timeout=timedelta(seconds=10),
        )
        verify_claim_output = await workflow.execute_activity(
            verify_claim,
            receive_claim_output,
            start_to_close_timeout=timedelta(seconds=10),
        )
        process_payout_output = await workflow.execute_activity(
            process_payout,
            verify_claim_output,
            start_to_close_timeout=timedelta(seconds=10),
        )
        return process_payout_output
