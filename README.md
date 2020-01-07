# mftAnomaly - forensic timestamp tampering
# first use TZWORKS to parse Master File Table: 
# ntfswalk64 -mftfile files/C/$MFT > mft

# Then run -> python mftAnomaly.py mft
# output example:
# ANOMALY---
#	     \[root]\<path corrupted>\p\pfBL.dll
#	     $STD_INFO:  01/03/2018   13:33:44.000 
#	     $FILE_NAME: 11/19/2017   17:09:09.403
