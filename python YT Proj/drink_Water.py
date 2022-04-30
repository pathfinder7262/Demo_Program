import time
from plyer import notification

if __name__=="__main__":
    while(True):
        notification.notify(
            title="Please Drink Water Now...",
            message="its good for your skin and privent pimple.",
            app_icon= "D:\ccpy\kvr program\python YT Proj\GW.ico",
            timeout=10
        )
        time.sleep(60*60)