"""Run the Codex compatibility contract from any working directory."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEST_MODULE_PATH = REPO_ROOT / "tests" / "test_codex_compat.py"


def load_contract_suite() -> unittest.TestSuite:
    module_name = "_jhulie_codex_compat_tests"
    spec = importlib.util.spec_from_file_location(module_name, TEST_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load compatibility tests from {TEST_MODULE_PATH}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return unittest.defaultTestLoader.loadTestsFromModule(module)


def main() -> int:
    suite = load_contract_suite()
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
