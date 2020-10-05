from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase
import string
import re

HOST = 'chal.ctf.b01lers.com'
PORT = 2008

r = remote(HOST,PORT)

def bacon(bacon):
    bacondict = {}
    plaintext = ""
 
    bacon = bacon.lower()
    bacon = re.sub("[\W\d]", "", bacon.strip())
    for i in range(0,26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        bacondict[tmp] = chr(65+i)
 
    for i in range(0, len(bacon)//5):
        plaintext = plaintext + bacondict.get(bacon[i*5:i*5+5], ' ')
    return plaintext.lower()

def rot13(s):
    rot13Table = ''.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return s.translate(rot13Table)

def atbash(text):
    N = ord('z') + ord('a')
    ans=''
    return ans.join([chr(N - ord(s)) for s in text])

def Base64(s):
    base64_bytes = s.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()

        result = globals()[method.decode()](argument.decode())  # :)

        r.recv()
        r.sendline(result.encode())
        print (count)
        count += 1
        if count == 1000:
            print(r.recv())
            exit(0)
    
