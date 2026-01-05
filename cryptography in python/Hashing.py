import hashlib
import os
import hmac

def hash_password(password:str, salt:str='')->str:
    if salt == '':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        return hashlib.sha256((password+salt).encode()).hexdigest()

def check_db_password(password:str,hash:str, salt:str = '' ) -> bool:
    #retrieve hash from DB
    db_hash = hash_password(password=password,salt=salt)

    if(hmac.compare_digest(hash, db_hash)):
        return True

    return False

salt = os.urandom(12)
password = "hash me!"
hash = hashlib.sha256(password.encode()).hexdigest()
salted_hash = hashlib.sha256((password+str(salt)).encode()).hexdigest()

print(check_db_password(password=password, hash=hash))
print(check_db_password(password=password, hash=salted_hash, salt=str(salt)))
