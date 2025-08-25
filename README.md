# CatchPhish 🐟🔍
A lightweight phishing detection system

---

## Overview
CatchPhish is a project aimed at detecting and preventing phishing attempts in a simple, accessible way.  
The goal is to provide users with a tool that can quickly analyze a URL or message and flag potential risks.

---

## Current Features (Rule-Based Detection)
Right now, CatchPhish uses a **rule-based detection system**.  
It scans inputs against a set of predefined rules such as:

- Suspicious keywords or patterns commonly used in phishing links  
- Abnormal URL structures (e.g., excessive subdomains, numeric IPs)  
- Presence of “@” or misleading domain names  
- Very long or obfuscated URLs  

These heuristics allow the system to quickly identify many known phishing techniques without requiring heavy computation.

---

## Roadmap (Underway 🚀)
The next phase of CatchPhish focuses on integrating **machine learning (ML) techniques** to enhance detection accuracy. With ML, the system will be able to:

- Learn from real phishing datasets and improve over time  
- Detect more subtle or evolving phishing strategies  
- Provide probabilistic scoring instead of just binary safe/unsafe checks  

This will make CatchPhish not only rule-aware but also adaptive and intelligent.

---

## Tech Stack
- **Frontend/UI**: Simple web interface (in progress with styling)  
- **Backend**: Flask (for handling user inputs and predictions)  
- **Detection Engine**:  
  - Rule-based detection (currently live)  
  - Machine learning models (under development)  

---

## Usage
1. Enter a URL or text you want to check.  
2. CatchPhish analyzes it against phishing detection rules.  
3. You get a quick safety verdict.  

---

## Future Work
- Deploy trained ML models for phishing classification  
- Build a clean, responsive UI for better user experience  
- Integrate notifications / browser extensions  
