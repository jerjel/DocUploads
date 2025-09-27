# setup.py (in root directory)
import os
from setuptools import setup, find_packages

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from file
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = []
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(line)
    return requirements

setup(
    # === Package Identification ===
    name="forecasting-framework",           # Package name (pip install forecasting-framework)
    version="1.0.0",                       # Version (should match your versioning)
    
    # === Author Information ===
    author="Your Name",
    author_email="your.email@company.com",
    maintainer="Your Name",
    maintainer_email="your.email@company.com",
    
    # === Package Description ===
    description="A reusable forecasting framework with domain-specific components",
    long_description=read_readme(),        # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of long description
    
    # === Project URLs ===
    url="https://github.com/your-org/forecasting-framework",
    project_urls={
        "Bug Reports": "https://github.com/your-org/forecasting-framework/issues",
        "Source": "https://github.com/your-org/forecasting-framework",
        "Documentation": "https://your-org.github.io/forecasting-framework/",
    },
    
    # === Package Contents ===
    packages=find_packages(),              # Automatically find all packages/subpackages
    # Alternative: packages=['forecasting_framework', 'forecasting_framework.core', ...]
    
    # === Package Data ===
    package_data={
        'forecasting_framework': ['data/*.json', 'templates/*.yaml'],  # Include non-Python files
    },
    include_package_data=True,             # Include files specified in MANIFEST.in
    
    # === Python Version ===
    python_requires=">=3.8",               # Minimum Python version required
    
    # === Dependencies ===
    install_requires=read_requirements(),  # Runtime dependencies
    # Alternative: install_requires=['pandas>=1.3.0', 'numpy>=1.20.0', ...]
    
    # === Optional Dependencies ===
    extras_require={
        "dev": [                           # pip install forecasting-framework[dev]
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "deployment": [                    # pip install forecasting-framework[deployment]
            "twine",
            "build",
        ],
        "visualization": [                 # pip install forecasting-framework[visualization]
            "matplotlib",
            "seaborn",
        ],
    },
    
    # === Entry Points ===
    entry_points={
        "console_scripts": [               # Creates command-line scripts
            "forecast-cli=forecasting_framework.cli:main",
            "forecast-analyze=forecasting_framework.analyze:main",
        ],
        "forecasting_framework.data_preparators": [  # Plugin system
            "healthcare=forecasting_framework.extensions.healthcare:HealthcarePreparator",
        ],
    },
    
    # === Package Classification ===
    classifiers=[
        # Development status
        "Development Status :: 4 - Beta",
        
        # Intended audience
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Operating system
        "Operating System :: OS Independent",
        
        # Python versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        
        # Topic
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    
    # === Additional Metadata ===
    keywords="forecasting, machine-learning, time-series, data-science",
    license="MIT",
)