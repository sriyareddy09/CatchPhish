from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email', '').lower()

    suspicious_keywords = ["otp", "password", "urgent", "click", ".exe", "http", "money", "suspended", "reset"]
    flagged = [word for word in suspicious_keywords if word in email]

    if flagged:
        return jsonify({'status': 'NOPE', 'reason': ', '.join(flagged)})
    else:
        return jsonify({'status': 'SAFE', 'reason': 'No suspicious keywords found.'})

if __name__ == '__main__':
    app.run(debug=True)
