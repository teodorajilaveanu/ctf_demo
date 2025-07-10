f = open('./msg.enc', 'r')
enc = f.read()
f.close()
enc = bytes.fromhex(enc)
flag = []

for e in enc:
	flag.append((e - 18) * pow(123, -1, 256) % 256)

print(''.join([chr(f) for f in flag]))