# Flag of Life (Misc)  
  
> Help our adventurer in attaining the Flag of Life by defeating the Demon Guard Flageon.  
  
  
When connected to the link provided, we see the following:  
  
 	  'Demon Guard Flageon: Who dares to disturb my slumber?
 	  ...
 	  A human?
 	  what is your name human?
     
 	  You: xyz
   
	  Demon Guard Flageon: Listen close, xyz.
 	  To pass through you must give me a key of certain shape and size.
	  I do not expect mere mortals to pass this test and win the Flag of Life.
 	  So here is a hint: the shape of the key is a square.
 	  But I will not tell you the size.
	  You have 3 tries!
   
	  How lucky! Look in your backpack. You have a square-key-making device.
	  huh... weird thing to carry around if you ask me.
	  Anyways.
	  The problem is the device needs the edge length as input to make the key...
   
 	  Input edge length:  
  
    
  We try various key lengths:  
    
  ![trials](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/Flag%20of%20Life/trials.png)  
  By this, we can conclude that the key length is supposed to be 0. However, the program accepts only positive integers.  
    
  Therefore, we exploit the 16-bit int property, where it considers 65536 as 0.  
    
  ![solution](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/Flag%20of%20Life/solution.png)  
    
    
  ### Flag
  `darkCTF{-2147483648_c0m3s_aft3r_2147483647}`
    
