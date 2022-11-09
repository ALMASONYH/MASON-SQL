import requests
from colorama import Fore
import sys as mp
import time as mpp
def slow(mpr):
	for mppp in mpr + "\n":
		mp.stdout.write(mppp)
		mp.stdout.flush()
		mpp.sleep(0.5 / 120)
slow("""
==================================================
          _____              __  __                                      
         |  ___| __ ___  ___|  \/  | __ _ ___  ___  _ __  _ __ _   _     
  _____  | |_ | '__/ _ \/ _ \ |\/| |/ _` / __|/ _ \| '_ \| '__| | | |    
 |_____| |  _|| | |  __/  __/ |  | | (_| \__ \ (_) | | | | |  | |_| |  _ 
         |_|  |_|  \___|\___|_|  |_|\__,_|___/\___/|_| |_|_|   \__, | (_)
                                                               |___/     

 - By https://www.youtube.com/channel/UCEG8JF8i-mqQGEK0uf3V_rw
==================================================

""")

slow("\n [1]-http:// === [2]-https://")
slow("\n=====================================")
MASONxx= input("[MASON 1or2] >> ")
slow("\n=====================================")
MASON= "[MASON url] >> "
MASONurl= input(MASON)
slow("\n=====================================")
MASONlist="MASON-file.txt"
MASONlist2= open(MASONlist, 'r')
def mproscan():
	while True:
		MASON1 = MASONlist2.readline().split('\n')[0]
		if MASONxx == '1':
			MASONurl2= "http://"+MASONurl+"/"+MASON1
			MASONreq1= requests.get(url=MASONurl2).status_code
			if MASONreq1 == 200:
				print(f'[{Fore.GREEN}MASON Found >>{Fore.WHITE}] ', MASONurl2)
				slow("\n=====================================")
				with open('MASON-Url-Found.txt', 'a') as mp:
					mp.write(MASON+MASONurl2+'\n')
			else:
				print(f'[{Fore.RED}MASON Not Found >>{Fore.WHITE}] ', MASONurl2)
				slow("\n=====================================")
		elif MASONxx == '2':
			MASONurl3= "https://"+MASONurl+"/"+MASON1
			MASONreq2= requests.get(url=MASONurl3).status_code
			if MASONreq2 == 200:
				print(f'[{Fore.GREEN}MASON Found >>{Fore.WHITE}] ', MASONurl3)
				slow("\n=====================================")
				with open('MASON-Url-Found.txt', 'a') as mp:
					mp.write(MASON+MASONurl3+'\n')
			else:
				print(f'[{Fore.RED}MASON Not Found >>{Fore.WHITE}] ', MASONurl3)
				slow("\n=====================================")
mproscan()
