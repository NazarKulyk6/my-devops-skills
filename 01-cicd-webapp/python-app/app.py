from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Python DevOps App!',
        'version': '1.0.1',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/info')
def info():
    return jsonify({
        'app': 'Python DevOps App',
        'version': '1.0.1',
        'status': 'running',
        'endpoints': ['/', '/health', '/info']
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
