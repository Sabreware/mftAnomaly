mftAnomaly
================

mftAnomaly - forensic timestamp tampering

first use TZWORKS to parse Master File Table: 

ntfswalk64 -mftfile $MFT > mft

Then run -> python mft.py mft

output example:

ANOMALY---

     \[root]\<path corrupted>\p\pfBL.dll
     $STD_INFO:  01/03/2018   13:33:44.000 
     $FILE_NAME: 11/19/2019   17:09:09.403
