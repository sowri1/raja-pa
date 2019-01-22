import os 
def enable():
    os.system("netsh interface set interface 'Wi-Fi' enabled")

def disable():
    os.system("netsh interface set interface 'Wi-Fi' disabled")
os.system("netsh interface show interface")
disable()