from datetime import datetime, timedelta
import psycopg2
from flask import Flask, request, jsonify
import bcrypt
from flask_caching import Cache

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 86400})

@app.route('/teste', methods=['GET']) 
def teste():
    return jsonify({"message": "Gogh Approves"}), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.json
    cache.set(webhook, (body))
    return jsonify(body), 200

@app.route('/edit', methods=['POST'])
def webhookedit():
    body = request.json
    cache.set(webhook, (body))
    return jsonify(body), 200

@app.route('/webhook/consulta', methods=['GET'])
def consulta():
    return jsonify(cache.get(webhook))


if __name__ == '__main__':
    app.run(debug=True)
#
