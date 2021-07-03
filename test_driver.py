"""
Test driver script for all test scripts.

Required since Python does not allow imports above top level hierarchy.
Running this script forces the top level hierarchy to be the root of
this project.
"""

import sys
import os
import argparse
from typing import Dict

import pytest

def main():
    argv = process_argv()
    test_path = argv["path"]
    core_count = os.cpu_count()
    sys.exit(pytest([test_path, "-n", str(core_count)]))

def process_argv() -> Dict[str, str]:
    if len(sys.argv) == 1:
        print("Must run test driver with exactly one command line argument",
                file=sys.stderr)
        print("Use -h or --help for help", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser("Certificate Automater Test Driver")
    parser.add_argument("path")
    argv = parser.parse_args(sys.argv[1:])
    return vars(argv)

if __name__ == "__main__":
    main()