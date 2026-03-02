import hashlib
import json

def sha256(data: str) -> str:
    """Return SHA-256 hash of given string."""
    return hashlib.sha256(data.encode()).hexdigest()

def hash_block(block: dict) -> str:
    """Create hash of a block dictionary."""
    block_string = json.dumps(block, sort_keys=True)
    return sha256(block_string)
