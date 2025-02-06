
#язык (в разработке) ru - русский eng - English;  shitty translation from me and google
lang ="ru"
#directore
#mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
#mein_direct=[mein_direct.decode('UTF-8') for arg in args]
#logs;on-1,off-0
log_actived=0
#log save
log_save=0 
#установочные пакеты install path
path ={
    'calk_m' : "https://github.com/xHak2215/calk_m",
    'pynet'  : "https://github.com/xHak2215/py.net", 
    
}
# custom
try:

    from pyfiglet import Figlet
    preview_text = Figlet(font='slant')
except:
    preview_text=str(hex('slant'))#самнительно. . .
#consol title
consoledTitle="consolSH"
title = 1# 1 - title on 0 - title off
#среда исполнения SH-мая консоль cmd-консоль виндовс 
sreda="SH"
