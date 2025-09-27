# This file marks this directory as a Python package.





# your-project/                   ← Root directory
# ├── setup.py                    ← Here (or pyproject.toml)
# ├── README.md
# ├── LICENSE
# ├── requirements.txt
# ├── MANIFEST.in                 ← Include/exclude files for distribution
# ├── .gitignore
# ├── CHANGELOG.md
# ├── docs/
# ├── tests/
# └── forecasting_framework/      ← Your actual package
#     ├── __init__.py
#     ├── core/
#     ├── models/
#     └── utils/


# Architectural Changes:
# Modular Structure: Separated concerns into distinct modules
# Abstract Base Classes: Defined clear interfaces for extension
# Plugin System: Made components easily swappable and extendable
# Configuration Validation: Added Pydantic for type safety
# Factory Pattern: Centralized component creation

# Distribution Changes:
# setup.py: Proper packaging for PyPI
# Entry Points: CLI tools for easy usage
# Documentation: Examples and usage guides
# Testing: Comprehensive test suite
# Type Hints: Full type annotation support

# User Experience Improvements:
# Easy Extension: Simple decorators for adding custom components
# Configuration Flexibility: YAML/JSON support with validation
# CLI Interface: Command-line access for automation
# Examples: Ready-to-use examples for common scenarios