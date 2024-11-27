print('Loading . . .')
kast = '>>'
try:
    import subprocess
    import os
    import time
    import datetime
    import sys
    import psutil 
    import requests
    import math
    import platform
    import keyboard
    from pyfiglet import Figlet
    from subprocess import Popen, PIPE, STDOUT     
    import subprocess as sp
#    import ctypes
    import pyautogui
#   subprocess.call(['python.exe' '-m' 'pip' 'install' '--upgrade pip'])
    modul_neim=['pip','requests','psutil']
except ImportError:
    print("error lib")
    print('извините каиета из библиотек не установлены')
    try:
        impors= input("устанавить? y/n"+kast)
        if impors == 'y':
            try:
                os.system('start impori.bat')
            except:
                print(f"увы не палучилась ")
        elif impors =="n":
            print('нет так нет в ручную')
    except IOError:
        raise SystemExit("error fail 1")
    
    
try:
    from settings import *
except ModuleNotFoundError:
    # Настройка\settings
    #язык (в разработке) ru - русский eng - English;  shitty translation from me and google
    lang ="ru"
    #logs;on-1,off-0
    log_actived=0
    #log save
    log_save=0
    # custom
    preview_text = Figlet(font='slant')
    #consol title
    consoledTitle="consolSH"
    title = 1# 1 - title on 0 - title off
    #среда исполнения SH-мая консоль cmd-консоль виндовс 
    sreda="SH"
    print("use um")

mein_direct=str(os.path.dirname(os.path.abspath(__name__)))

cd_udirect=0#не удалять not delete
vare={
    "$cd":f'{os.getcwd()}',
    "$pi":'3,1415926535',

    
}
#установочные пакеты
path ={
    'calk_m' : "https://github.com/xHak2215/calk_m",
    'pynet'  : "https://github.com/xHak2215/py.net", 
    
    
}


if log_actived == 1:
    from loguru import logger

    
if lang =="ru":
    HELP='''dir - (показать содержимое текущей директории), \n cm  <имя_директории> - (создать директорию), \n var  - создание переменных \n uod - запуск и передачя данных в программу \n color - изменение цвета \n apt - установщик пакетов на основе pip (apt -p для списка покетов также можно просто вписать сылку на github) \n 
 del <имя_директории> - (удалить директорию). \n pwd - текущий репозиторий \n bash - исполнение bash скриптов \n echo - вывод текста/цифр переменных \n eval - исполнение простых комманд python \n consol - исполнение комманд в консоли os  (windows-cmd ; Linux-terminal ) \n datatime - дата и время \n # - символ комментария
 taskill - завершение процессов  \n apt - pip-based package installer (apt -p for a list of packages you can also just enter a link to github) \n pip - pip-'комманда' \n system - взаимодействие с системой (system-scan - отчет о системе) (system-scan-save - отчет о системе и сохронение ) (system-off выключение пк) (system -start /путь/ - запуск программ)
 
 '''
elif lang=="eng":
    HELP='''dir - (show contents of current directory), \n cm <directory_name> - (create directory), \n var - create variables \n uod - launch and transfer data to the program \n color - change color \n apt - pip-based package installer (apt -p for a list of packages, you can also just enter a link to github) \n
del <directory_name> - (delete directory). \n pwd - ticking repository \n bash - execution of bash scripts \n echo - output of text/numbers of variables \n eval - execution of simple python commands \n consol - execution of commands in the os console (windows-cmd; Linux-terminal) \n datatime - data and time \n # - comment symbol
taskill - termination of processes \n apt - pip-based package installer (apt -p for a list of packages ) you can also just enter a link to github \n pip - pip-'command' \n system - interaction with the system (system-scan - system report) (system-off shutdown of the PC) (system -start /path/ - start programs)

'''
else:
    print("not lang")
     



def calc():
    deist =["0 синус - sin","1 тангет - tan","2 косинус - cos","3 число пи - pi","4 калькулятор (обычный)"]
    print("Выберите функцию:")
    for number, letter in enumerate(deist):
        print(number,".", letter)
    key=input(f"выберите действие {kast}")
    if key == "0":
        sinus()
    elif key == "1":
        cosinus()
    elif key == "2":
        tanget()
    elif key == "3":
        print(math.pi)
    elif key == "4":
        print(eval(input("ведите пример "+kast)))
    else:
        helpcalc =str(deist)
        helpcalc + "доступные операции"
        print("error" + helpcalc )


def sinus():
    sin = input(f"Введите значение угла в градусах для нахождения синуса (sin){kast} ")
    sin = float(sin)
    print(math.sin(math.radians(sin)))

def cosinus():   
    cos = input(f"Введите значение угла в градусах для нахождения косинуса (cos){kast} ")
    cos = float(cos)
    print(math.cos(math.radians(cos)))

def tanget():
    tan = input(f"Введите значение угла в градусах для нахождения тангенса (tan){kast} ")
    tan = float(tan)
    print(math.tan(math.radians(tan)))


def interhek():
    try:
        ulrinethek = requests.get('https://ya.ru/')
        if ulrinethek.status_code == 200:
            print('connect internet')
        elif ulrinethek.status_code != 200:
            print('Not connect https://ya.ru/')
            print("error inet 1")
            ulrinethek = requests.get('https://www.google/')
        if ulrinethek.status_code == 200:
            print('connect internet')
        elif ulrinethek.status_code != 200:
            print('Not connect https://www.google/')
            print("error inet 1")
    except  requests.exceptions.Timeout:
        print('Not connect error time out')   
def scansystem(key):
    # Получаем информацию о системе
    def get_system_info():
        uname = platform.uname()
        return f"System: {uname.system}\n Node Name: {uname.node}\n Release: {uname.release}\n Version: {uname.version}\n Machine: {uname.machine}\n Processor: {uname.processor}"
# Получаем информацию о процессоре
    def get_cpu_info():
        cpu_info = ""
        for cpu, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            cpu_info += f"CPU {cpu} Usage: {percentage}%n"
        return cpu_info
    # Получаем информацию о памяти
    def get_memory_info():
        svmem = psutil.virtual_memory()
        return f"Total Memory: {svmem.total}\n bytesnAvailable Memory: {svmem.available} \n bytesnUsed Memory: {svmem.used} \n bytesnMemory Usage: {svmem.percent}%"
# Получаем информацию о дисковом пространстве
    def get_disk_info():
        partitions = psutil.disk_partitions()
        disk_info = ""
        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                disk_info += f"Device: {partition.device}\n Mountpoint: {partition.mountpoint}\n File System Type: {partition.fstype}\n Total Size: {partition_usage.total}\n bytesnUsed: {partition_usage.used}\n bytesnFree: {partition_usage.free}\n bytesnPercentage: {partition_usage.percent}%"
            except PermissionError:
                pass
        return disk_info
    # Генерируем отчет
    def generate_report():
        
        system=preview_text.renderText(platform.system())
        
        report = "=== System Report ===\n"
        report += get_system_info() + "\n"
        report += "=== CPU Report ===\n"
        report += get_cpu_info() + "\n"
        report += "=== Memory Report ===\n"
        report += get_memory_info() + "\n"
        report += "=== Disk Report ===\n"
        report += get_disk_info() + "\n"
        report += "Report generated on: " + str(datetime.datetime.now())
        return report,system
    report=generate_report()
    print(report)
    if key =="save":
        # Сохраняем отчет в файл
        def save_report(report):
            os.chdir(mein_direct)
            with open("system_report.txt", "a") as file:
                file.write(report)
        save_report(report)
        if cd_udirect != 0:
            os.chdir(cd_udirect)
    
def sreda_cmd(command):
    while True:      
        p = subprocess.Popen(
            ['cmd',"sh" ],  # Используем 'sh' для запуска оболочки
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
        stdout,stderr = p.communicate(command)
        print(stdout) 
            
def ping(ping_url)->int:
    start_time = time.time()
    try:
        try:
            k=requests.get(ping_url)
            s=k.status_code
            if s== 200:
                pass
            else:
                return "not"
        except requests.exceptions.InvalidURL:
            return f"Invalid url {kast}{ping_url}"
    except requests.exceptions.ConnectionError: return "not conect"
    response=time.time() - start_time
#    print('ping',response)
    return response

def admin()->bool:
    if os.getcwd() == "C:/Windows/system32":
        return True
    else:
        return False
if title == 1:
    os.system("cls")
    print("\033[37m\033[44m{}\033[0m".format(preview_text.renderText(consoledTitle)))
    if lang =="ru":
        print("ДОБРО ПОЖАЛОВАТЬ В consolSH :)")
    if lang =="eng":
        print("WELCOM FROM consolSH :)")
    else:
        if log_actived==1:
            logger.debug(f"not lang {lang}")
            if log_save == 1:
                logger.add("log_console.log", compression="zip",rotation="500 MB") 
            
        
interhek()
app =""

 
while True:
    if log_actived == 1:
        
        logger.debug(f"logs on {log_actived}")
        logger.add(sys.stderr, format="{time} {level} {message} {error}", filter="comsol(mein file)", level="INFO")
        if log_save == 1:

            logger.add("log_console.log", compression="zip",rotation="500 MB") 
    #горячие клавиши
    keyboard.add_hotkey("ctrl+q", lambda: exit)
    
    
    if admin() == True:
        adm = "#"
    else:
        adm = "~"
    try:
        command = input("\033[32m{}\033[0m".format(f'{app}{os.getcwd()} {adm} "{sreda}" {kast}'))
        command=command.lower()
        if sreda == "SH":
            pass
        elif sreda =="cmd":
                sreda_cmd(input("\033[32m{}\033[0m".format(f'{app}{os.getcwd()} {adm} "{sreda}" {kast}')))
    except KeyboardInterrupt:
        pass
        if log_actived ==1:logger.debug(f"error {kast} KeyboardInterrupt")
    
    if command == "break":
        break
    elif command == "dir" or command == "ls":
        dir=os.listdir()
        i = 0
        while i < len(dir):
            file_byte = os.path.getsize(dir[i])
            print(f'{dir[i]} - {file_byte} bytes\n ')
            i += 1
    elif command.startswith("cm"):
        a = 0
        directory_name = command.split(" ")[1]
        while True:
            try:
                os.mkdir(directory_name)
                if lang =="ru":
                    print(f"Создана директория{kast} {directory_name}")
                elif lang =='eng':
                    print(f'Directory created {kast} {directory_name}')
                else:
                    if log_actived=="1":
                        logger.debug(f"not lang {lang}")
                break
            except FileExistsError:
                a=a+1
                directory_name=f'{directory_name}({a})' 
    elif command.startswith("del"):
        directory_name = command.split(" ")[1]
        try:
            os.rmdir(directory_name)
            print(f"Директория {directory_name} удалена")
        except FileNotFoundError:
            print(f"Директория {directory_name} не найдена")
    elif command == 'help':
        print(HELP)
    elif command.startswith("cd"):
        try:
            directory_name = command.split(" ")[1]
            os.chdir(directory_name)
            cd_udirect=directory_name
        except FileNotFoundError:
            print("error file 1")
    elif command == "pwd":
        print(os.getcwd())
    elif command == "date":
        print (datetime.datetime.now())
#        subprocess.call(["ping", "-c", "3", "google.com"])
    elif command == "exit": 
        try:
            if lang =="ru":
                print("Выход из syshab")
                print (":( уже уходиш ...")
                exit()     
            elif lang =="eng":
                print("exit is syshab")
                print (":( you're leaving already...")
                exit()   
        except PermissionError:
            file = open("log_console.log") #закрытие лог файла
            file.close()
    elif command.startswith("bash"):
        directory_name = command.split(" ")[1]
        if platform.system() =='Linux':
            os.chdir(mein_direct+"/cd")
            p = subprocess.Popen(
            [f"bash {directory_name}"],  # под линукс типо
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
            stdout,stderr = p.communicate(f"bash {directory_name} n")
            print(stdout)
            if cd_udirect != 0:
                os.chdir(cd_udirect)
        elif platform.system() =='Windows':
            os.chdir(mein_direct+"/cd")
            p = subprocess.Popen(
            ["busybox64.exe","sh" ],  # Используем 'sh' для запуска оболочки
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
            stdout,stderr = p.communicate(f"bash {directory_name} n")
            print(stdout) 
            if cd_udirect != 0:
                os.chdir(cd_udirect)
        
    elif command.startswith("echo") or command.startswith("print"):
        try:
            printe = command.split("'")[1]
        except IndexError:
            try:
                printe = command.split(" ")[1]
                printe =vare[printe]
            except KeyError:
                print('not var')
        print(printe)    
    elif command.startswith("var="):#var=переменная=данные
        try:
            var = command.split("=")[1]
            var_name = command.split(" ")[2]
            vare[var] = var_name
            if log_actived == 1:
                logger.debug(f"var list {vare}")
        except IndexError :
            print('error arg')
            if log_actived ==1:
                logger.debug(f"error arg нет аргументов")
    elif command.startswith("var delete"):
        var=command.split(" ")[1]
        del vare[var]
    elif command == "date":
        print (datetime.datetime.now())
    elif command.startswith("system"):
        key=command.split('-')[1]
        if key =="scan":
            try:
                key=command.split('-')[2]
                scansystem(key)
            except IndexError:
                scansystem(0)
        elif key =="off"or key=="poweroff":
            if platform.system() =='Windows':
                os.system('shutdown -s')
            elif platform.system() =='Linux':
                os.system('poweroff')
        elif key.startswith("start"):
            directory=key.split(' ')[1]
            os.system(f'start "consolSHProcess"{directory} ')
            

    elif command =="cls":
        if platform.system() =='Windows':
            os.system('cls')        
        else:
            os.system('clear')
    elif command.startswith("vuod"):
        directory=command.split(" ")[1]
        directory=directory.split(" ")[0]
        command=command.split(" ")[2]
        os.chdir(mein_direct)
        p = subprocess.Popen(
            [directory,"sh" ],  # Используем 'sh' для запуска оболочки
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
        stdout,stderr = p.communicate(f"{directory_name}")
        print(stdout)
        if cd_udirect != 0:
            os.chdir(cd_udirect)
        
        stdout,stderr = p.communicate(command)
        print(stdout) 
    elif command.startswith("color"):
        color=command.split(" ")[1]   
        if color =="green":
            print("\033[32m{}".format(""))
        elif color =="red":
            print("\033[31m{}".format(""))
        elif color =="blue":
            print("\033[34m{}".format(""))
        elif color =="white":
            print("\033[34m{}".format(""))
        elif color =="yellow":
            print("\033[37m{}".format(""))
        elif color =="not":
            print("\033[0m{}".format(""))
        else:
            try:
                 print("\033",color,"{}".format(""))
            except:
                print("error not color")
    elif command.startswith("corsemove"):
        x=command.split(":")[1] #corsemove:x:y
        x=x.split(":")[0]
        y=command.split(":")[2]
        print(x)
        print(y)
        pyautogui.PAUSE = True
        pyautogui.FAILSAFE = True
        for i in range(1):pyautogui.moveRel(x,y, duration=0.)
    elif command =="corsekordxy":
        try:
            import pyautogui
        except:
            print("not lib pyautogui")
        width, height = pyautogui.size()
        print(width,height)
    elif command.startswith("ping"):
        url=command.split(" ")[1]
        pings=ping(url)
        print(pings)
    elif command.startswith("taskill"):
        key=command.split(" ")[1]
        if platform.system() =='Linux':
            sp.Popen(f'TASKKILL /F /IM {key} /T')
        elif platform.system() =='Linux':
            sp.Popen(f'kill -SIGKILL {key}')
    elif command=="process":
        print(*[line.decode('cp866', 'ignore') for line in Popen('tasklist', stdout=PIPE).stdout.readlines()])
    elif command== "mein direct":
        print(mein_direct)
    elif command.startswith("apt"):
        try:
            Key=command.split(" ")[1]
            os.chdir(f"{mein_direct}\\cd\\path_file")
            if key.startswith("-p"):
                print(path.keys())
            elif key.startswith("-i"):
                ulr=key.split("-i")[1]
                if url in list(path.keys()):
                    url=path[url]
                    print(f"install path in {kast} {url} ")
            if True == os.path.isfile(f"{mein_direct}\\cd\\pip3.12.exe"):
                    if log_actived ==1:
                        logger.debug(f"error pip")
                    print("error pip файл pip3.12.exe не найден проверьте его наличие подробнее в info.txt")
            os.system(f"{mein_direct}\\cd\\pip3.12.exe install git+{url}")
        except IndexError :
            print('error arg')
            if log_actived ==1:
                logger.debug(f"error arg нет аргументов")
#    elif command.startswith(list(vare.keys())):#задаем переменую без комманды var
#        var=command.split("=")[0]
#        vars=command.split("=")[1]#даделать
#        vare[var]=vars
    elif command =="varslist":
        print(list(vare.keys()))
    elif command.startswith('path'):
        try:
            p=command.split(" ")[1]
            os.chdir(f"{mein_direct}\\cd\\path_file")
            os.system(f"{mein_direct}\\cd\\pip3.12.exe show {p}")
            if cd_udirect != 0:
                    os.chdir(cd_udirect)
        except IndexError :
            print('error arg')
            if log_actived ==1:
                logger.debug(f"error arg нет аргументов")
    elif command.startswith('pip'):
        try:
            p=command.split("-")[1]
            os.chdir(f"{mein_direct}\\cd\\path_file")
            error=os.system(f"{mein_direct}\\cd\\pip3.12.exe {p}")
            if error !=0:
                print('вазникла проблема с pip ')
                #os.path.exists(f"start {mein_direct}\\cd\\pip3.12.exe")
                if True == os.path.isfile(f"{mein_direct}\\cd\\pip3.12.exe"):
                    if log_actived ==1:
                        logger.debug(f"error pip")
                    print("error pip файл pip3.12.exe не найден проверьте его наличие подробнее в info.txt")
            if cd_udirect != 0:
                os.chdir(cd_udirect)
        except IndexError :
            print('error arg')
            if log_actived ==1:
                logger.debug(f"error arg нет аргументов")
    elif command.startswith("eval"):
        try:
            command=command.split(" ")[1]
            print(eval(command))
        except IndexError :
            print('error arg')
            if log_actived ==1:
                logger.debug(f"error arg нет аргументов")
        
    elif command.startswith("consol"):
        os.system(command.split(" ")[1])
    elif command == "datatime":
        import datetime
        print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    elif command.startswith("python"):
        a="python "
        if platform.system() =='Linux':
            a="python3 "
        os.system(a,command.split(" ")[1])
    elif command[0] =="#":
        pass
        
    
        
        
    else:
        if lang =="ru":
            print("error 1 команды нет")
        elif lang =="eng":
            print("error 1 not command")
        else:
            print("error 1 not command")
        if log_actived==1:
            logger.debug(f"not command {kast} {command}")
