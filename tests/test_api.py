# -*- coding: utf-8 -*-

from learn_temporal import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_temporal.tests import run_cov_test

    run_cov_test(__file__, "learn_temporal.api", preview=False)
