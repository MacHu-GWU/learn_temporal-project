# -*- coding: utf-8 -*-

import logging
import dataclasses
from datetime import timedelta

from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Params:
    greeting: str
    name: str


@activity.defn
async def say_hello(params: Params) -> str:
    message = f"{params.greeting}, {params.name}!"
    logger.info(message)
    return message


@workflow.defn(name="wf1")
class Workflow1:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello,
            Params(greeting="Hello", name=name),
            start_to_close_timeout=timedelta(seconds=10),
        )


async def main():
    # Connect to Temporal Server
    client = await Client.connect("localhost:7233")

    # Start Worker
    async with Worker(
        client,
        task_queue="my-task-queue",
        workflows=[Workflow1],
        activities=[say_hello],
    ):
        print("Worker is running. Press Ctrl+C to stop.")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
