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
    import datetime
    import platform
    import keyboard
    from pyfiglet import Figlet
    from subprocess import Popen, PIPE, STDOUT     
    import subprocess as sp
    import ctypes
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

# Настройка\settings
# open:
#openp = ["txt", "bat", "exe", "jpg", "png", "wav", "mp3"]
# cmd
#cmd = 'CMD_consol_sh.bat'
#язык (в разрабоьке) ru - русский eng - English;  shitty translation from me and google
lang ="ru"
#directore
mein_direct=str(os.path.dirname(os.path.abspath(__name__)))
mein_direct.encode("utf-8")
#logs;on-1,off-0
log_actived=0
#log saveс
log_save=0
# custom
preview_text = Figlet(font='slant')
#consol title
consoledTitle="consolSH"
title = 1# 1 - title on 0 - title off
#сруда исполнения SH-мая кансоль cmd-кансоль виндовс 
sreda="SH"

cd_udirect=0#не удалять not delete
vare={}


def calc():
    deist =["0 синус - sin","1 тангет - tan","2 косинус - cos","3 число пи - pi","4 калькулятор (обычный)"]
    print("Выберите функцию:")
    for number, letter in enumerate(deist):
        print(number,".", letter)
    key=input(f"выбирите действие {kast}")
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
            print('conekt internet')
        elif ulrinethek.status_code == 404:
            print('Not conekt https://ya.ru/')
            ulrinethek = requests.get('https://www.google/')
        if ulrinethek.status_code == 200:
            print('conect internet')
        elif ulrinethek.status_code == 404:
            print('Not conekt https://www.google/')
    except  requests.exceptions.Timeout:
        print('Not conekt error time out')   
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
                disk_info += f"Device: {partition.device}\n nMountpoint: {partition.mountpoint}\n File System Type: {partition.fstype}\n Total Size: {partition_usage.total}\n bytesnUsed: {partition_usage.used}\n bytesnFree: {partition_usage.free}\n bytesnPercentage: {partition_usage.percent}%nn"
            except PermissionError:
                pass
        return disk_info
    # Генерируем отчет
    def generate_report():
        report = "=== System Report ===\n"
        report += get_system_info() + "\n"
        report += "=== CPU Report ===\n"
        report += get_cpu_info() + "\n"
        report += "=== Memory Report ===\n"
        report += get_memory_info() + "\n"
        report += "=== Disk Report ===\n"
        report += get_disk_info() + "\n"
        report += "Report generated on: " + str(datetime.datetime.now())
        return report
    report=generate_report()
    print(report)
    if key =="seve":
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
            [command,"sh" ],  # Используем 'sh' для запуска оболочки
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
        print(p)
            
def ping(ping_url)->int:
    start_time = time.time()
    try:
        k=requests.get(ping_url)
        s=k.status_code
        if s== 200:
            pass
        else:
            return "not"
    except requests.exceptions.InvalidURL:
        return f"Invalid url {kast}{ping_url}"
    response=time.time() - start_time
#    print('ping',response)
    return response
      
def admin() ->str:
   try:
    if os.getcwd() == "C:\Windows\system32":
        return True
    else:
        return False
   except AttributeError:  
     return ctypes.windll.shell32.IsUserAnAdmin() != 0
if title == 1:
    os.system("cls")
    print("\033[37m\033[44m{}\033[0m".format(preview_text.renderText(consoledTitle)))
    print("ДОБРО ПОЖАЛОВАТЬ В consolSH :)")
interhek()
app =""



while True:
    if log_actived == 1:
        logger.add(backtrace=True, diagnose=True)
        from loguru import logger
        logger.debug(f"logs on {log_actived}")
        logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
        if log_save == 1:
            logger.add("log_console.log", compression="zip") 
    #гарячие клавишы 
    keyboard.add_hotkey("ctrl+q", lambda: exit)
    
    
    if admin() == True:
        adm = "#"
    else:
        adm = "~"

    command = input("\033[32m{}\033[0m".format(f'{app}{os.getcwd()} {adm} "{sreda}" {kast}'))
    command=command.lower()
    if sreda == "SH":
        pass
    elif sreda =="cmd":
            sreda_cmd(input("\033[32m{}\033[0m".format(f'{app}{os.getcwd()} {adm} "{sreda}" {kast}')))
    
    
    if command == "break":
        break
    elif command == "dir":
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
                print(f"Создана директория{kast} {directory_name}")
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
        if lang == "ru":
            print(' "dir" - (показать содержимое текущей директории), \n cm  <имя_директории> - (создать директорию), \n var  - создание переменых \n vuod - запуск и передачя даных в программу \n  ')
            print("  del <имя_директории> - (удалить директорию). \n pwd - тикущий репозиторий \n bash - исполнение bash скриптов \n echo - вывод текста/цыфр перемных \n" )
        elif lang == "eng":
            print(' "dir" - (show the contents of the current directory),\n cm <directory name> - (create directory), \n vuod - запуск и передачя даных в програму')
            print(" del <directory name> - (delete directory). \n pwd - ticking repository \n bash - execution of bash scripts \n ")
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
        if lang =="ru":
            print("Выход из syshab")
            print (":( уже уходиш...")
            exit()     
        elif lang =="eng":
            print("exit is syshab")
            print (":( you're leaving already...")
            exit()   
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
        
    elif command.startswith("echo"):
        try:
            printe = command.split("'")[1]
        except IndexError:
            try:
                printe = command.split(" ")[1]
                printe=vare[printe]
            except KeyError:
                print('not var')
        print(printe)    
    elif command.startswith("var"):#var=переменая=данные
        var = command.split("=")[1]
        var_name = command.split("=")[2]
        vare[var] = var_name
        if log_actived == 1:
            logger.debug(f"var list {vare}")
    elif command.startswith("var delete"):
        var=command.split(" ")
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
        elif key =="off":
            if platform.system() =='Windows':
                os.system('shutdown -s')
            elif platform.system() =='Linux':
                os.system('poweroff')
    elif command =="cls":
        os.system('cls')        
    elif command.startswith("vuod"):
        directory=command.split(" ")[1]
        comand=command.split(" ")[2]
        os.chdir(mein_direct)
        p = subprocess.Popen(
            [directory,"sh" ],  # Используем 'sh' для запуска оболочки
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Позволяет работать со строками вместо байтов
            )
        if cd_udirect != 0:
            os.chdir(cd_udirect)
        
        stdout,stderr = p.communicate(comand)
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
        try:
            import pyautogui
        except:
            print("not lib pyautogui")
        x=command.split(":")[1]     #corsemove:x:y
        y=command.split(":")[2]
        pyautogui.moveRel(x,y, duration=0.25)
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
        url=command.split(" ")[1]

        
        
        
    else:
        if lang =="ru":
            print("error 1 команды нет")
        elif lang =="eng":
            print("error 1 not command") 
