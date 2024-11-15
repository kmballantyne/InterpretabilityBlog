#%%
import shap
import numpy as np
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load data and train a model
data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier().fit(X, y)

# Create SHAP explainer and compute SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Select a sample to explain and extract relevant SHAP values
sample_index = 0
sample_shap_values = shap_values[1][sample_index]  # Adjust class index if needed
base_value = explainer.expected_value[1]
features = data.feature_names

# Prepare data for Svelte
force_plot_data = {
    "base_value": base_value,
    "shap_values": sample_shap_values.tolist(),
    "feature_names": features,
    "data_point": X[sample_index].tolist()
}

force_plot_data

# # Save to JSON file
# with open("force_plot_data.json", "w") as f:
#     json.dump(force_plot_data, f)
