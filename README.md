# CatchPhish 🐟🔍
A lightweight phishing detection system

---

## Overview
CatchPhish is a project aimed at detecting and preventing phishing attempts in a simple, accessible way.  
The goal is to provide users with a tool that can quickly analyze a URL or message and flag potential risks.

---

## Features

CatchPhish combines **rule-based detection** with a **Random Forest machine learning model** to identify phishing URLs.

### Rule-Based Detection
- Suspicious keywords
- Abnormal URL structures
- Presence of "@"
- Long or obfuscated URLs

### Machine Learning Detection
- Random Forest classifier trained on phishing datasets
- Predicts whether a URL is legitimate or phishing
- Complements rule-based checks by identifying more subtle patterns

This makes CatchPhish not only rule-aware but also adaptive and intelligent.

---

## Tech Stack
- **Frontend/UI**: Simple web interface (in progress with styling)  
- **Backend**: Flask (for handling user inputs and predictions)  
- **Detection Engine**:  
  - Rule-based detection (currently live)  
  - Machine learning model (Random Forest)  

---

## Usage
1. Enter a URL or text you want to check.  
2. CatchPhish analyzes it against phishing detection rules.  
3. You get a quick safety verdict.  
