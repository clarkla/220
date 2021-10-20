def encode(message, key):
    encoded = []
    for i in message:
        shift = ord(i) + key
        encoded.append(chr(shift))
    return "".join(encoded)