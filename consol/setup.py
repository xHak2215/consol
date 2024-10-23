import os
mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
mein_direct.encode("utf-8")
os.chdir(mein_direct)
os.system("pip install -r requirements.txt")





