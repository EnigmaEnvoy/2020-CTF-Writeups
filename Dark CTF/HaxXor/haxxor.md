# haxXor (Cryptography)  
  
  
> you either know it or not take this and get your flag  
> `5552415c2b3525105a4657071b3e0b5f494b034515`  
  
  
We know that the challenge is related to XOR from the title. We need to find the key used for the XOR operation in order to reverse it.  
  
We know that the first 8 characters of the flag are `darkCTF{`.  
If we XOR the first 16 characters in the HEX string with `darkCTF{`, we get `1337hack`.  
  
![key check](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/HaxXor/key_check.png)  
This is the recurring key. Hence, we XOR the entire HEX string with `1337hack1337hack1337h`, which gives the flag.  
  
![solution](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/HaxXor/solution.png)  
  
  
### Flag
`darkCTF{kud0s_h4xx0r}`
