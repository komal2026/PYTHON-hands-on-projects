import time 
from plyer import notification


while True:
    print("Please sip some water!")
    notification.notify(title="Ayyo drink some water you little sassy",
                        message = "You need to drink some water")
    time.sleep(60*60)
