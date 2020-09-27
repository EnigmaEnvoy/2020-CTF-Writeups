# WEIRD ENCRYPTION (Cryptography)  
  
> I made this weird encryption I hope you can crack it.  
> A file with the [encrypted text]() and another with the [encryption algorithm]() were also provided.  
  
  
According to enc.py, the encryption considers each letter of the flag and divides the ASCII value of the letter by 16. The quotient and remainder values after the division determine which phrases from a main_string are added to the encrypted text.  
In order to crack the encryption, we need to separate each phrase added for the quotient and remainder from the encrypted text. The index of the phrase added after division is multiplied by 16 and added to the index of the phrase added after mod. This will give us the ASCII value of the character in the plain text.  
A [python code]() was written to crack it.  
  
  
### Flag
`DarkCTF{0k@y_7h15_71m3_Y0u_N33d_70_Br3@k_M3}`
