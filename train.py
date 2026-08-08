import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load dataset
df = pd.read_csv("dataset.csv")

# 2. Feature Extraction
# Drop and keep all other features OBSERVE THE DROP COMMAND HERE!
X = df.drop(columns=['id', 'CLASS_LABEL'])
Y = df['CLASS_LABEL']

# 3.  Engineered features
X['UrlComplexity'] = X['UrlLength'] * X['NumDots']
X['SuspiciousSigns'] = X['NumDash'] + X['AtSymbol'] + X['TildeSymbol']
X['FormRisk'] = X['InsecureForms'] + X['AbnormalFormAction'] + X['ExtFormAction']

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# 5. Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Test model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 7. Save model
joblib.dump(model, 'phishing_model.pkl')
joblib.dump(list(X.columns), 'feature_names.pkl')
print("Model and features saved!")
