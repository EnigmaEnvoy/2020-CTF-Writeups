# Memory3 (Forensics)  
  
  
> He sent me a secret file , can you recover it ?
>
> PS: NO BRUTEFORCE NEEDED FOR THE PASSWORD  
  
  
When the strings command is run on the raw file in [Memory2](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Fword%20CTF/Memory/Memory2/memory2.md), we observe a gofile link which contains a zip file.  
We also come across a password: `fw0rdsecretp4ss`, using which we can open the zip file and retrieve an image which contains the flag.  
  
  
### Flag
`FwordCTF{dont_share_secrets_on_public_channels}`
