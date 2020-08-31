# Secret Array (Misc)

> There was no description given for this challenge. Just a link to connect to using netcat.

Once we connect to the link, the following message was shown:

> I have a 1337 long array of secret positive integers. The only information I can provide is the sum of two elements. You can ask for that sum up to 1337 times by specifing two different indices in the array.
>
> [!] - Your request should be in this format : "i j". In this case, I'll respond by arr[i]+arr[j]
>
> [!] - Once you figure out my secret array, you should send a request in this format: "DONE arr[0] arr[1] ... arr[1336]"
>
> [\*] - Note 1: If you guessed my array before 1337 requests, you can directly send your DONE request.  
> [\*] - Note 2: The DONE request doesn't count in the 1337 requests you are permitted to do.  
> [\*] - Note 3: Once you submit a DONE request, the program will verify your array, give you the flag if it's a correct guess, then automatically exit.  
  
    
The basic idea to solve this challenge is to find out one element (preferably the first one) so that all consecutive elements can be easily found using their sum with the first element.  
In order to do that, we first get the sum of the first and second elements (sum_12), sum of the first and third elements (sum_13), and sum of the second and third elements (sum_23). Using these 3, we find out first, second and third elements.  
After that, we get the sum between first and the remaining 1334 elements and calculate all of them.  
  
  
The complete payload is in the file: [solve.py](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Fword%20CTF/Secret%20Array/solve.py)  

### Flag
`FwordCTF{it_s_all_about_the_math}`
