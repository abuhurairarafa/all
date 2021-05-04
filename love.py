import os,re,sys,itertools,time,requests,random,threading,json,random
import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

print("""   _    _   _  ___\n  /_\  | |_| || -- \ ® ┌──────────────────────────────┐\n / _ \ |  _  || -- /   │  Script By Abu Huraira Rafa  │\n/_/ \_\|_| |_||_|\_\   │  Github.com/abuhurairarafa   │\n   ID Facebook         └──────────────────────────────┘ """)
def login():
    os.system('clear')
    banner()
    toket = raw_input("\n[•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] Login Successful')
        bot_follow()
    except KeyError:
        print ("\n[!] Token Invalid")
        os.system('clear')
        login()

    def menu():
        os.system("clear")
        banner()
        try:
            toket = open('login.txt', 'r').read()
            otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except Exception as e:
            print("\n[•] Error : %s" % e)
            login()
        print("\n[1] Dump ID From Friend")
        print("[2] Dump ID From Public")
        print("[3] Dump ID From Followers")
        print("[4] Get Data Target")
        print("[0] Log Out")
        r = raw_input("\n[•] Choose : ")
        if r == "":
            print("\n[!] Fill In The Correct")
            menu()
        elif r == "1":
            friend()
        elif r == "2":
            public()
        elif r == "3":
            followers()
        elif r == "4":
            target()
        elif r == "0":
            try:
                os.system('rm -rf login.txt')
                exit()
            except Exception as e:
                print("\n[!] Error File Not Found %s" % e)
        else:
            print("\n[!] Wrong Input")
            menu()


def target():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\n[!] Token Invalid")
        os.system('rm -rf login.txt')
        login()
    try:
        idt = raw_input("\n[•] ID Target        : ")
        try:
            jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
            op = json.loads(jok.text)
            print("[•] Name Account     : " + op["name"])
            print("[•] Username         : " + op["username"])
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Email            : " + op["email"])
            except KeyError:
                print("[•] Email            : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Date Of Birth    : " + op["birthday"])
            except KeyError:
                print("[•] Date Of Birth    : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Gender           : " + op["gender"])
            except KeyError:
                print("[•] Gender           : -")
            try:
                r = requests.get("https://graph.facebook.com/" + idt + "/friends?access_token=" + toket)
                id = []
                z = json.loads(r.text)
                qq = (op['first_name'] + '.json').replace(" ", "_")
                ys = open(qq, 'w')
                for i in z['data']:
                    id.append(i['id'])
                    ys.write(i['id'])
                ys.close()
                print("[•] Total Friend     : %s" % (len(id)))
            except KeyError:
                print("[•] Total Friend     : -")
            try:
                a = requests.get("https://graph.facebook.com/" + idt + "/subscribers?limit=20000&access_token=" + toket)
                id = []
                b = json.loads(a.text)
                bb = (op['first_name'] + '.json').replace(" ", "_")
                jw = open(bb, 'w')
                for c in b['data']:
                    id.append(c['id'])
                    jw.write(c['id'])
                jw.close()
                print("[•] Total Follower   : %s" % (len(id)))
            except KeyError:
                print("[•] Total Follower   : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Relationship     : " + op["relationship_status"])
            except KeyError:
                print("[•] Relationship     : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Religion         : " + op["religion"])
            except KeyError:
                print("[•] Religion         : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] About            : " + op["about"])
            except KeyError:
                print("[•] About            : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Interested In    : " + op["interested_in"])
            except KeyError:
                print("[•] Interested In    : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Political        : " + op["political"])
            except KeyError:
                print("[•] Political        : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Quotes           : " + op["quotes"])
            except KeyError:
                print("[•] Quotes           : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Website          : " + op["website"])
            except KeyError:
                print("[•] Website          : -")
            except IOError:
                print("[•] Website          : -")
            try:
                jok = requests.get("https://graph.facebook.com/" + idt + "?access_token=" + toket)
                op = json.loads(jok.text)
                print("[•] Update Time      : " + op["updated_time"])
            except KeyError:
                print("[•] Update Time      : -")
            except IOError:
                print("[•] Update Time      : -")
            raw_input("\n[ Back ]")
            menu()
        except KeyError:
            raw_input("\n[ Back ]")
            menu()
    except Exception as e:
        exit("[•] Error : %s" % e)


if __name__ == '__main__':
    menu()
