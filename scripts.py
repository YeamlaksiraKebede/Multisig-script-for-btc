from bitcoin.wallet import CBitcoinSecret
from bitcoin.core.script import CScript
from bitcoin.wallet import P2PKHBitcoinAddress

# Define opcode values
OP_CHECKSIGADD = 147
OP_CHECKSIG = 172
OP_SWAP = 124
OP_NUMEQUAL = 156

# Generate keys for borrower, lender, and oracle
borrower_key = CBitcoinSecret.from_secret_bytes(b'AliceSecretAliceSecretAliceSecr')
lender_key = CBitcoinSecret.from_secret_bytes(b'BobSecretBobSecretBobSecretBobSec')
oracle_key = CBitcoinSecret.from_secret_bytes(b'OracleSecretOracleSecretOracleS')

# Convert public keys to Bitcoin addresses
borrower_pubkey = P2PKHBitcoinAddress.from_pubkey(borrower_key.pub)
lender_pubkey = P2PKHBitcoinAddress.from_pubkey(lender_key.pub)
oracle_pubkey = P2PKHBitcoinAddress.from_pubkey(oracle_key.pub)

print("Borrower Public Key:", borrower_pubkey)
print("Lender Public Key:", lender_pubkey)
print("Oracle Public Key:", oracle_pubkey)

# Script for Multisig Address Creation
multisig_script = CScript([borrower_pubkey, lender_pubkey, oracle_pubkey, OP_CHECKSIGADD, OP_CHECKSIGADD, 2, OP_NUMEQUAL])

print("Multisig Script:", multisig_script.hex())

# Locking Script
# Note: In a real-world scenario, borrower_sig and lender_sig would be signatures created by the borrower and lender respectively.
# For this example, we will use placeholders for these signatures.
borrower_sig_placeholder = b'borrower_sig_placeholder'
lender_sig_placeholder = b'lender_sig_placeholder'

locking_script = CScript([borrower_sig_placeholder, lender_sig_placeholder, oracle_pubkey, OP_CHECKSIG, OP_SWAP, OP_CHECKSIG])

print("Locking Script:", locking_script.hex())

