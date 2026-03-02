import json
from utils import sha256

class Transaction:
    """Represents a blockchain transaction."""

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        """Convert transaction to dictionary."""
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def hash(self):
        """Return transaction hash."""
        return sha256(json.dumps(self.to_dict(), sort_keys=True))
