# Factory Pattern Implementation
from typing import Type, Dict, Any
from .registry import registry
from .base_classes import BaseComponent

class ComponentFactory:
    @staticmethod
    def create_component(
        component_type: str, 
        name: str, 
        config: Dict[str, Any] = None
    ) -> BaseComponent:
        """Factory method to create components"""
        component_class = registry.get(component_type, name)
        
        if config is None:
            return component_class()
        else:
            return component_class(config)
    
    @staticmethod
    def create_domain_pipeline(domain_config: Dict[str, Any]) -> 'ForecastingPipeline':
        """Create a complete pipeline for a domain"""
        pipeline = ForecastingPipeline()
        
        # Create data preparator
        prep_config = domain_config.get('data_preparator', {})
        prep_name = prep_config.get('name', 'default')
        pipeline.data_preparator = ComponentFactory.create_component(
            'data_preparator', prep_name, prep_config.get('config')
        )
        
        # Create model
        model_config = domain_config.get('model', {})
        model_name = model_config.get('name', 'default')
        pipeline.model = ComponentFactory.create_component(
            'model', model_name, model_config.get('config')
        )
        
        # Create controls
        for control_config in domain_config.get('controls', []):
            control = ComponentFactory.create_component(
                'control', 
                control_config['name'], 
                control_config.get('config')
            )
            pipeline.add_control(control)
        
        return pipeline