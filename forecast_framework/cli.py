# CLI Interface
import argparse
from .core.framework import ForecastingFramework
from .utils.config_loader import ConfigLoader

def main():
    parser = argparse.ArgumentParser(description='Forecasting Framework CLI')
    parser.add_argument('--config', required=True, help='Path to configuration file')
    parser.add_argument('--domain', required=True, help='Domain to run forecasting for')
    parser.add_argument('--forecast-date', help='Forecast date (YYYY-MM-DD)')
    parser.add_argument('--dry-run', action='store_true', help='Run without saving results')
    
    args = parser.parse_args()
    
    # Load configuration
    config = ConfigLoader.load_config(args.config)
    
    # Initialize framework
    framework = ForecastingFramework(config)
    
    # Run forecasting
    results = framework.run_forecast_pipeline(
        domain=args.domain,
        forecast_date=args.forecast_date,
        dry_run=args.dry_run
    )
    
    print(f"Forecasting completed for domain: {args.domain}")
    print(f"Results: {results}")

if __name__ == "__main__":
    main()