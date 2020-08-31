# Welcome Reverser (Reverse Engineering)

> Hello and welcome to FwordCTF2k20. Let's start with something to warmup GOOD LUCK and have fun.

Along with the message, an ELF file and a netcat link was provided.  
When connected to the link, the following message was displayed:

> Hello give me the secret number so i can get the flag:  
  
  
Analysing the ELF file tells us that the secret number is a 16 digit one. On further analysis, we conclude that the secret number required to get the flag is **8888888888888888**.  
On entering this number, we get the flag.  
  
  
### Flag
`FwordCTF{luhn!_wh4t_a_w31rd_n4m3}`
