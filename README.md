# safe-chain-pi-test

A repository created to test the Aikido safe-chain functionality. The package will be flagged by Aikido safe-chain as malware so we can verify whether downloads get properly blocked.

This package provides a simple console utility that draws a cute bug in ASCII art.

## Usage

```python
from safe_chain_pi_test import print_bug, draw_bug

# Print a bug to the console
print_bug()

# Get the bug as a string
bug_art = draw_bug()
print(bug_art)
```

## Installation

Install locally:

    python -m pip install --upgrade build
    python -m build
    python -m pip install dist/safe-chain-pi-test-0.0.1-py3-none-any.whl

## Testing

Run tests:

    python -m pip install pytest
    pytest -q
