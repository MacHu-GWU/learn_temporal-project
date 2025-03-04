# -*- coding: utf-8 -*-

from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from .activity_def import (
        ReceiveClaimInput,
        ReceiveClaimOutput,
        receive_claim,
    )


@workflow.defn(name="insurance_claim_workflow")
class InsuranceClaimWorkflow:
    @workflow.run
    async def run(
        self,
        receive_claim_input: ReceiveClaimInput,
    ) -> ReceiveClaimOutput:
        return await workflow.execute_activity(
            receive_claim,
            receive_claim_input,
            start_to_close_timeout=timedelta(seconds=10),
        )
