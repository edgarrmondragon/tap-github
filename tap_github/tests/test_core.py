"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_github.tap import TapGitHub
from .fixtures import repo_list_config, search_config

# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests_for_search_mode(search_config):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapGitHub, config=search_config)
    for test in tests:
        test()


def test_standard_tap_tests_for_repo_list_mode(repo_list_config):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapGitHub, config=repo_list_config)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
