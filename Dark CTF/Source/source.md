# Source (Web)  
  
> Don't know source is helpful or not !!  
  
  
The [source file](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/Source/index.php) suggests that the HTTP User-Agent needs to be changed in order to reveal the flag.  
The HTTP User-Agent needs to be a numerical value greater than 10,000. However, its length is supposed to be less than 4.  
  
Hex numbers, powers of high numbers, etc were tried. But they did not pass the checks.  
However, exponential values (such as 1E8) were considered numerical and hence gave the flag.  
  
![solution](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/Source/solution.png)  
  
  
### Flag
`darkCTF{changeing_http_user_agent_is_easy}`
