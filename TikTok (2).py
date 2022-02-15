import random
import requests
import time as mm
import sys as n
from colorama import *
import string

req = requests.session()


def wacn(s):
    for c in s + "\n":
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(0.7 / 150)


def vpn():
    user = ""
    for i in range(15):
        user += random.choice(string.ascii_lowercase + string.digits)
    urlvpn = f"https://www.tiktok.com/@{user}?"
    headersvpn = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    sendvpn = req.get(urlvpn, headers=headersvpn)
    if sendvpn.status_code == 404:
        wacn(f"{Fore.LIGHTGREEN_EX}أنت لست ممنوعا")
    else:
        wacn(f"{Fore.LIGHTRED_EX}أنت ممنوع تمكين VPN")
    exit()


def checksessionid():
    sessionid = input(f"{Fore.LIGHTWHITE_EX}ضع معرف الجلسة: ")
    user = ""
    for i in range(8):
        user += random.choice(string.ascii_lowercase)
    urlchecksession = f"https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id={user}&app_language=ar"
    datachecksession = ""
    headerschecksession = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    cookieschecksession = {'sessionid': sessionid}
    sendchecksession = req.get(urlchecksession, data=datachecksession, headers=headerschecksession,
                               cookies=cookieschecksession)
    jsonsendchecksession = str(sendchecksession.json()["status_msg"])
    if jsonsendchecksession == "" or "":
        wacn(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}هذه الجلسة ليست محظورة")
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}تم حظر معرف الجلسة هذا")
    exit()


def checkersession(sessionid, user, count):
    urlcheckersession = f"https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id={user}&app_language=ar"
    datacheckersession = ""
    headerscheckersession = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    cookiescheckersession = {'sessionid': sessionid}
    sendchecksession = req.get(urlcheckersession, data=datacheckersession, headers=headerscheckersession,
                               cookies=cookiescheckersession)
    jsonsendcheckersession = str(sendchecksession.json()["status_msg"])
    if jsonsendcheckersession == "" or "":
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTGREEN_EX}تم الصيد")
        with open("found.txt", "a") as found:
            found.write(user + "\n")
    else:
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTRED_EX}لم يتم الصيد")


def checkerwithoutsession(user, count, tk, id):
    urlcheckerwithoutsession = f"https://www.tiktok.com/@{user}?"
    headerscheckerwithoutsession = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    sendcheckerwithoutsession = req.get(urlcheckerwithoutsession, headers=headerscheckerwithoutsession)
    if sendcheckerwithoutsession.status_code == 404:
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTGREEN_EX} تم الصيد")
        with open("found.txt", "a") as found:
            found.write(user + "\n")
            bott = f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={id}&text=❖ TikTok : {user}\n❖ Free By : @ZZSNN @j88sd @JJ9MJ"
            req.get(bott)
    else:
        print(
            f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTRED_EX} لم يتم الصيد")


wacn(f"""{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}
عبسكه
معرف المطور @JI9JJ 
المطور@JI9JJ 
                                                        
{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}[1] تحقق مما إذا كنت محظورًا
        [2] تحقق مما إذا تم حظر معرف الجلسة
        [3] المدقق مع معرف الجلسة
        [4] المدقق بدون معرف الجلسة
      
        {Style.BRIGHT}{Fore.LIGHTCYAN_EX}   
           TELEGRAM : @JI9JJ
               tele : @JI9JJ
{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================""")
choose = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}حدد رقم: ")
wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
if choose == "1":
    vpn()
elif choose == "2":
    checksessionid()
elif choose == "3":
    wacn(f"""{Style.BRIGHT}{Fore.LIGHTWHITE_EX}
        [1] اختيار من الملفات
        [2] اختيار تلقائي""")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    lastchoice = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}حدد رقم: ")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    if lastchoice == "1":
        sesssionid = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}أدخل معرف الجلسة: ")
        fileinput = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}اختيار من الملفات: ").strip()
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        users = open(fileinput, "r").read().splitlines()
        count = 0
        for user in users:
            if user == "":
                wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}شكرا لاستخدام أداتي")
                exit()
            else:
                count += 1
                checkersession(sesssionid, user, count)
    elif lastchoice == "2":
        sesssionid = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}enter session id: ")
        amount = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}how many users: "))
        length = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}length of users: "))
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        count = 0
        chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for _ in range(amount):
            user = ""
            for _ in range(length):
                user += random.choice(chars)
            count += 1
            checkersession(sesssionid, user, count)
        wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}thanks for using my tool.")
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        exit()
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}fool you will find nothing.")
elif choose == "4":
    tk = input("[+] توكنك: ")
    id = input("[+] ايديك: ")
    wacn(f"""{Style.BRIGHT}{Fore.LIGHTWHITE_EX}
            [1] اختيار من الملفات
            [2] اختيار تلقائي""")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    lastchoice = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}اختر رقم: ")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    if lastchoice == "1":
        fileinput = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}اختيار من الملفات: ").strip()
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        users = open(fileinput, "r").read().splitlines()
        count = 0
        for user in users:
            if user == "":
                wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}شكرا لاستخدام أداتي")
                exit()
            else:
                count += 1
                checkerwithoutsession(user, count, tk, id)
    elif lastchoice == "2":
        amount = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}كم عدد المستخدمين: "))
        length = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}طول المستخدمين: "))
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        count = 0
        chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for _ in range(amount):
            user = ""
            for _ in range(length):
                user += random.choice(chars)
            count += 1
            checkerwithoutsession(user, count, tk, id)
        wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}شكرا لاستخدام أداتي")
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        exit()
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}أيها الأحمق لن تجد شيئًا")
else:
    wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}أيها الأحمق لن تجد شيئًا")
