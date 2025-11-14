import hashlib

def hash(text):
    a = hashlib.sha256()
    a.update(text.encode('utf-8'))
    return a.hexdigest()