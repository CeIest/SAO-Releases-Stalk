__author__ = "Celest"

import time
import hashlib
import requests
import webbrowser
import subprocess
from urllib.request import urlopen, Request, urlretrieve
from win10toast import ToastNotifier
  


coverorpreview = input("What to track?\n'1' for Cover,\n'2' for Preview:\n")



# KADOKAWA PART
# Checking differences by reading the status code of the file
if coverorpreview == "1":
    coverID = input("Enter the Kadokawa ID of the release (example: '322102000017'):\n")
    coverIDpreset = coverID[0:6]


    def kdkwnotification_push():
        hr=ToastNotifier()
        hr.show_toast("The cover has been uploaded on Kadokawa.")


    print("Kadokabrrrrrrrrrr")

    while True:
            kadokawa_1000 = requests.get('https://cdn.kdkw.jp/cover_1000/'+coverIDpreset+'/'+coverID+'.jpg')
            kadokawa_500 = requests.get('https://cdn.kdkw.jp/cover_500/'+coverIDpreset+'/'+coverID+'.jpg')
            kadokawa_b = requests.get('https://cdn.kdkw.jp/cover_b/'+coverIDpreset+'/'+coverID+'.jpg')
            # And others, to do later (like https://d1hc4zdhstp3wq.cloudfront.net/img/goods/L/322102000017.jpg)
            
    
            if kadokawa_1000.status_code == 404 and kadokawa_500.status_code and kadokawa_b.status_code == 404:
                gettime = time.asctime()
                print("Checked on", gettime, ", nothing has changed.")
                time.sleep(60)
                continue

    
            else:
                print("The cover has been uploaded on Kadokawa.")
                kdkwnotification_push()
                urlretrieve('https://cdn.kdkw.jp/cover_1000/'+coverIDpreset+'/'+coverID+'.jpg', coverID+"_1000.jpg")
                urlretrieve('https://cdn.kdkw.jp/cover_500/'+coverIDpreset+'/'+coverID+'.jpg', coverID+"_500.jpg")
                urlretrieve('https://cdn.kdkw.jp/cover_b/'+coverIDpreset+'/'+coverID+'.jpg', coverID+"_b.jpg")
                # To-do: Notification_mail()
                break




# BOOKWALKER PART
# Checking differences by comparing hashes.
elif coverorpreview == "2":
    previewID = input("Enter Bookwalker's ID of the release (example: 'ded6f8074d-9a1d-4f57-bcdc-c011aaed6fc5':\n")
    previewIDtrimmed = previewID[2:]


    def bwnotification_push():
        hr=ToastNotifier()
        hr.show_toast("The preview has been uploaded on Bookwalker.")


    bookwalker = Request('https://viewer-trial.bookwalker.jp/03/9/viewer.html?cid='+previewIDtrimmed+'&cty=0',
              headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(bookwalker).read()
    currentHash = hashlib.sha224(response).hexdigest()


    print("brrrrrrrrrrwalker")

    while True:
            response = urlopen(bookwalker).read()
            currentHash = hashlib.sha224(response).hexdigest()

            time.sleep(60)
            
            response = urlopen(bookwalker).read()
            newHash = hashlib.sha224(response).hexdigest()


            if newHash == currentHash:
                gettime = time.asctime()
                print("Checked on", gettime, ", nothing has changed.")
    
            else:
                print("The preview has been uploaded on Bookwalker.")
                bwnotification_push()
                # To-do: Notification_mail()
                print("Ripping the preview...\n")
                #subprocess.run(["bw-dl.sh", previewIDtrimmed], shell=True)
                # To-do: the rips on imgur
                break


else: 
    print("Wrong input, please retry")