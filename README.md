$MFT timestomping and tunneling detection
================

mft anomaly - forensic timestamp tampering and file tunneling detection

<b>prerequisites</b> 
     tzworks.net -> ntfswalk64 

<b>execution</b>
1) ntfswalk64 -mftfile $MFT > mftfile
2) run -> python mft.py mftfile stomp ""
     or
   python mft.py mftfile stomp "Users\user" <-- only this directory<br>
     or
   python mft.py mftfile tunnel "filename" <-- only check for this filename

<b>output</b>

ANOMALY---

     \[root]\<path corrupted>\p\pfBL.dll
     $STD_INFO:  01/03/2018   13:33:44.000 
     $FILE_NAME: 11/19/2019   17:09:09.403

SUMMARY...


     ('2023-03-20', 1)<br>
     ('2023-04-11', 1)<br>
     ('2024-02-20', 1)<br>
     ('2023-02-21', 5)<br>
     ('2022-12-19', 5)<br>
     ('2022-12-15', 6)<br>
     ('2023-08-30', 121)<br>
