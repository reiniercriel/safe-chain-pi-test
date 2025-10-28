#!/usr/bin/env python3
"""Test script to verify the safe-chain-pi-test module works correctly."""

import sys
sys.path.insert(0, 'src')

from safe_chain_pi_test import draw_bug, print_bug

print("=" * 50)
print("Testing draw_bug() function:")
print("=" * 50)
bug_art = draw_bug()
print(bug_art)

