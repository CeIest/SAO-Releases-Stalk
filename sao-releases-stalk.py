import time
import hashlib
from urllib.request import urlopen, Request
from win10toast import ToastNotifier
  
ttttime = time.asctime()

kadokawa = Request('https://www.kadokawa.co.jp/product/322102000017/', #Change the 322102000017 
              headers={'User-Agent': 'Mozilla/5.0'})



def notification_push():
    hr=ToastNotifier()
    hr.show_toast("Hey, something changed on Kadokawa")

  
response = urlopen(kadokawa).read() # Performing a GET request
  

currentHash = hashlib.sha224(response).hexdigest() # Creating the initial hash
print("brrrrrrrrrr")
while True:
        response = urlopen(kadokawa).read() # Performing a GET request but in the loop
        currentHash = hashlib.sha224(response).hexdigest() # Creating the hash but in the loop

        time.sleep(30) # 30 seconds between each checks.
          
        response = urlopen(kadokawa).read()
        newHash = hashlib.sha224(response).hexdigest()
  
        if newHash == currentHash: # Comparing the hashes
            print("checked on", ttttime, ", nothing has changed")
            continue
  
        else:
            print("It seems that something changed on Kadokawa. Maybe they uploaded the cover?")
            notification_push()
            # Notification_mail()
  
            response = urlopen(kadokawa).read()
            currentHash = hashlib.sha224(response).hexdigest()
  
            time.sleep(30)