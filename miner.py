class Miner:
    """Handles mining rewards."""

    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine(self, reward_address):
        """Mine pending transactions and reward miner."""
        block = self.blockchain.mine_block()

        reward_transaction = {
            "sender": "NETWORK",
            "recipient": reward_address,
            "amount": 1
        }

        self.blockchain.pending_transactions.append(reward_transaction)
        return block
