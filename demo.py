#!/usr/bin/env python3
"""Demo script to test the bug drawing functionality."""

import sys
sys.path.insert(0, 'src')

from safe_chain_pi_test import draw_bug, print_bug

print("Testing bug drawing functionality:")
print("-" * 40)
print_bug()
print("-" * 40)
print("Bug art as string:")
print(repr(draw_bug()))
