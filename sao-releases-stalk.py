import os
import time
import hashlib
from urllib.request import urlopen, Request
from win10toast import ToastNotifier
  
ttttime = time.asctime()




coverorpreview = input("What to track?\n'1' for Cover,\n'2' for Preview:\n")

# KADOKAWA PART
if coverorpreview == "1":
    coveritis = coverorpreview
    coverID = input("Enter the Kadokawa ID of the release (example: '322102000017'):\n")
    kadokawa = Request('https://www.kadokawa.co.jp/product/'+coverID+'/',
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



# BOOKWALKER PART
elif coverorpreview == "2":
    previewitis = coverorpreview
    previewID = input("Enter Bookwalker's ID of the release (remove the 'de' at the beginning pls):\n")
    bookwalker = Request('https://bookwalker.jp/de'+previewID+'/',
              headers={'User-Agent': 'Mozilla/5.0'})
    def notification_push():
        hr=ToastNotifier()
        hr.show_toast("Hey, something changed on Bookwalker")


    response = urlopen(bookwalker).read() # Performing a GET request
    

    currentHash = hashlib.sha224(response).hexdigest() # Creating the initial hash
    print("brrrrrrrrrr")
    while True:
            response = urlopen(bookwalker).read() # Performing a GET request but in the loop
            currentHash = hashlib.sha224(response).hexdigest() # Creating the hash but in the loop

            time.sleep(30) # 30 seconds between each checks.
            
            response = urlopen(bookwalker).read()
            newHash = hashlib.sha224(response).hexdigest()
    
            if newHash == currentHash: # Comparing the hashes
                print("checked on", ttttime, ", nothing has changed")
                continue
    
            else:
                print("It seems that something changed on bookwalker. Maybe they uploaded the cover?")
                notification_push()
                # Notification_mail()
                # os.system("bookwalkerripper.py ", previewID, "E:\rips") # to fix this shit plz
                response = urlopen(bookwalker).read()
                currentHash = hashlib.sha224(response).hexdigest()
    
                time.sleep(30)



else: 
    print("wrong input")