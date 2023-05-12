# encryption-mode-time-comparison
Time the encryption of the same large file using ECB, CBC, CFB, OFB,  CTR, and XTS-AES. Compare and rationalize the outcome.


line 12:  infile = open('"Samplefile.txt', 'rb') 


line 27 : mode = modes.CTR(iv)  <--- # edit for mode type #ECB, #CBC, #CFB, #OFB, #CTR, and #XTS-AES


