# Abstract Base Classes & Interfaces
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class BaseConfig(BaseModel):
    """Base configuration model for validation"""
    pass

class BaseComponent(ABC):
    """Base class for all framework components"""
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass

class DataPreparatorInterface(BaseComponent):
    """Interface for domain-specific data preparators"""
    
    @abstractmethod
    def prepare_data(self, raw_data: Any) -> Any:
        pass

class ModelInterface(BaseComponent):
    """Interface for forecasting models"""
    
    @abstractmethod
    def train(self, data: Any) -> None:
        pass
    
    @abstractmethod
    def predict(self, data: Any) -> Any:
        pass

class ControlInterface(BaseComponent):
    """Interface for control components"""
    
    @abstractmethod
    def execute(self, domain: str, data: Any) -> Dict[str, Any]:
        pass

class ReportInterface(BaseComponent):
    """Interface for report generation"""
    
    @abstractmethod
    def generate(self, domain: str, data: Any) -> Dict[str, Any]:
        pass