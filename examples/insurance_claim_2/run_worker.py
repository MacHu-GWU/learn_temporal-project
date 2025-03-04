# -*- coding: utf-8 -*-

import asyncio

from learn_temporal.examples.insurance_claim_2.worker_def import insurance_claim_worker

if __name__ == "__main__":
    asyncio.run(insurance_claim_worker())
