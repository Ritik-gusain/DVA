import hashlib
import json
from time import time
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)
blockchain = Blockchain()

# New home route to prevent 404 errors
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Blockchain API!'}), 200

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = last_block['proof'] + 1
    previous_hash = hashlib.sha256(json.dumps(last_block, sort_keys=True).encode()).hexdigest()
    block = blockchain.create_block(proof, previous_hash)
    return jsonify(block), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify(blockchain.chain), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
