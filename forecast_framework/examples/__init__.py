# Documentation & Examples
"""
Examples for users to understand how to use the library
"""

def example_custom_component():
    """Example of creating a custom data preparator"""
    from ..core.base_classes import DataPreparatorInterface
    from ..core.registry import register_component
    
    @register_component('data_preparator', 'my_custom_preparator')
    class MyCustomPreparator(DataPreparatorInterface):
        def prepare_data(self, raw_data):
            # Your custom logic here
            return processed_data

def example_usage():
    """Example of using the framework"""
    from .core.framework import ForecastingFramework
    from .utils.config_loader import ConfigLoader
    
    config = ConfigLoader.load_config('my_config.yaml')
    framework = ForecastingFramework(config)
    
    results = framework.run_forecast_pipeline('healthcare')
    return results