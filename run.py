import os,sys,json
from time import sleep
try:
    import requests
except ImportError:
    print("! No Module Name requests")
    print("! Please wait...")
    os.system("pip install requests")

log = '''
    Get Information
   _____   _   _     _               _     
  / ____| (_) | |   | |             | |    
 | |  __   _  | |_  | |__    _   _  | |__  
 | | |_ | | | | __| | '_ \  | | | | | '_ \ 
 | |__| | | | | |_  | | | | | |_| | | |_) |
  \_____| |_|  \__| |_| |_|  \__,_| |_.__/ 
    User
                                           
'''
url = 'https://api.github.com/users/'

def ketik(a):
    for i in a+"\n":
        sys.stdout.write(i);sys.stdout.flush()
        sleep(000.1)
        
class main:
    def __init__(self):
        print(log)
        self.user = input('[•] Input Github User: ')
        ketik("[!] Please Wait...");sleep(1)
        try:
            req = requests.get(url+self.user)
            loads = json.loads(req.text)
            print('\n[•] User: {}'.format(loads["login"]))
            print("[•] Name: {}".format(loads["name"]))
            print("[•] ID: {}".format(loads["id"]))
            print("[•] Bio: {}".format(loads["bio"]))
            print("[•] Followers: {}".format(loads["followers"]))
            print("[•] Following: {}".format(loads["following"]))
            print("[•] Repository: {}".format(loads["public_repos"]))
        except KeyError:
            print("[!] User not found")
if __name__ == '__main__':
    main()
