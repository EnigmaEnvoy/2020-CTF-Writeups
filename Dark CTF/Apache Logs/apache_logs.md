# Apache Logs (Web)
  
> Our servers were compromised!! Can you figure out which technique they used by looking at Apache access logs.  
> flag format: DarkCTF{}  
  
  
In the [log file](https://github.com/EnigmaEnvoy/2020-CTF-Writeups/blob/master/Dark%20CTF/Apache%20Logs/logs.ctf) provided, we can see some SQL Injection payloads.  
Decoding some of them:  
  
**String:** `GET /mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C+108%2C+97%2C+103%2C+32%2C+105%2C+115%2C+32%2C+83%2C+81%2C+76%2C+95%2C+73%2C+110%2C+106%2C+101%2C+99%2C+116%2C+105%2C+111%2C+110%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details HTTP/1.1`  
**URL Decoded string:** `GET/mutillidae/index.php?page=user-info.php&username='+union+all+select+1,String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+83,+81,+76,+95,+73,+110,+106,+101,+99,+116,+105,+111,+110),3+--+&password=&user-info-php-submit-button=View+Account+DetailsHTTP/1.1`  
**Converting the character codes to text:** `flag is SQL_Injection` (This is a fake flag).  
  
  
**String:** `GET /mutillidae/index.php?csrf-token=&username=CHAR%28121%2C+111%2C+117%2C+32%2C+97%2C+114%2C+101%2C+32%2C+111%2C+110%2C+32%2C+116%2C+104%2C+101%2C+32%2C+114%2C+105%2C+103%2C+104%2C+116%2C+32%2C+116%2C+114%2C+97%2C+99%2C+107%29&password=&confirm_password=&my_signature=&register-php-submit-button=Create+Account HTTP/1.1`  
**URL Decoded string:** `GET/mutillidae/index.php?csrf-token=&username=CHAR(121,+111,+117,+32,+97,+114,+101,+32,+111,+110,+32,+116,+104,+101,+32,+114,+105,+103,+104,+116,+32,+116,+114,+97,+99,+107)&password=&confirm_password=&my_signature=&register-php-submit-button=Create+AccountHTTP/1.1`  
**Converting the character codes to text:** `you are on the right track`  
  
  
**String:** `GET /mutillidae/index.php?page=client-side-control-challenge.php HTTP/1.1" 200 9197 "http://192.168.32.134/mutillidae/index.php?page=user-info.php&username=%27+union+all+select+1%2CString.fromCharCode%28102%2C%2B108%2C%2B97%2C%2B103%2C%2B32%2C%2B105%2C%2B115%2C%2B32%2C%2B68%2C%2B97%2C%2B114%2C%2B107%2C%2B67%2C%2B84%2C%2B70%2C%2B123%2C%2B53%2C%2B113%2C%2B108%2C%2B95%2C%2B49%2C%2B110%2C%2B106%2C%2B51%2C%2B99%2C%2B116%2C%2B49%2C%2B48%2C%2B110%2C%2B125%29%2C3+--%2B&password=&user-info-php-submit-button=View+Account+Details`  
**URL Decoded string:** `GET/mutillidae/index.php?page=client-side-control-challenge.phpHTTP/1.1"2009197"http://192.168.32.134/mutillidae/index.php?page=user-info.php&username='+union+all+select+1,String.fromCharCode(102,+108,+97,+103,+32,+105,+115,+32,+68,+97,+114,+107,+67,+84,+70,+123,+53,+113,+108,+95,+49,+110,+106,+51,+99,+116,+49,+48,+110,+125),3+--+&password=&user-info-php-submit-button=View+Account+Details`  
**Converting the character codes to text:** `flag is DarkCTF{5ql_1nj3ct10n}`  
  
  
### Flag
`DarkCTF{5ql_1nj3ct10n}`
