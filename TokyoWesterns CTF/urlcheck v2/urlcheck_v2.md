# urlcheck v2 (Web)

> This challenge is similar to urlcheck v1. We need to access the internal network to get the flag. However, it is made harder in this problem.

According to [app.py](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/TokyoWesterns%20CTF/urlcheck%20v2/app.py), we have to access `127.0.0.1/admin-status` this time too. But, in v2, [ipaddress.is_global](https://docs.python.org/3/library/ipaddress.html) in Python is used to check if the URL is private and block it.  
  
Following the SSRF payloads in this [link](https://github.com/brannondorsey/whonow), we can form the following payload:  
`http://A.34.192.228.43.1time.127.0.0.1.1time.repeat.rebind.network/admin-status`  
  
  
### Flag
`TWCTF{17_15_h4rd_70_55rf_m17164710n_47_4pp_l4y3r:(}`
