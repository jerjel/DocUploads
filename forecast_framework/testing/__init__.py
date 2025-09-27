# Testing Framework
import pytest
from unittest.mock import Mock, patch
from ..core.framework import ForecastingFramework

class TestFramework:
    def test_framework_initialization(self):
        # Test framework can be initialized
        framework = ForecastingFramework(mock_config)
        assert framework is not None
    
    def test_domain_pipeline_creation(self):
        # Test domain-specific pipeline creation
        framework = ForecastingFramework(mock_config)
        pipeline = framework.create_domain_pipeline('test_domain')
        assert pipeline is not None

# forecasting_framework/testing/fixtures.py
import pytest
from ..utils.config_loader import FrameworkConfig

@pytest.fixture
def mock_config():
    return FrameworkConfig(
        framework={'logging_level': 'DEBUG'},
        domains={'test': {'model': {'name': 'default'}}}
    )