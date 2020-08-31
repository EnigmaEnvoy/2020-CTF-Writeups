> Flag is : FwordCTF{computername_user_password}
  
We also have a foren.raw file given with the question.  
  
  
We analyse the file using [Volatility](https://www.volatilityfoundation.org/about). The profile is Win7SP1x64.  
  
  
* In order to find the computer name:  
  
```$ volatility -f foren.raw hivelist --profile=Win7SP1x64```  
  
```
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a000b0f410 0x000000002720d410 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a000d00010 0x000000001ff75010 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a000f8b410 0x00000000175e8410 \??\C:\Windows\System32\config\COMPONENTS
0xfffff8a00145f010 0x0000000027d9b010 \SystemRoot\System32\Config\DEFAULT
0xfffff8a0014da410 0x00000000275c0410 \SystemRoot\System32\Config\SAM
0xfffff8a0033fe410 0x0000000069de6410 \??\C:\Users\SBA_AK\ntuser.dat
0xfffff8a0036e7010 0x0000000069188010 \??\C:\Users\SBA_AK\AppData\Local\Microsoft\Windows\UsrClass.dat
0xfffff8a0038fe280 0x0000000068390280 \??\C:\System Volume Information\Syscache.hve
0xfffff8a00000f010 0x000000002cfef010 [no name]
0xfffff8a000024010 0x000000002d07a010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000058010 0x000000002d3ae010 \REGISTRY\MACHINE\HARDWARE
0xfffff8a000846010 0x000000002a0e9010 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a000873010 0x0000000013880010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a000ab8010 0x0000000027455010 \SystemRoot\System32\Config\SECURITY
```  
  
  
Get the Virtual Address of the \REGISTRY\MACHINE\SYSTEM (in this case it is *0xfffff8a000024010*) and run the following command:  
```$ volatility -f foren.raw --profile=Win7SP1x64 printkey -o 0xfffff8a000024010 -K 'ControlSet001\Control\ComputerName\ComputerName'```  
  
```
Volatility Foundation Volatility Framework 2.6
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: ComputerName (S)
Last updated: 2020-08-25 16:20:54 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) mnmsrvc
REG_SZ        ComputerName    : (S) FORENWARMUP
```
  
  
We can conclude that the name of the computer is **FORENWARMUP**.  
  
  
  
* In order to find the user and password:  
  
```$ volatility -f foren.raw hashdump --profile=Win7SP1x64```
  
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
fwordCTF:1000:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:514fab8ac8174851bfc79d9a205a939f:::
SBA_AK:1004:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
```  
  
  
The user is **SBA_AK**.  
We crack the password hash to obtain the password: **password123**  
  
  
  
### Flag
`FwordCTF{FORENWARMUP_SBA_AK_password123}`
