# Smart Tech - Package Sorting Assessment

This project contains a Python solution for a technical assessment that classifies packages into shipping stacks based on size and weight.

## Problem Summary

The function `sort(width, height, length, mass)` returns:

- `STANDARD` when the package is neither bulky nor heavy
- `SPECIAL` when the package is either bulky or heavy
- `REJECTED` when the package is both bulky and heavy

A package is considered:

- **Bulky** if:
  - volume (`width * height * length`) is greater than or equal to `1,000,000`, or
  - any single dimension is greater than or equal to `150`
- **Heavy** if mass is greater than or equal to `20`

## Project Files

- `main.py` - solution implementation (`sort` function)
- `test_main.py` - test script for the solution (pytest style)

## How to Run

### 1) Run the script checks in `main.py`

```bash
python main.py
```

Expected output:

```text
All tests passed.
```

### 2) Run the dedicated test script

If needed, install pytest:

```bash
pip install pytest
```

Then run:

```bash
pytest -q
```

## Technical Assessment Reflection

I enjoyed solving this assessment because the requirements were clear and practical.  
My focus was to keep the logic readable and explicit so each rule (bulky, heavy, and final classification) is easy to verify and maintain.  
I also added dedicated tests with boundary cases to increase confidence in correctness, especially around threshold values.
