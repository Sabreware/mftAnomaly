mftAnomaly
================

mftAnomaly - forensic timestamp tampering and file tunneling detection

first use TZWORKS to parse Master File Table: 

1) ntfswalk64 -mftfile $MFT > mftfile

2) run -> python mft.py mftfile stomp ""

or

2) python mft.py mftfile stomp "Users\user" <-- only this directory<br>

or<br>

python mft.py mftfile tunnel "filename" <-- only check for this filename

output example:

ANOMALY---

     \[root]\<path corrupted>\p\pfBL.dll
     $STD_INFO:  01/03/2018   13:33:44.000 
     $FILE_NAME: 11/19/2019   17:09:09.403
