from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction
from miner import Miner

def main():
    # Initialize blockchain
    blockchain = Blockchain()
    miner = Miner(blockchain)

    # Create wallets
    alice = Wallet()
    bob = Wallet()

    # Create transaction
    tx = Transaction(alice.get_address(), bob.get_address(), 10)
    blockchain.add_transaction(tx)

    # Mine block
    mined_block = miner.mine(alice.get_address())

    print("Block mined:")
    print(mined_block)

if __name__ == "__main__":
    main()
