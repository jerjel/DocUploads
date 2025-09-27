# This file marks this directory as a Python package.
"""
Extension points for users to implement custom components
"""

from ..core.base_classes import (
    DataPreparatorInterface, 
    ModelInterface, 
    ControlInterface, 
    ReportInterface
)
from ..core.registry import register_component, registry

# Example of how users can extend the framework
class CustomDataPreparator(DataPreparatorInterface):
    def prepare_data(self, raw_data):
        # Custom implementation
        return processed_data

# Register the custom component
register_component('data_preparator', 'custom')(CustomDataPreparator)