# Train of Thought (Crypto)
  
  
> We've managed to infiltrate Mr. Levenshtein's subconscious, but he keeps losing his train of thought! Sort out the noise and find the flag in this mess.  
> Wrap the decrypted string in flag{xxxxxxxxx} for submission.  
> A text file also was given which had some random words.  
  
  
There is a clue in the problem description which tells us that it is related to Levenshtein's distance.  
  
Calculating the Levenshtein's distance between every consecutive word in the text file (eg: between dream and dreams, dreams and fantasticalities, etc),  
we get: `1 14 15 18 7 1 14 9 26 5 4 13 9 14 4`  
  
Taking a=1 .. z=26, the above gets translated to `anorganizedmind`.  
  
  
### Flag
`flag{anorganizedmind}`
