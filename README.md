.
<a id="readme-top"></a>





<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/xHak2215/consol">
    <img src="srk/Ico_image.png" alt="ico" width="80" height="80">
  </a>

  <h3 align="center">consolSH</h3>

  <p align="center">
    consol
    <br />
    <a href="https://github.com/xHak2215/consol"><strong>.</strong></a>
    <br />
  </p>
</div>



<details>
  <summary>автор</summary>
  <ol>
    <li>
      <ul>
      <li><a href="#about-the-project">основной проект</a></li>
      </ul><ul>
      <li><a href="https://t.me/HITHELL">telegram</a></li>
      </ul>
    </li>
  </ol>
</details>






<!-- consolSH -->
<h2>информация </h2>

<h3>consolSH - это попытка соединить возможностьи CMD,Python,bash(терминал линукса)
</h3>


<h3> установка: </h3>

для работы приложения необходим <a href="https://www.python.org/"> python 3.12v</a> или выше желательно наличие pip

```sh
git clone https://github.com/xHak2215/consol
```
или же с помощю pip:
```sh
pip download git+https://github.com/xHak2215/consol                                                       
```
или просто  <a href="https://github.com/xHak2215/consol/archive/refs/heads/main.zip">скачять</a> 
<h3>затем необходимо запустить файл setup.py далее дождаться установки библиотек и все!</h3>

за тем посоветую почитать файл<a href="https://github.com/xHak2215/consol/tree/main/consol/info.txt"> info.txt</a>
и ввести команду :

```Sh
help

```



потдерживаемые системы:
* windows
* Linux (крайне не стабильная работа работаю над этим)


поддерживаемые языки:
* Русский
* Англиский (не полный перевод)

<h2>настройка</h2>

настройки расположены в файле <a href="https://github.com/xHak2215/consol/blob/main/consol/settings.py">settings.py</a>(примечание переименовывать файл нельзя)
<h4>при не нохождении файла будут использованы настройки По умолчанию</h4>
<h3>содержимое файл</h3>

```python
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
```
<h2>особенности</h2>

<h3>переменные (var)</h3>

переменные По умолчанию:
* $cd - директория запуска консоли
* $ip - число пи

<h3>задать сваю прерменную</h3>

```consolSH
var nameVar=dataVar
```
<h3>ввод данных input</h3>
синтакис команды

```consolSH
input:название переменой,выводимый текст на строке ввода
```

<h3>apt</h3>
<h4>работает на основе pip может сачивать репозитории с GitHyb </h4>
<h4>имеет модули  для получения списка ведите: </h4>

```consolSH
apt-p
```
<h4>модули будут дополняться структура модулей схожа с библиотеками python</h4>


<p align="right">(<a href="#readme-top">↑верх↑</a>)</p>

<input type="button" name="↑верх↑" value="#readme-top"/>










