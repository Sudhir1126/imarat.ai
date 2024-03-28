# deepar_forecasting.py

import pandas as pd
from gluonts.model.deepar import DeepAREstimator
from gluonts.dataset.common import ListDataset
from gluonts.evaluation.backtest import make_evaluation_predictions
from gluonts.evaluation import Evaluator

# Sample data (replace with actual data)
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'value': [10, 20, 30, 25, 35] * 20  # Sample asset depletion levels
})

# Convert data to GluonTS-compatible format
training_data = ListDataset([{
    "start": data["timestamp"].min(),
    "target": data["value"].values,
    "feat_static_cat": [0],  # Placeholder category
}], freq="D")

# Define and train DeepAR estimator
estimator = DeepAREstimator(freq="D", prediction_length=7, trainer={"epochs": 10})
predictor = estimator.train(training_data=training_data)

# Make predictions
forecast_it, ts_it = make_evaluation_predictions(
    dataset=training_data, predictor=predictor, num_samples=100
)

# Evaluate predictions
evaluator = Evaluator(quantiles=[0.1, 0.5, 0.9])
agg_metrics, item_metrics = evaluator(iter(ts_it), iter(forecast_it), num_series=len(training_data))

print(agg_metrics)
