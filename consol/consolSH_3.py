modul_neim=['pip', 'beautifulsoup4' ,'tkinter-page' ,'requests', 'wikipedia psutil','requests''tabulate','you-get','wmi','asyncio','PyQt5','getch','subprocess.run','QtGui','QtGui','sockets','folium','pyfiglet']
kast = '>>'
try:
    import subprocess
    subprocess.call(['python.exe' '-m' 'pip' 'install' '--upgrade pip'])
    import os
    import hashlib
    import time
    import types
    import datetime
    from tkinter import messagebox as mb
    import webbrowser
    import sys
    import decimal
    import timeit
    import psutil
    import requests
    from tabulate import tabulate
    import math
    import string
    import asyncio
    import secrets
    import logging
    import datetime
    import platform
    import sqlite3
    import wikipedia
    import tkinter as tk
    from bs4 import BeautifulSoup
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from http.cookiejar import CookieJar
    from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
    from PyQt5.QtCore import QTimer, QTime, Qt
    import keyboard
    import msvcrt
    import socket 
    from pyfiglet import Figlet
    import folium

    modul_neim=['pip', 'beautifulsoup4' ,'tkinter-page' ,'requests', 'wikipedia','psutil','requests']
except ImportError:
    print("error lib")
    print('извините каиета из библиотек не установлены')
    try:
        impors= input("устанавить? y/n"+kast)
        if impors == 'y':
            try:
                os.system('start impori.bat')
            except:
                print(f"увы не палучилась \f тебе придетсья самаму устанавить subprocess для этого открой терминал (cmd) т веди : pip install subprocess.run ")
                subprocess.call(['pip', 'install', modul_neim , '-y'])
        elif impors =="n":
            print('нет так нет в ручную')
            input()
    except IOError:
        raise SystemExit("error fail 1")
        input()

#pip install beautifulsoup4
#pip install tkinter-page
#pip install requests
#pip install wikipedia
#pip  install pip
#pip install psutil
#pip install requests
#pip install tabulate
#pip install you-get
#pip install wmi
#pip install asyncio
#pip install PyQt5
#pip install getch
#pip install subprocess.run
#pip install folium
#pip install pyfiglet

tireparitir = os.getcwd()

# Настройка
# open:
openp = ["txt", "bat", "exe", "jpg", "png", "wav", "mp3"]
# cmd
cmd = 'CMD_consol_sh.bat'
#язык (в разрабоьке)
lang ="ru"
# custom
preview_text = Figlet(font='standard')
#try:
#    os.chdir("C:/Users/Home/Desktop/beta 3.0/consol/Cd/root")

#---------import kast-----------
#    from kast import s_kast
#    s_kast()
#except:
#    print("error fail 1")
#    print("use um")
#-------------------------------

inethek=""
ulrinethek = requests.get('https://ya.ru/')
def interhek():
    if ulrinethek.status_code == 200:
        print('conekt internet')
        inethek = "true"
    elif ulrinethek.status_code == 404:
        print('Not conekt internet!')
        inethek = "folse"
interhek()



try:
    os.chdir(f'{tireparitir}\\Cd\\root\\kast')
    with open('kast.txt', 'r') as file: 
        kast = file.read()
    #kast = '>>'
    colors = ["green", "red", "blue"]
except:
    kast = '>>'
    print("error fail 1")
    print("use um")
def cor_direct():
    try:
        with open('start direct.txt', 'r') as file: 
                direct = file.read()
        os.chdir(direct)
    except:
        print("error fail 1")
        print("use um")
#cor_direct()

def scan_file(file_path):
    try:
        if os.path.isfile(file_path):
            # Хэшируем содержимое файла для сканирования через VirusTotal
            with open(file_path, 'rb') as f:
                file_content = f.read()
                file_hash = hashlib.sha256(file_content).hexdigest()
            
            # Запрос к API VirusTotal для получения отчета о файле
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', 
                                    params={'apikey': '79a74932f60d2c552e88149c961618b10547d700f9c21b757f58f42b2779d35b', 'resource': file_hash})
            # Проверяем статус ответа
            if response.status_code == 200:
                result = response.json()
                # Проверяем наличие положительных сигналов на вирусы в отчете
                if result['response_code'] == 1 and result['positives'] > 0:
                    print(f"Malicious file detected: {file_path}")
                    
                    return True
                else:
                    print(f"File is clean: {file_path}")
                    return False
            else:
                print(f"Error scanning file: {file_path}, HTTP status code: {response.status_code}")
        else:
            print(f"Format file not supported: {file_path}")
        
    except PermissionError:
        print(f"Access denied to file: {file_path}")
    except Exception as e:
        print(f"Error scanning file: {file_path}, Error: {e}")
    return False

def scan_url(url):
    try:
        # Запрос к API VirusTotal для получения отчета о URL
        response = requests.get('https://www.virustotal.com/vtapi/v2/url/report',
                                params={'apikey': '79a74932f60d2c552e88149c961618b10547d700f9c21b757f58f42b2779d35b', 'resource': url})
        # Проверяем статус ответа
        if response.status_code == 200:
            result = response.json()
            # Проверяем наличие положительных сигналов на вирусы в отчете
            if result['response_code'] == 1 and result['positives'] > 0:
                print(f"Malicious URL detected: {url}")
                print("Scan results from NS:")
                for scan, result in result['scans'].items():
                    print(f"{scan}: {result['result']}")
                return True
            else:
                print(f"URL is safe: {url}")
                return False
        else:
            print(f"Error scanning URL: {url}, HTTP status code: {response.status_code}")
    except Exception as e:
        print(f"Error scanning URL: {url}, Error: {e}")
    return False

def anti_virus(target):
    if target.startswith('http://') or target.startswith('https://'):
        scan_url(target)
    else:
        scan_file(target)

def directoryс():
    try:
        print(os.getcwd())
        C =  os.listdir("Cd/")
        os.chdir("Cd/root")
        root =  os.listdir(os.getcwd())
        os.chdir("..")
        os.chdir("file")
        os.listdir(os.getcwd())
        file = os.listdir(os.getcwd())
        print(root + file)
    except IOError:
        raise SystemExit("error fail 1")
        input()


def admin():
   try:
     return os.getpid() == 0
   except AttributeError:
     return ctypes.windll.shell32.IsUserAnAdmin() != 0

def opentxt():
    txt = input("Введите путь к файлу или URL: " + kast)
    os.path.isdir(txt) 
    sv = input("Введите способ взаимодействия (чтобы получить подсказку введите 'help'): " + kast)
    print(sv)
    if sv == "help":
        print("w - (запись), a - (добавление данных к уже существующему файлу), r - (чтение)")
    else:
        print("error")
    so = ["r", "a", "w"]
    for sv in so:
        txtfile = open(txt, sv, encoding="UTF-8")
        print(txtfile.read())
        txtfile.close()

def openphoto():
    try:
        music = input("Введите путь: " + kast)
        jpg = input("Введите путь: " + kast)
        os.path.isdir(jpg) 
        webbrowser.open(jpg)
    except IOError:
        raise SystemExit("error fail 1")
        input()

def infoplatform():
    print(sys.platform)
    WinTip = sys.platform
    print(sys.getwindowsversion())
    WinVersipn = sys.getwindowsversion()

def list_hec(liste, txtceh):
    for s in liste: 
        if txtceh.lower().find(s.lower()) != -1: 
            hec = True

def sudo():
    servise = ["PyPI", "GitHub", "youtube"]
    # Установка пакета с PyPI
    dovald = input("servis dovald" + kast)
    if dovald == "PyPI":
        ULR = input("ULR" + kast)
        subprocess.call(['pip', 'install', ULR])
    elif dovald == "GitHub":
        ULR = input("ULR" + kast)
        # Установка пакета с GitHub
        subprocess.call(['pip', 'install', f'git+{ULR}'])
    elif dovald == "youtube":
        ULR = input("ULR" + kast)
        subprocess.call(['you-get', ULR])
    elif dovald == "ULR (beta)":
        ULR = input("ULR" + kast)
        # Установка пакета с других источников
        subprocess.call(['pip', 'install', ULR])
    elif dovald == "help":
        print("Доступные сервисы: " + str(servise))
    else:
        print("error"+"доступные сервисы" + str(servise))

def calc():
    deist =["синус - sin","тангет - tan","косинус - cos","число пи - pi","калькулятор (обычный)"]
    print("Выберите функцию:")
    for number, letter in enumerate(deist):
        print(number,".", letter)
    choice = input("Введите номер функции: ")
    if choice == "0":
        sinus()
    elif choice == "1":
        cosinus()
    elif choice == "2":
        tanget()
    elif choice == "3":
        print(math.pi)
    elif choice == "4":
        print(eval(input("ведите пример "+kast)))
    else:
        helpcalc =str(deist)
        helpcalc + "доступные операции " 
        print("error" + helpcalc )


def sinus():
    sin = input("Введите значение угла в градусах для нахождения синуса (sin): ")
    sin = float(sin)
    print(math.sin(math.radians(sin)))

def cosinus():   
    cos = input("Введите значение угла в градусах для нахождения косинуса (cos): ")
    cos = float(cos)
    print(math.cos(math.radians(cos)))

def tanget():
    tan = input("Введите значение угла в градусах для нахождения тангенса (tan): ")
    tan = float(tan)
    print(math.tan(math.radians(tan)))

def cmdcom():
    cmdcom = input("Введите команду для выполнения в командной строке: ")
    if cmdcom == "cmd":
        print("Введите любую команду из cmd после cmdcom")
    elif cmdcom == "":
        print("Введите любую команду из cmd после cmdcom")
    else:
        subprocess.run(['cmd', '/c', cmdcom])

def you_get_help():
    print("Для использования you-get введите: 'you-get [ссылка на видео]'")

def dec():
    print("esc - выход")
    try:
        while True: 
 #           inp_key =keyboard.record('esc')
            cpu_gr = str(psutil.cpu_percent())
            cpu = "Percentage usage:" + cpu_gr + "%"
            cpu_r = psutil.cpu_percent()
            if psutil.cpu_percent() >= 30:
                cpu_r = "\033[31m {}" .format(cpu)
            elif psutil.cpu_percent() >= 50:
                cpu_r = "\033[33m {}" .format(cpu)
            elif psutil.cpu_percent() >= 100:
                cpu_r = "\033[32m {}" .format(cpu)
#           elif inp_key == "[KeyboardEvent(esc down)]":
#                print("не готово мне лань")
            print(cpu_r)   
            
            # CPU frequency
            cpu_info = psutil.cpu_freq()
            print(f"Current frequency: {cpu_info.current:.2f} Mhz")
            print(f"Minimum frequency: {cpu_info.min:.2f} Mhz")
            print(f"Maximum frequency: {cpu_info.max:.2f} Mhz")
            time.sleep(1)
            os.system('cls')
    except KeyboardInterrupt:
        print("Команда прервана пользователем")
def gen_password():
    async def generate_password(length):
        """Генерация случайного пароля заданной длины"""
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    async def generate_passwords_async(password_length):
        """Генерация паролей асинхронно"""
        while True:
            password = await generate_password(password_length)
            yield password
            await asyncio.sleep(0.01)

    def save_password_to_file(password, file_path):
        """Сохранение пароля в текстовый файл"""
        with open(file_path, "a") as file:
                file.write(password + "\n")
    async def main():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        password_length = int(await asyncio.to_thread(input(f"Введите длину пароля{kast}")))
        logging.info(f"Выбрана длина пароля: {password_length}")
        # Получение пути к текущей директории
        current_directory = os.path.dirname(os.path.realpath(__file__))
        # Формирование полного пути для сохранения файла с паролями
        file_path = os.path.join(current_directory, "passwd_list.txt")
        logging.info(f"Путь для сохранения паролей: {file_path}")
        async for password in generate_passwords_async(password_length):
            save_password_to_file(password, file_path)
            logging.info(f"Сгенерирован и сохранен новый пароль: {password}")
            await asyncio.sleep(0.000008)  # Задержка в 1 секунду перед логированием

    if __name__ == "__main__":
        asyncio.run(main())
def hifr():
    def encrypt(text, shift):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
            return result

    def decrypt(text, shift):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                result += char
        return result
    print("руский не подержывается")
    text = input(":")
    shift = 3
    encrypted_text = encrypt(text, shift)
    print("Зашифрованный текст:", encrypted_text)
    encrypted = input("расшыфровка:")
    decrypted_text = decrypt(encrypted_text, shift)

    print("Расшифрованный текст:", decrypted_text)
def text_to_bits():
    text = input("text " + kast)
    binary_string = ' '.join(format(ord(char), '08b') for char in text)
    print(binary_string)

def text_from_bits():
    binary_string = input("bin" + kast , 2)
    binary_string = int(binary_string)
    text = ''.join(chr(int(char, 2)) for char in binary_string.split(' '))
    print(text)
    
def scansystem():
    # Получаем информацию о системе
    def get_system_info():
        uname = platform.uname()
        return f"System: {uname.system}\n nNode Name: {uname.node}\n nRelease: {uname.release}\n nVersion: {uname.version}\n nMachine: {uname.machine}\n nProcessor: {uname.processor}"
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
                disk_info += f"Device: {partition.device}\n nMountpoint: {partition.mountpoint}\n nFile System Type: {partition.fstype}\n nTotal Size: {partition_usage.total}\n bytesnUsed: {partition_usage.used}\n bytesnFree: {partition_usage.free}\n bytesnPercentage: {partition_usage.percent}%nn"
            except PermissionError:
                pass
        return disk_info

    # Генерируем отчет
    def generate_report():
        report = "=== System Report ===nn"
        report += get_system_info() + "nn"
        report += "=== CPU Report ===nn"
        report += get_cpu_info() + "nn"
        report += "=== Memory Report ===nn"
        report += get_memory_info() + "nn"
        report += "=== Disk Report ===nn"
        report += get_disk_info() + "nn"
        report += "Report generated on: " + str(datetime.datetime.now())
        return report

    # Сохраняем отчет в файл
    def save_report(report):
        with open("system_report.txt", "w") as file:
            file.write(report)

    # Генерируем отчет и сохраняем его в файл
    report = generate_report()
    save_report(report)
    print("System report generated and saved to system_report.txt" + " to  " +  os.getcwd())
def str_cek():
    utxt =input("str 1"+ kast)
    rtxt =input("str 2"+ kast)
    if  rtxt == utxt:
        print ("одинаковы")
    else:
         print("не одинаковы")
def SQL():
    # Создаем соединение с базой данных
    neim_sql = input("назваеие базы даных" + kast)
    conn = sqlite3.connect(neim_sql)
    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()
    # Создаем таблицу
    print('пример : CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    SQL_programm = input("прогрвмма" + kast)
    cursor.execute(SQL_programm)
    SQL_programm = input("даные" + kast)
    # Вставляем данные в таблицу
    cursor.execute(SQL_programm, ('Alice', 25))
    # Получаем данные из таблицы
    print(cursor.fetchall())
    # Закрываем соединение
    conn.close()
def wik():
    try:
        wicis = input("wiki" + kast)
        wikipedia.set_lang(lang)
        print(wikipedia.search(wicis))
        print("выбирите то что вам нужно из списка выше ")
        wicis = input("wici " + kast)
        print(wikipedia.summary(wicis))
    except :
        raise SystemExit("нету интернету или еще што мне было лень полнастью делать проверки")
    
def brower():
    try:
        class HTMLViewer(QMainWindow):
            def __init__(self, html):
                super().__init__()
                self.resize(1500,1400)
                self.setWindowTitle("brower")
                # Создаем виджет для отображения HTML-кода
                self.browser = QWebEngineView()
                self.setCentralWidget(self.browser)
                # Загружаем HTML-код в виджет
                self.browser.setHtml(html)
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            # Создаем объект CookieJar для хранения файлов cookies
            cookie_jar = CookieJar()
            # Загружаем HTML-код с веб-сайта с использованием файлов cookies
            print("не все сайты подержываютсья ")
            url = input("ведите ссылку" + kast)
            response = requests.get(url, cookies=cookie_jar)
            html = response.text
            print("loading . . .")
            # Отображаем HTML-код в графическом интерфейсе
            viewer = HTMLViewer(html)
            viewer.show()
            sys.exit(app.exec_())
    except :
        raise SystemExit("нету интернету или еще што мне было лень полнастью делать проверки")
        
def time_h():
    class ClockWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.resize(160,130)
            layout = QVBoxLayout()
            self.label = QLabel()
            layout.addWidget(self.label)
            self.setLayout(layout)
            timer = QTimer(self)
            timer.timeout.connect(self.update_time)
            timer.start(1000)  # обновление времени каждую секунду
        def update_time(self):
            current_time = QTime.currentTime()
            display_text = current_time.toString('hh:mm:ss')
            self.label.setText(display_text)
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        clock = ClockWidget()
        clock.show()
        sys.exit(app.exec_())
def game_bloks():
    class Character:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

    class Game:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.character = Character(0, 0)
            self.blocks = set()

        def draw(self):
            for y in range(self.height):
                for x in range(self.width):
                    if x == self.character.x and y == self.character.y:
                        print("@", end=" ")
                    elif (x, y) in self.blocks:
                        print("ㅤ", end=" ")
                    else:
                        print(".", end=" ")
                print()

        def run(self):
            while True:
                self.draw()
                inp_key = msvcrt.getch().decode()
                os.system("cls")
                print(" (w - up, s - down, a - left, d - right, b - place block, q - quit) ")
                action = inp_key
                if action == "w":
                    self.character.move(0, -1)
                elif action == "s":
                    self.character.move(0, 1)
                elif action == "a":
                    self.character.move(-1, 0)
                elif action == "d":
                    self.character.move(1, 0)
                elif action == "b":
                    x = int(input("Enter X coordinate for the block: "))
                    y = int(input("Enter Y coordinate for the block: "))
                    self.blocks.add((x, y))
                elif action == "q":
                    break
    game = Game(20, 15)
    game.run()
def tablet():
    vt="─"
    ht="│"
    bt="║"
    nt="═"
    gt="╪"
    yt="╚"
    vyt="╝"
    gyt="╔"
    uyt="╗"
    we="ㅤ "
    rt="╣"
    qt="╠"
    i = 15
    b=0
    tablet="nan"
    tablet = nt*i
    i=i-3
    we = we * i
    #txt =input()
    def btab():
        for a in range(0,10):
            print(bt+we+bt)  
    print(gyt + tablet + gt+tablet+uyt)  
    btab()
    #yt=qt
    #vyt=rt
    print(yt + tablet + gt+tablet + vyt)
    #btab()
    #print(yt + tablet + gt+tablet + vyt)
    
def web_perebod():    
    try:
        import sys
        from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QVBoxLayout, QWidget
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        from PyQt5.QtCore import QUrl
        from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
        from PyQt5.QtCore import QTimer, QTime, Qt
        import PyQt5.QtGui 
        import PyQt5.QtWidgets 
        #pip install PyQt5 PyQtWebEngine
    except:
        print("error lib")
    class BrowserWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("consolSH")
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl("https://translate.yandex.ru/"))
            self.setCentralWidget(self.browser)
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
    
def ping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', host]
    return subprocess.run(command, stdout=subprocess.PIPE).returncode == 0

def ip_py():
    os.mkdir(f'{os.getcwd()}/Cd/root')
    import pynet 




os.system("cls")
print(preview_text.renderText('consolSH'))
print("ДОБРО ПОЖАЛОВАТЬ В consolSH :)")
time.sleep(1)
if inethek == "true":
    print("интернет есть все ок")
elif inethek == "foles":
    print("интернета нету увы")
time.sleep(1)
os.system("cls")

while True:
    #гарячие клавишы 
    keyboard.add_hotkey("ctrl+q", lambda: exit)
    
    
    if admin() == True:
        adm = "#"
    else:
        adm = "~"

    command = input(os.getcwd() + adm + "sh" + kast)

    if command == "exit":
        print("Выход из syshab")
        exit()
    elif command == "dir":
        print(os.listdir())
    elif command.startswith("cm"):
        cm = command
        directory_name = cm.split(" ")[1]
        os.mkdir(directory_name)
        print(f"Создана директория {directory_name}")
    elif command.startswith("del"):
        directory_name = command.split(" ")[1]
        os.rmdir(directory_name)
        print(f"Директория {directory_name} удалена")
    elif command == 'help':
        print(' "dir" - (показать содержимое текущей директории),\f,"open" - открывает файлы (не все)  ')
        print("cm  <имя_директории> - (создать директорию), \f  del <имя_директории> - (удалить директорию). \f pwd - тикущий репозиторий \f games - убивалки времини \f install Winterm - установка Windows terminal ")
    elif command.startswith("cd"):
        try:
            cd = command
            directory_name = cd.split(" ")[1]
            os.chdir(directory_name)
        except FileNotFoundError:
            print("error file 1")
            
    elif command == "pwd":
        print(os.getcwd())
    elif command == "C:":
        print(C())
    elif command == "date":
        print (datetime.datetime.now())
    elif command == "filesystem":
        print(directoryс())
    elif command == "open":
        print("может открыть")
        print (openp)
        opencom = input("Введите формат файла: " + kast)
        if opencom == "txt":
            opentxt()
        elif opencom == "bat":
            directb= input ("Введите полный путь: " + kast)
            os.system(f"start {directb}")
            subprocess.call([directb])
            subprocess.call(["ping", "-c", "3", "google.com"])
        elif opencom == "exe":
            direct= input ("Введите полный путь:")
            os.system(r'direct')
        elif opencom == "jpg":
            openphoto()
        elif opencom == "png":
            openphoto()
        elif opencom == "wav":
            print("в разработке")
#            musics()
        elif opencom == "mp3":
            print("в разработке")
#            musics()
    elif command == "cmd":
        os.system(cmd)
        subprocess.call([cmd])
        subprocess.call(["ping", "-c", "3", "google.com"])
    elif command == "to close":
        print("Выход из syshab")
        print (":)")
        exit()
    elif command == "pip":
        package = input("Установить модуль :")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    elif command == "os platform":
        infoplatform()
    elif command == "pydire":
        print(sys.executable)
    elif command == "process":
        print(psutil.Process().cpu_percent(interval=1))
    elif command == "calc":
        calc()
    elif command == "sudo":
        sudo() 
    elif command.startswith("anti"):
        anit = command
        if len(anit.split()) == 1:  # Проверяем, содержит ли команда только "anti"
            print("Введите путь к файлу или URL")
        else:
            target = anit.split(" ")[1]
            anti_virus(target)
    elif command == "dec":
        dec()
    elif command == "cmdcom":
        cmdcom()
    elif command == "you-get -h":
        you_get_help()
    elif command == "apt":
        # Установка пакета с помощью apt
        package_name = input("package name" + kast)
        def install_with_apt(package_name):
            subprocess.call(['sudo', 'apt', 'install', package_name, '-y'])
    #    install_with_apt('python3')
    #    install_with_apt('git')
    elif command == "giner_password":
        gen_password()
    elif command == "hifr":
        hifr()
    elif  command.startswith("echo"):
        echo = command
        printe = echo.split(" ")[1]
        print(printe)
    elif command == "cmdadmin":
        os.system('C:/Windows/System32/conhost.exe')
    elif command == "binout":
        text_to_bits()
    elif command == "binin":
        text_from_bits()
    elif command == "scan system":
        scansystem()
    elif command == "cls":
        os.system("cls")
    elif command == "command -h":
       with open("command.txt", "r") as f: 
           f = str(f.readlines())
           print(f)
    elif command ==" str_cek":
         str_cek()
    elif command== "wiki":
        wik()
    elif command == "SQL":
        SQL()
    elif command == "browe":
         brower()
    elif command == "time":
        time_h()
    elif command =="games":
        games =['tetris','bloks']
        for numbe, letter in enumerate(games):
            print(numbe,".", letter)
        game = input("выбирите игру и впишыте номер"+kast)
        if game =="0":
             os.chdir('C:/Users/Home/Desktop/beta 3.0/consol/Cd/root/tetris')
             os.system('start.py')
        elif game == "1":
            game_bloks()
    elif command =="tablet":
        tablet()
    elif command =="installbib" :
        os.system('start impori.bat')
    elif command =="command":
        try:
            with open('command.txt', 'r') as file:
                read_file = file.read()
                print(read_file)
        except IOError:
            raise SystemExit("error fail 1")
            input()
    elif command =="info":
        try:
            with open('info.txt', 'r') as file: 
                read_file = file.read()
                print(read_file)
        except IOError:
            raise SystemExit("error fail 1")
            input()
    elif command =="install Winterm":
        #install Windows terminal
        subprocess.Popen('powershell.exe','winget install --id Microsoft.WindowsTerminal -e')
    elif command =="str":
        print(globals())
    elif command =="python help":
        command = input(kast)
        help(command)
    elif command =="ipconfig":
        try:
            ip_c=os.system("ipconfig")
            print(ip_c)
        except:
            print(socket.gethostbyname("python.org"))
    elif command =="ping ":
        ping =input("ведите айпи или ведите ссылку нажмите enter для проверки соеденения с  google")
        if ping == "":
            try:
                ping = os.system("ping google.com")
                print(ping)
            except:
                print("error inet 1")
        else:
            try:
                host=input(':')
                print("Проверяем соединение...")
                if ping(host):
                    print('С сервером установлена связь!')
                else:
                    print('Сервер недоступен.')
            except:
                print("error inet 1")
    elif command =="off pc":
        print("off")
        os.system('shutdown -s')
    elif command =="lib":
        print(sys.executable)
    elif command =="wep perevod":
         web_perebod()
    elif command ==" ":
        print("прабел")
    elif command.startswith("redact"):
        redact = command
        try:
            os.chdir("beta 3.0/consol/Cd/root/")
            defi = redact.split(" ")[1]
            if defi == "kast":
                kast = input("redact kast" + kast)
                try:
                    os.chdir("/beta 3.0/consol/Cd/root/kast")
                    with open("kast.txt", "a") as file: 
                        kast = file.readlines()
                        file.write(kast)
                    with open('kast.txt', 'r') as file: 
                        kast = file.read()
                    print(f"new kast{kast}")
                except:
                    print("erorr file 1")
            elif defi =="dir":
                try:
                    os.chdir("beta 3.0/consol/Cd/root/")
                    dir = input("redact dir" + kast)
                    with open('start direct.txt', 'a') as file: 
                        direct = file.readlines()
                        direct = file.write(dir)
                    os.chdir(direct)
                except:
                    print("error fail 1")
        except:
            print("erorr arg 1")
            cor_direct()
    elif command =="cmdhelp":
         help=input(kast)
         os.system("help "+help)
    elif command =="powerShell":
         command=input(f"PS {kast}")
         subprocess.Popen(f'powershell.exe','{command} Out-File -FilePath E:\PowerShellLogs\PrimerRabotiIzPython.txt')
    elif command == "py.net":
        ip_py()
     
     
     
    else:
        print("Неизвестная команда")
