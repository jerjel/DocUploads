from dataclasses import dataclass
from typing import Dict, List, Any
import numpy as np

@dataclass
class RegressionConfig:
    name: str
    intercept: float
    coefficients: List[float]
    feature_names: List[str]
    metadata: Dict[str, Any] = None

class LinearRegressionModel:
    def __init__(self, config: RegressionConfig):
        self.config = config
        self.intercept = config.intercept
        self.coefficients = np.array(config.coefficients)
        self.feature_names = config.feature_names
        
    def predict(self, features: List[float]) -> float:
        features_array = np.array(features)
        if len(features_array) != len(self.coefficients):
            raise ValueError(f"Expected {len(self.coefficients)} features, got {len(features_array)}")
        return self.intercept + np.dot(self.coefficients, features_array)
    
    def predict_dict(self, feature_dict: Dict[str, float]) -> float:
        # Ensure features are in correct order
        features = [feature_dict[name] for name in self.feature_names]
        return self.predict(features)

class ModelRegistry:
    def __init__(self):
        self.models: Dict[str, LinearRegressionModel] = {}
    
    def register_model(self, config: RegressionConfig):
        self.models[config.name] = LinearRegressionModel(config)
    
    def get_model(self, name: str) -> LinearRegressionModel:
        return self.models[name]
    
    def load_from_json(self, config_path: str):
        # Load multiple model configurations from JSON/YAML
        pass



# # Usage Example:

# # Define models via configuration
# pricing_config = RegressionConfig(
#     name="pricing_model",
#     intercept=10.5,
#     coefficients=[2.1, -0.8, 1.3],
#     feature_names=["age", "income", "experience"]
# )

# risk_config = RegressionConfig(
#     name="risk_model", 
#     intercept=0.2,
#     coefficients=[0.05, -0.02, 0.1],
#     feature_names=["debt_ratio", "payment_history", "credit_age"]
# )

# # Register and use
# registry = ModelRegistry()
# registry.register_model(pricing_config)
# registry.register_model(risk_config)

# # Make predictions
# price = registry.get_model("pricing_model").predict([25, 50000, 3])
# risk_score = registry.get_model("risk_model").predict_dict({
#     "debt_ratio": 0.3, 
#     "payment_history": 0.9, 
#     "credit_age": 5
# })