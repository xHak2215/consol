import os
def s_kast():
    try:
        with open('kast.txt', 'r') as file: 
                kast = file.read()
                print(kast)
    except:
        print("erorr file 1")
        print("use um")
        kast = '>>'