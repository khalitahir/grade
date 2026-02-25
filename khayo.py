import hashlib
def hash_password(passwod):
    hash_opj = hashlib.sha256()
    hash_opj.update(passwod.encode('utf-8'))
    return hash_opj.hexdigest()

password = 'K_tahiR'
hashed_password = hash_password(password)
print(hashed_password)