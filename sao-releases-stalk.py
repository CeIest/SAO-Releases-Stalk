import os
import time
import requests
import webbrowser
from win10toast import ToastNotifier
  
ttttime = time.asctime()




coverorpreview = input("What to track?\n'1' for Cover,\n'2' for Preview (broken):\n")




# KADOKAWA PART
if coverorpreview == "1":
    coverID = input("Enter the Kadokawa ID of the release (example: '322102000017'):\n")
    coverIDpreset = coverID[0:6]

    def kdkwnotification_push():
        hr=ToastNotifier()
        hr.show_toast("Hey, the cover has been uploaded on Kadokawa")


    print("Kadokabrrrrrrrrrr")

    while True:
            kadokawa_1000 = requests.get('https://cdn.kdkw.jp/cover_1000/'+coverIDpreset+'/'+coverID+'.jpg')
            kadokawa_500 = requests.get('https://cdn.kdkw.jp/cover_500/'+coverIDpreset+'/'+coverID+'.jpg')
            # And others, to do later
            time.sleep(60)
            
    
            if kadokawa_1000.status_code == 404 and kadokawa_500.status_code == 404:
                print("Checked on", ttttime, ", nothing has changed")
                continue

    
            else:
                print("The cover has been uploaded on Kadokawa")
                kdkwnotification_push()
                webbrowser.open('https://cdn.kdkw.jp/cover_1000/'+coverIDpreset+'/'+coverID+'.jpg')
                webbrowser.open('https://cdn.kdkw.jp/cover_500/'+coverIDpreset+'/'+coverID+'.jpg')
                # Notification_mail()
                # break (but breaks webbrowser, try with a time.sleep idk)




# BOOKWALKER PART (to fix)
elif coverorpreview == "2":
    previewID = input("Enter Bookwalker's ID of the release (remove the 'de' at the beginning pls):\n")



    def bwnotification_push():
        hr=ToastNotifier()
        hr.show_toast("Hey, the preview has been uploaded on Bookwalker")


    print("brrrrrrrrrrwalker")

    while True:
            bookwalker_preview = requests.get('https://viewer-trial.bookwalker.jp/03/9/viewer.html?cid='+previewID+'&cty=0')

            time.sleep(60)
            
    
            if bookwalker_preview.status_code == 400:
                print("Checked on", ttttime, ", nothing has changed")
                continue

    
            else:
                print("The preview has been uploaded on Bookwalker")
                bwnotification_push()
                # Notification_mail()
                # os.system("bookwalkerripper.py ", previewID, "E:\rips")
                # uploads the rips on imgur



else: 
    print("wrong input")