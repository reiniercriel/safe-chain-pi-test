from safe_chain_pi_test import draw_bug, print_bug
import io
import sys


def test_draw_bug_returns_string():
    """Test that draw_bug returns a string."""
    result = draw_bug()
    assert isinstance(result, str)
    assert len(result) > 0
