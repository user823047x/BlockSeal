import time
from utils import hash_block

class Blockchain:
    """Simple Blockchain implementation."""

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the chain."""
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "transactions": [],
            "previous_hash": "0",
            "nonce": 0
        }
        genesis_block["hash"] = hash_block(genesis_block)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        """Add new transaction to pending transactions."""
        self.pending_transactions.append(transaction.to_dict())

    def mine_block(self):
        """Mine a block using proof-of-work."""
        block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "transactions": self.pending_transactions,
            "previous_hash": self.chain[-1]["hash"],
            "nonce": 0
        }

        computed_hash = hash_block(block)

        # Proof-of-Work algorithm
        while not computed_hash.startswith("0" * self.difficulty):
            block["nonce"] += 1
            computed_hash = hash_block(block)

        block["hash"] = computed_hash
        self.chain.append(block)
        self.pending_transactions = []

        return block
