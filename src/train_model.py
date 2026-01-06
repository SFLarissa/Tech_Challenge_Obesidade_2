# ============================================
# Importando bibliotecas
# ============================================

import pandas as pd
import numpy as np
from pathlib import Path
import os
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ============================================
# Caminhos do projeto (RELATIVOS)
# ============================================

BASE_DIR = Path.cwd()  # diretório onde o script é executado
DATA_PATH = BASE_DIR / "data" / "Obesity.csv"
MODEL_DIR = BASE_DIR / "model_data"
MODEL_PATH = MODEL_DIR / "pipeline.joblib"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

# ============================================
# Leitura do dataset
# ============================================

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.info())
print(df.describe())

# ============================================
# Separando target
# ============================================

X = df.drop(columns=["Obesity"])
y = df["Obesity"]

# ============================================
# Separação de colunas
# ============================================

num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns

print("Colunas numéricas:", list(num_cols))
print("Colunas categóricas:", list(cat_cols))

# ============================================
# Train / Test
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ============================================
# Pipelines
# ============================================

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, num_cols),
    ("cat", categorical_pipeline, cat_cols)
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

# ============================================
# GridSearch
# ============================================

param_grid = {
    "model__C": [0.01, 0.1, 1, 10],
    "model__solver": ["lbfgs"]
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring="accuracy",
    cv=3,
    n_jobs=-1,
    verbose=2
)

# ============================================
# Treinamento
# ============================================

grid_search.fit(X_train, y_train)

print("Melhores hiperparâmetros:")
print(grid_search.best_params_)

# ============================================
# Avaliação
# ============================================

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("Matriz de Confusão:\n")
print(confusion_matrix(y_test, y_pred))

# ============================================
# Salvando modelo com joblib
# ============================================

joblib.dump(best_model, MODEL_PATH)

print(f"\nModelo salvo com sucesso em:\n{MODEL_PATH.resolve()}")

# ============================================
# Teste de carga do modelo
# ============================================

model = joblib.load(MODEL_PATH)
print("\nModelo carregado com sucesso!")
