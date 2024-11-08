
#язык (в разрабоьке) ru - русский eng - English;  shitty translation from me and google
lang ="ru"
#directore
#mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
#mein_direct=[mein_direct.decode('UTF-8') for arg in args]
#logs;on-1,off-0
log_actived=0
#log saveс
log_save=0
# custom
try:

    from pyfiglet import Figlet
    preview_text = Figlet(font='slant')
except:
    preview_text=str(hex('slant'))#самнительно. . .
#consol title
consoledTitle="consolSH"
title = 1# 1 - title on 0 - title off
#среда исполнения SH-мая кансоль cmd-кансоль виндовс 
sreda="SH"