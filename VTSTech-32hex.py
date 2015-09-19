import sys, os, hashlib, binascii, time

from passlib.apps import custom_app_context as pwd_context
from passlib.context import CryptContext

if sys.platform.startswith('win32'):
	import msvcrt
pwd_context = CryptContext(schemes=["hex_md5", "hex_md4", "hex_sha1", "nthash" ])
 
def banner():
	print "#########################################"
	print "# VTSTech-32hex v0.36 Python Version    #"
	print "# Facebook: facebook.com/VTSTech        #"
	print "# Twitter: @VTSTech_                    #"
	print "# Web: www.VTS-Tech.org                 #"
	print "# E-mail: veritas@vts-tech.org          #"
	print "# XMPP: veritas@creep.im                #"
	print "# BTC 1VTSgzD24bjkSGdD7kvauxkxHZ4yiwhdU #"
	print "#########################################"

StartTime = time.time()
ETime = 0
silent = 1
Cracked = ""
lines = 0
linet = 0
CrkCnt = 0
cnt = ""
TotalTime = ""
LastAlgo = ""
numpass = open('passwords.dat')
num_pass = sum(1 for line in numpass)
numpass.close()
if len(sys.argv) == 1:
	banner()
	print ""
	print "Usage: VTStech-32hex.py -l hashlist.txt - List mode using hashlist.txt"
	print ""
	print "Options"
	print ""
	print "-l hashlist.txt, load target hashes from hashlist.txt"
	print "-s speed per sec updates (60s interval)"
	print ""
	print "Press any key to display speed/sec"	
	print ""
	print "Supports the following encryption methods:"
	print ""	
	print "MD5 md5()"	
	print "MD4 md4()"	
	print "NTLM"
	print "RAdmin v2.x"
	print "MD5-SHA1 md5(sha1())"
	print "MD5-UP-MD5 md5(strtoupper(md5()))"	
	print "Double MD5 md5(md5())"	
	print "Triple MD5 md5(md5(md5()))"		
	print "Quadruple MD5 md5(md5(md5(md5())))"
	print "Quintuple MD5 md5(md5(md5(md5(md5()))))"
	print "Hextuple MD5 md5(md5(md5(md5(md5(md5())))))"
	print "Double MD4 md4(md4())"	
	print "Triple MD4 md4(md4(md4()))"		
	print "Quadruple MD4 md4(md4(md4(md4())))"
	print "Quintuple MD4 md4(md4(md4(md4(md4()))))"
	print "Hextuple MD4 md4(md4(md4(md4(md4(md4())))))"	
	sys.exit()
else:
	banner()
	print "Press any key to display speed/sec"
	if len(sys.argv[1]) == 2:
		if sys.argv[1] == "-l":
			target = sys.argv[2]
			hashes = open(sys.argv[2])				 
		elif sys.argv[2] == "-l":
			target = sys.argv[3]
			hashes = open(sys.argv[3])
		elif sys.argv[3] == "-l":
			target = sys.argv[4]
			hashes = open(sys.argv[4])
		if sys.argv[1] == "-s":
			silent = 0
		elif sys.argv[2] == "-s":
			silent = 0
md5 = CryptContext(schemes=["hex_md5"],)
md5sha_hash = CryptContext(schemes=["hex_sha1"],)
md4 = CryptContext(schemes=["hex_md4"],)
nt_hash = CryptContext(schemes=["nthash"],)
numhash = open(target)
line=0
num_hash = sum(1 for line in numhash)
print ""
print num_pass,"passwords,", num_hash,"hashes loaded."
print ""
TotalPass = (num_pass * num_hash) * 16
numhash.close()
hashes = open(target)
for lineh in hashes:
	passwd = open("passwords.dat")	
	CurrHash = lineh
	CurrTime = time.time()
	TotalTime = CurrTime - StartTime
	if sys.platform.startswith('win32'):
			while msvcrt.kbhit():
				msvcrt.getch()
				progress = str(cnt),chr(47),str(TotalPass)
				pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
				duration = str(round(TotalTime,2)),"s"
				print "Elapsed:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
	if ((CurrTime - ETime)  > 60) or ((CurrTime - ETime) == CurrTime):
		if (TotalTime > 1):
			if silent == 0:
				progress = str(cnt),chr(47),str(TotalPass)
				pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
				duration = str(round(TotalTime,2)),"s"
				print "Elapsed:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
		ETime = CurrTime
	for linep in passwd:
		lines += 1
		CurrPass = linep
		CurrHash = CurrHash.strip(chr(13))
		CurrHash = CurrHash.strip(chr(10))
		CurrHash = CurrHash.strip(chr(34))
		CurrPass = CurrPass.strip(chr(13))
		CurrPass = CurrPass.strip(chr(10))
		CurrPass = CurrPass.strip(chr(34))
		md51x = md5.encrypt(CurrPass)
		md52x = md5.encrypt(md51x)
		md53x = md5.encrypt(md52x)
		md54x = md5.encrypt(md53x)
		md55x = md5.encrypt(md54x)
		md56x = md5.encrypt(md55x)
		md5sha1 = md5.encrypt(md5sha_hash.encrypt(CurrPass))
		md41x = md4.encrypt(CurrPass)
		md42x = md4.encrypt(md41x)
		md43x = md4.encrypt(md42x)
		md44x = md4.encrypt(md43x)
		md45x = md4.encrypt(md44x)
		md46x = md4.encrypt(md45x)
		CurrPass2 = str(CurrPass + str((chr(0) * 100)))
		radmin = md5.encrypt(CurrPass2[0:100])
		md5umd5 = md5.encrypt(md51x.upper())
		cnt = (lines * 16)
		CurrTime = time.time()
		try:
			CurrPass.decode('ascii')
		except UnicodeDecodeError:
			ntlm = md4.encrypt(" ".encode('utf-16le'))	
		else:			
			ntlm = md4.encrypt(CurrPass.encode('utf-16le'))			
		TotalTime = CurrTime - StartTime
		if md51x == CurrHash:
			Algo = "MD5"
			Cracked = md51x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md52x == CurrHash:
			Algo = "Double MD5"
			Cracked = md52x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)				
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md53x == CurrHash:
			Algo = "Triple MD5"
			Cracked = md53x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md54x == CurrHash:
			Algo = "Quadruple MD5"
			Cracked = md54x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md55x == CurrHash:
			Algo = "Quintuple MD5"
			Cracked = md55x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md56x == CurrHash:
			Algo = "Hextuple MD5"
			Cracked = md56x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md5sha1 == CurrHash:
			Algo = "MD5(SHA1())"
			Cracked = md5sha1,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md41x == CurrHash:
			Algo = "MD4"
			Cracked = md41x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md42x == CurrHash:
			Algo = "Double MD4"
			Cracked = md42x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md43x == CurrHash:
			Algo = "Triple MD4"
			Cracked = md43x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md44x == CurrHash:
			Algo = "Quadruple MD4" 
			Cracked = md44x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md45x == CurrHash:
			Algo = "Quintuple MD4"
			Cracked = md45x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
		elif md46x == CurrHash:
			Algo = "Hextuple MD4"
			Cracked = md46x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break
		elif ntlm == CurrHash:
			Algo = "NTLM"
			Cracked = ntlm,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)
				LastAlgo == Algo
				CrkCnt = CrkCnt + 1				
			break
			break
		elif radmin == CurrHash:
			Algo = "radmin"
			Cracked = radmin,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break
		elif md5umd5 == CurrHash:
			Algo = "MD5-UP-MD5"
			Cracked = md5umd5,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method:",Algo
				print ''.join(Cracked)
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break			
print ""
print ""
DidWeWin = "Recovered: ",str(CrkCnt),"/",str(num_hash)," (",str(round(float(CrkCnt) / float(num_hash)*100,2)),"%)"
progress = str(cnt),chr(47),str(TotalPass)
pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
duration = str(round(TotalTime,2)),"s"
print ''.join(DidWeWin)
print ""
print "Elapsed time:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
print "Recovery complete."
sys.exit()