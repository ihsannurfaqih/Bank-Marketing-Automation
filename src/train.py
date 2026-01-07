import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold

# model imports
import xgboost as xgb

from sklearn.inspection import permutation_importance

from sklearn.metrics import classification_report, recall_score, precision_score, f1_score

import matplotlib.pyplot as plt
import seaborn as sns
import joblib

pd.options.display.max_columns = 100

# import data
df = pd.read_csv("../data/train.csv", sep=";")

# map y to 0 and 1
df['y'] = df['y'].map({'yes':1, 'no':0})

# define feature
numeric_features = [
    'age',
    'duration',
    'campaign',
    'emp.var.rate',
    'cons.conf.idx',
    'euribor3m',
    'nr.employed'
]

categorical_features = [
    'job',
    'marital',
    'education',
    'default',
    'contact',
    'poutcome'
]

# split data
X_train, X_val, y_train, y_val = train_test_split(
    df[numeric_features + categorical_features].copy(),
    df['y'].copy(),
    test_size=0.2,
    random_state=42,
    stratify=df['y']
)

scale_pos_weight = sum(y_train == 0) / sum(y_train == 1)

final_model = Pipeline(steps=[
    ('vectorizer', DictVectorizer()),
    ('classifier', xgb.XGBClassifier(
        scale_pos_weight = scale_pos_weight
        , random_state = 42
        , subsample = 1.0
        , reg_lambda = 3
        , reg_alpha = 0.1
        , n_estimators = 300
        , min_child_weight = 1
        , max_depth = 6
        , learning_rate = 0.01
        , colsample_bytree = 0.6
    )
    )
])

print("Training model started...")
model = final_model.fit(X_train.to_dict(orient='records'), y_train)
print("Training model completed.")

print("Exporting The Model")
joblib.dump(final_model, '../model/best_model.bin', compress=3)
print("Model Exported")