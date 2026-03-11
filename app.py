from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location')
def get_location():
    return jsonify({
        "campus": "IIIT Kottayam",
        "location": "Vallichira, Kerala, India",
        "latitude": 9.7564,
        "longitude": 76.6494,
        "status": "Active"
    })

if __name__ == '__main__':
    # Listen on all interfaces so Kubernetes can route traffic to it
    app.run(host='0.0.0.0', port=5000)
