from pwn import *

conn = remote('secretarray.fword.wtf', 1337)
print (conn.recv() )

secr_array = []

conn.sendline("0 1")
sum_12 = int(conn.recvline())

conn.sendline("0 2")
sum_13 = int(conn.recvline())

conn.sendline("1 2")
sum_23 = int(conn.recvline())

secr_array.append((sum_12 + sum_13 - sum_23)//2)
secr_array.append(sum_12 - secr_array[0])
secr_array.append(sum_13 - secr_array[0])

print (secr_array)

for i in range(3, 1337):
  conn.sendline("0 "+str(i))
  x = int(conn.recvline())
  print (str(i)+' : '+str(x))
  secr_array.append(x - secr_array[0])

print (len(secr_array))

arr = ''
for i in range(1337):
	arr += (str(secr_array[i])+' ')
conn.sendline("DONE "+arr)
print (conn.recvline())
