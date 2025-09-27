# setup.py
import os
from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="forecasting-framework",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@company.com",
    description="A reusable forecasting framework with domain-specific components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/forecasting-framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "tox>=3.0",
        ],
        "deployment": [
            "twine>=4.0",
            "build>=0.10",
        ],
    },
    entry_points={
        "console_scripts": [
            "forecast-cli=forecasting_framework.cli:main",
        ],
    },
)