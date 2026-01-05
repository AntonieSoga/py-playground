import hashlib
import os
import hmac

def hash_password(password: str, salt_hex: str = '') -> str:
    return hashlib.sha256((password + salt_hex).encode()).hexdigest()

def check_db_password(password: str, stored_hash: str, salt_hex: str = '') -> bool:
    calculated_hash = hash_password(password, salt_hex)    
    return hmac.compare_digest(stored_hash, calculated_hash)



# --- Main Execution ---

# 1. Create Salt: Use .hex() to get a clean string
salt_bytes = os.urandom(16)
salt_hex = salt_bytes.hex() 

password = "hash me!"

# 2. Create the hash to "store" in the DB
# We pass the clean hex string, not the raw bytes object
stored_hash = hash_password(password, salt_hex)

# 3. Verify
print(f"Salt used: {salt_hex}")
print(f"Hash stored: {stored_hash}")

print("Match:", check_db_password(password=password, stored_hash=stored_hash, salt_hex=salt_hex))