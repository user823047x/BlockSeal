from ecdsa import SigningKey, SECP256k1
import binascii

class Wallet:
    """Simple wallet using ECDSA for signing transactions."""

    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign(self, message: str) -> str:
        """Sign a message with the private key."""
        signature = self.private_key.sign(message.encode())
        return binascii.hexlify(signature).decode()

    def get_address(self) -> str:
        """Return public key as wallet address."""
        return binascii.hexlify(self.public_key.to_string()).decode()
