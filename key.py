import os
from time import sleep

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

os.system('clear')
print(GG+'\t  Tools By Billal')
print(G+'\t    Bl4ckDr460n')
print('\t https://WhiteCyberArmy.blogspot.com')
print(W+'[]===========================================[]')
print(RR+'\nPlease Wait...')
sleep(1)
print(G+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(G+'[!]Success !')
print(RR+'\nPlease Wait...')
sleep(1)
print(G+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(G+'[!] Success !')
sleep(1)
print(G+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(G+'[!] Successfully !! ^^'+Y+'\n\nhubungi https://WhiteCyberArmy.blogspot.com untuk requests\natau pertanyaan \nThanks :*\n\n')
print """

	"""
os.system('clear')
print(Y+'Thanks To :')
print """
			"""
print(G+' Bl4ck Dr460n')
sleep(1)
print(GL+'Semut')
sleep(1)
print(BB+'Kanjok Pengesty')
print """

		"""
# Thank To :
# Bl4ck Dr460n
# Semut
# kanjok pengesty
