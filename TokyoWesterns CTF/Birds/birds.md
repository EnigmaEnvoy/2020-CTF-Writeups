# Birds (Misc)

> TWCTF{  
> BC552  
> AC849  
> JL106  
> PQ448  
> JL901  
> LH908  
> NH2177  
> }  
>  
> It will be a proper sentence.  
> Flag format is /^TWCTF{[A-Z]+}$/  
  
  
The codes provided are flight numbers connecting the following airports:  
* BC552: OKA -> NGO (Okinawa to Nagoya)  
* AC849: LHR -> YYZ (London to Toronto)  
* JL106: ITM -> HND (Osaka to Tokyo)  
* PQ448: TBS -> ODS (Tbilisi to Odesa)  
* JL901: HND -> OKA (Tokyo to Okinawa)  
* LH908: FRA -> LHR (Frankfurt to London)  
* NH2177: NRT -> ITM (Tokyo to Osaka)  
  
  
As we can see, there are certain flights, which when put together, form routes connecting various airports.  
Three such routes are formed with the flights given:  

* FRA -> LHR -> YYZ
* TBS -> ODS
* NRT -> ITM -> HND -> OKA -> NGO  
  
The first letters of the airports in the three routes put together gives the flag.  
  
  
### Flag
`TWCTF{FLYTONIHON}`
