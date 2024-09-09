import time
import streamlit as ST
from speedtest import Speedtest  

ST.title('SpeedTest')

def testSpeed():
    test = Speedtest()
    
    with ST.status("Connecting to server...", expanded=True) as status:
        time.sleep(3)
        status.update(label="Testing download speed...")
        down_speed = test.download()
        down_speed = round(down_speed / 10**6, 2)  
        ST.write("Download speed is", down_speed, "Mbps")
        time.sleep(1)  
        
        
        status.update(label="Testing upload speed...")
        up_speed = test.upload()
        up_speed = round(up_speed / 10**6, 2)  
        ST.write("Upload speed is", up_speed, "Mbps")
        time.sleep(1)

        
        status.update(label="Testing ping")
        ping = test.results.ping
        ST.write("Ping", ping, "ms")
        time.sleep(1)
        
    
        status.update(label="SpeedTest complete!", state="complete", expanded=False)
    
    ST.button("Rerun")


testSpeed()
