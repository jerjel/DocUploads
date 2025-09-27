from abc import ABC, abstractmethod

class BaseRegressionModel(ABC):
    def __init__(self):
        self.intercept = None
        self.coefficients = []
        self.feature_names = []
    
    @abstractmethod
    def _load_coefficients(self):
        """Load model-specific coefficients"""
        pass
    
    @abstractmethod
    def _validate_features(self, features: List[float]) -> List[float]:
        """Optional feature validation/transformation"""
        return features
    
    def predict(self, features: List[float]) -> float:
        validated_features = self._validate_features(features)
        return self.intercept + sum(
            coef * feat for coef, feat in zip(self.coefficients, validated_features)
        )

class PricingModel(BaseRegressionModel):
    def _load_coefficients(self):
        self.intercept = 10.5
        self.coefficients = [2.1, -0.8, 1.3]
        self.feature_names = ["age", "income", "experience"]
    
    def __init__(self):
        super().__init__()
        self._load_coefficients()

####################################################
############### Data driven approach ###############
####################################################
import pandas as pd

class DataFrameRegressionModel:
    def __init__(self, intercept: float, coefficients: Dict[str, float]):
        self.intercept = intercept
        self.coefficients = coefficients  # {feature_name: coefficient}
    
    def predict(self, df: pd.DataFrame) -> pd.Series:
        result = pd.Series(self.intercept, index=df.index)
        for feature, coef in self.coefficients.items():
            result += coef * df[feature]
        return result

# Usage
model = DataFrameRegressionModel(
    intercept=10.5,
    coefficients={"age": 2.1, "income": -0.8, "experience": 1.3}
)

predictions = model.predict(df[["age", "income", "experience"]])        



###############################################################
############### External Config. File Structure ###############
###############################################################

{
  "models": {
    "pricing_model": {
      "intercept": 10.5,
      "coefficients": [2.1, -0.8, 1.3],
      "feature_names": ["age", "income", "experience"],
      "description": "Customer pricing model"
    },
    "risk_model": {
      "intercept": 0.2,
      "coefficients": [0.05, -0.02, 0.1],
      "feature_names": ["debt_ratio", "payment_history", "credit_age"],
      "description": "Credit risk assessment"
    }
  }
}