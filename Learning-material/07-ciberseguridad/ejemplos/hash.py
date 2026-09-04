import bcrypt
password = b"secreto123"

# NUNCA guardar la contraseña en texto plano. Se guarda un hash con sal.
hash1 = bcrypt.hashpw(password, bcrypt.gensalt())
hash2 = bcrypt.hashpw(password, bcrypt.gensalt())
print("misma contraseña, hash 1:", hash1.decode()[:52], "...")
print("misma contraseña, hash 2:", hash2.decode()[:52], "...")
print("-> distintos, por la sal aleatoria. Eso frena las 'rainbow tables'.")
print()
print("verificar login correcto:", bcrypt.checkpw(b"secreto123", hash1))
print("verificar login incorrecto:", bcrypt.checkpw(b"otra_clave", hash1))
