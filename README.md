
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
    <a href="https://github.com/xHak2215/consol"><strong>документация»</strong></a>
    <br />
    <br />
    <li><a href="https://github.com/xHak2215/consol/tree/main/consol">View Demo</a></li>
    <br />
  </p>
</div>



<details>
  <summary>автор</summary>
  <ol>
    <li>
      <ul>
      <li><a href="#about-the-project">основной проект</a>
      </ul><ul>
      <li><a href="https://t.me/HITHELL">telegram</a></li>
      </ul>
    </li>
  </ol>
</details>






<!-- consolSH -->
<h2>информация </h2>


<h3> установка: </h3>

для работы приложения необходим python 3.12v или выше  

```sh
git clone https://github.com/xHak2215/consol
```
или просто  <a href="https://github.com/xHak2215/consol/archive/refs/heads/main.zip">скачять</a> 
<h3>затем необходимо запустить файл setup.py далее дождаться установки библиотек и все!</h3>

за тем посоветую почитать файл<a href="https://github.com/xHak2215/consol/tree/main/consol/info.txt"> info.txt</a>


потдержываемые системы:
* windows
* Linux

поддерживаемые языки:
* Русский
* англиский(не полный перевод)

<h2>настройка</h2>

настройки храняться в файле <a href="https://github.com/xHak2215/consol/blob/main/consol/settings.py">settings.py</a>(примечание переименовывать файл не льзя)
<h3>при не нохождении файла будут использываны настройки по умолчянию</h3>
<h3>сам файл</h3>

```python
#язык (в разроботке) ru - русский , eng - English;
lang ="ru"
#logs;on-1,off-0
log_actived=0
#log save
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
#среда исполнения SH-мая консоль cmd-консоль виндовс или Линукс в зависимости от системы
sreda="SH"
```


<p align="right">(<a href="#readme-top">↑верх↑</a>)</p>










