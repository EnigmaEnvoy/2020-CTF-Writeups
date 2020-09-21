# urlcheck v1 (Web)

> A link was given to a webpage which allowed us to check any URL. We were also given the source code to the webpage.  
  
  
Analyzing [app.py](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/TokyoWesterns%20CTF/urlcheck%20v1/app.py), we can conclude that the URL we need to check to get the flag is 127.0.0.1/admin-status.  
However, the webpage does not allow us to access any private IP. Hence, we have to obfuscate the URL to pass the check and get the flag.  
  
  
Following the SSRF payloads in this [link](https://medium.com/@pravinponnusamy/ssrf-payloads-f09b2a86a8b4), we arrive at `http://0177.0.0.1/admin-status`, which gives us the flag.  
  
  
### Flag
`TWCTF{4r3_y0u_r34dy?n3x7_57463_15_r34l_55rf!}`
