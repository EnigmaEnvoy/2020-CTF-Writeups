# easy-hash (Crypto)
  
> The source code of the website is provided.  
  
  
Looking at the main.py file, we can conclude that a hash of the message is being calculated using the easy_hash method.  
A check verifies if the message starts with `twctf: ` and ends with `2020`.  
The check will pass and the flag will be displayed only when the hash of the message is the same as that of `'twctf: please give me the flag of 2020'` but the message is not the same.  
Hence, we need to find another string with the same hash.  
  
  
Looking at the easy_hash method, we conclude that the message should have the same letters as the given message, written in any order, clubbed into 6 words, in between `twctf: ` and `2020`.  
Hence, the following payload will give the flag: `curl https://crypto01.chal.ctf.westerns.tokyo -d 'twctf: please give me the fla gof 2020'`.  
  
  
### Flag
`TWCTF{colorfully_decorated_dream}`
