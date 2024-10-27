import os
import platform
py='python.exe'
pip="pip3.12.exe install -r requirements.txt"
if platform.system() =='Linux':#LInuks setup
    py='python3.exe'
    pip="pip install -r requirements.txt"
mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
mein_direct.encode("utf-8")
os.system(f"{py} -m pip install --upgrade pip")
os.chdir(mein_direct+"\\cd")
os.system(pip)

