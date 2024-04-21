import secrets

# Generate a secure random secret key
secret_key = secrets.token_hex(16)  # Generate a 32-character hexadecimal string (16 bytes)

print(secret_key)
