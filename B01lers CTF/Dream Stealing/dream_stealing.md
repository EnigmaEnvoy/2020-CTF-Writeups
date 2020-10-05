# Dream Stealing (Crypto) 
  
  
> I've managed to steal some secrets from their subconscious, can you figure out anything from this?  
> A [text](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/B01lers%20CTF/Dream%20Stealing/ciphertext-bb416c708f242b0c70d6f2c07d646d9f.txt) file having Modulus, one factor of N, Public key and Ciphertext was given.  
  
  
By the parameters given in the file, we can conclude that the encryption technique used is RSA.  
  
We know that the Modulus given in the file is N. As one factor of N is given, we can find the other factor.  
The other factor: `10166627341555233885462189686170129966199363862865327417835599922534140147190891310884780246710738772334481095318744300242272851264697786771596673112818133`  
  
Calculating phi `(p-1)*(q-1)`(where p and q are the factors of N): `98570307780590287344989641660271563150943084591122129236101184963953890610515286342182643236514124325672053304374355281945455993001454145469449640602102788424913666243446115125013749894802497855425825476346571837495143781689593338561218309247406348975238353391320418652358081883392298327112356072070946617176`  
  
We can now calculate the private key by taking the modular inverse of the public key with respect to phi.  
Private key: `71019292355336569848224146505887711375625700158814041234714159220180032054227708100638146863374283786775541831015345256239719342257589808732806545609208410007110462888891498086394315520739111436827319730344824688262862111900161860529504971914388519344214410314551457166878195041761156822984243120178189851785`  
  
Using python's [pow function](https://docs.python.org/3/library/functions.html#pow), we can get (ciphertext)^private key MOD phi.  
Plain text: `46327402297734345668136112664627609061622411859278517910287191659094499226493`  
Converting plaintext to hex string: `666C61677B346363653535316E675F7468335F73756263306E7363313075737D`  
If we convert the above hex string to text, we get the flag.  
  
  
### Flag
`flag{4cce551ng_th3_subc0nsc10us}`