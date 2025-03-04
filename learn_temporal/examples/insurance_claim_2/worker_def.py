import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from .activity_def import receive_claim, verify_claim, process_payout
from .workflow_def import InsuranceClaimWorkflow


async def insurance_claim_worker():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="task-queue-1",
        workflows=[
            InsuranceClaimWorkflow,
        ],
        activities=[
            receive_claim,
            verify_claim,
            process_payout,
        ],
    )
    await worker.run()
