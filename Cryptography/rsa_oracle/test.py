from pwn import *

C2 = 2336150584734702647514724021470643922433811330098144930425575029773908475892259185520495303353109615046654428965662643241365308392679139063000973730368839
M1 = 25

p = remote("titan.picoctf.net", 57208)

p.recvuntil(b"decrypt.")
p.sendline(b"E")
p.recvuntil(b"keysize): ")
p.sendline(M1.to_bytes(1, "big")) # M1 codificado
p.recvuntil(b"mod n) ")

C1 = int(p.recvline())

p.sendline(b"D")
p.recvuntil(b"decrypt: ")
p.sendline(str(C1*C2).encode())
p.recvuntil(b"mod n): ")

password = int(p.recvline(), 16) // M1 #Indicamos que se recibe en formato hexadecimal (16) y quitamos el M1 que hemos añadido
M2 = password.to_bytes(len(str(password))-7, "big").decode("utf-8") #Convertimos el valor numérico a texto

print("Contraseña:", M2)