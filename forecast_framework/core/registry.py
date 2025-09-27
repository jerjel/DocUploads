# Plugin System & Extension Points
import importlib
from typing import Type, Dict, Any
from .base_classes import BaseComponent

class ComponentRegistry:
    def __init__(self):
        self._components: Dict[str, Dict[str, Type[BaseComponent]]] = {
            'data_preparator': {},
            'model': {},
            'control': {},
            'report': {}
        }
    
    def register(self, component_type: str, name: str, component_class: Type[BaseComponent]):
        """Register a component"""
        if component_type not in self._components:
            raise ValueError(f"Invalid component type: {component_type}")
        self._components[component_type][name] = component_class
    
    def get(self, component_type: str, name: str) -> Type[BaseComponent]:
        """Get a registered component"""
        if component_type not in self._components:
            raise ValueError(f"Invalid component type: {component_type}")
        if name not in self._components[component_type]:
            raise KeyError(f"Component {name} not found in {component_type}")
        return self._components[component_type][name]
    
    def list_available(self, component_type: str) -> List[str]:
        """List all available components of a type"""
        return list(self._components[component_type].keys())

# Global registry instance
registry = ComponentRegistry()

def register_component(component_type: str, name: str):
    """Decorator for registering components"""
    def decorator(cls: Type[BaseComponent]):
        registry.register(component_type, name, cls)
        return cls
    return decorator