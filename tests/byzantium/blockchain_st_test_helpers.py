from functools import partial

from ..helpers.load_state_tests import Load, run_blockchain_st_test

FIXTURES_LOADER = Load("Byzantium", "byzantium")

run_byzantium_blockchain_st_tests = partial(
    run_blockchain_st_test, load=FIXTURES_LOADER
)