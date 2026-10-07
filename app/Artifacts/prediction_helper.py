from joblib import load
import pandas as pd

model_young = load('app/Artifacts/model_young.joblib')
model_rest = load('app/Artifacts/model_rest.joblib')

scaler_young = load('app/Artifacts/scaler_young.joblib')
scaler_rest = load('app/Artifacts/scaler_rest.joblib')













def predict():
    pass