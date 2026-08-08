
from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
import os

app = Flask(__name__)

# load model + feature order 
model = joblib.load('phishing_model.pkl')
feature_names = joblib.load('feature_names.pkl') 

#  feature extractor
def extract_features_from_text(text):
    t = text.lower()
    f = {}
    # small, strong features
    f['NumDots'] = t.count('.')
    f['UrlLength'] = len(t)
    f['NumDash'] = t.count('-')
    f['AtSymbol'] = t.count('@')
    f['NoHttps'] = 0 if 'https' in t else 1
    # engineered features
    f['UrlComplexity'] = f['UrlLength'] * f['NumDots']
    f['SuspiciousSigns'] = f['NumDash'] + f['AtSymbol']
    f['FormRisk'] = 0
    return f

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'structure.html')

@app.route('/scriptt.js')
def js():
    return send_from_directory(os.getcwd(), 'scriptt.js')

@app.route('/style.css')
def css():
    return send_from_directory(os.getcwd(), 'style.css')

@app.route('/check', methods=['POST'])
def check_email():
    data = request.get_json() or {}
    text = data.get('email', '')

    # rule-based check
    suspicious_keywords = [
        "otp", "password", "urgent", "click", ".exe", "http", "money", 
        "suspended", "reset", "verify", "account", "login", "signin"
    ]

    flagged = [w for w in suspicious_keywords if w in text.lower()]
    if flagged:
        return jsonify({'status': 'NOPE', 'reason': ', '.join(flagged)})

    # build feature dict 
    small_f = extract_features_from_text(text)
    feature_values = []
    for name in feature_names:
        feature_values.append(small_f.get(name, 0))  # default 0 if not in small_f

    X_input = pd.DataFrame([feature_values], columns=feature_names)
    pred = model.predict(X_input)[0]

    if int(pred) == 1:
        return jsonify({'status': 'NOPE', 'reason': 'ML predicted phishing'})
    else:
        return jsonify({'status': 'SAFE', 'reason': 'ML predicted safe'})

if __name__ == '__main__':
    app.run(debug=True)
