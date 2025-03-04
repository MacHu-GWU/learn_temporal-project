# -*- coding: utf-8 -*-

import asyncio

from temporalio.client import Client

from learn_temporal.examples.insurance_claim_1.workflow_def import (
    ReceiveClaimInput,
    InsuranceClaimWorkflow,
)


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        InsuranceClaimWorkflow.run,
        arg=ReceiveClaimInput(
            policy_number="p-123456789",
            claim_amount=1000,
            claimant_name="John Doe",
        ),
        id="insurance-claim-workflow-1",
        task_queue="task-queue-1",
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
