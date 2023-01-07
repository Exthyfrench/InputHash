import hashlib

def hash_input(input_str):
    hash_object = hashlib.sha256()
    hash_object.update(input_str.encode('utf-8'))
    return hash_object.hexdigest()

input_str = input("Enter the input to be hashed: ")
hashed_input = hash_input(input_str)
print("Hash:", hashed_input)
