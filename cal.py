import pytest
from calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    # Uncomment below once you enable the zero-division check in calculator.py
    # with pytest.raises(ValueError):
    #     divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

Tamanna Tabassum
8:58 PM (2 minutes ago)
to me

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
bin/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

The project shown in your images is the **`python-calculator-classroom`** repository. Below are the main Python files (`calculator.py` and `test_calculator.py`) matching the code structure displayed on your screen, complete with the student exercise instructions visible in the comments.

### 1. `calculator.py`
This file contains the core functions for the calculator project, including the commented-out student exercises for division and power operations as shown in the screenshots.

```python
def add(a: float | int, b: float | int) -> float | int:
    return a + b  # Return the sum to the caller.


def subtract(a: float | int, b: float | int) -> float | int:
    return a - b  # Return the difference to the caller.


def multiply(a: float | int, b: float | int) -> float | int:
    return a * b  # Return the product to the caller.


def divide(a: float | int, b: float | int) -> float | int:
    # Student exercise: enable the zero-division test, observe
    # if b == 0:  # Detect a denominator for which division is undefined.
    #     raise ValueError("Cannot divide by zero.")  # Report the error.
    return a / b  # Return a floating-point quotient for a valid denominator.


def power(base: float | int, exponent: int) -> float | int:
    # if base == 0 and exponent < 0:
    #     raise ValueError("Zero cannot have a negative exponent.")
    return base ** exponent