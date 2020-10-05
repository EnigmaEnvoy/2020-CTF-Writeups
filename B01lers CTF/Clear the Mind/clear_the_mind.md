# Clear the Mind (Crypto)  
  
  
> They've gotten into your mind, but haven't managed to dive that deep yet. Root them out before it becomes an issue.  
> Another text file was given which n, c and e values.  
  
  
Looking at the text file, we realise that the values n, c and e correspond to the modulus, ciphertext and public key of RSA respectively.  
The value of e is very small (3) and that of n is very large. Hence, we can safely assume that the plaintext cubed would not be greater than n.  
  
  
Therefore, to get the plaintext, we need to calculate the cube root of the ciphertext.  
The cube root of ciphertext: `164587995846552213349276905669580061809447554828318448024777339`  
Converting the above to hex: `666C61677B77335F6E6565645F376F5F67305F6433657033727D`  
We get the flag if we decode the hex string.  
  
  
### Flag
`flag{w3_need_7o_g0_d3ep3r}`
