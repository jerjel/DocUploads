# Configuration System
from typing import Dict, Any
from pydantic import BaseModel, ValidationError
import yaml
import json
from pathlib import Path

class FrameworkConfig(BaseModel):
    """Validated configuration model"""
    framework: Dict[str, Any]
    domains: Dict[str, Dict[str, Any]]
    logging: Dict[str, Any] = {"level": "INFO"}
    
    class Config:
        extra = "allow"

class ConfigLoader:
    @staticmethod
    def load_config(config_path: str) -> FrameworkConfig:
        """Load and validate configuration"""
        path = Path(config_path)
        
        if path.suffix.lower() in ['.yaml', '.yml']:
            with open(path, 'r') as f:
                config_dict = yaml.safe_load(f)
        elif path.suffix.lower() == '.json':
            with open(path, 'r') as f:
                config_dict = json.load(f)
        else:
            raise ValueError(f"Unsupported config format: {path.suffix}")
        
        try:
            return FrameworkConfig(**config_dict)
        except ValidationError as e:
            raise ValueError(f"Invalid configuration: {e}")

# forecasting_framework/core/configurable.py
from abc import ABC
from typing import Dict, Any

class ConfigurableMixin(ABC):
    """Mixin for configurable components"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self._validate_config()
    
    def _validate_config(self):
        """Validate configuration - to be overridden by subclasses"""
        pass
    
    def update_config(self, new_config: Dict[str, Any]):
        """Update configuration"""
        self.config.update(new_config)
        self._validate_config()