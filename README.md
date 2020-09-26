<h1 align="center">Добро пожаловать в b0mb3r CLI 👋</h1>
<p align="center">
    CLI для смс-бомбера <a href=https://github.com/crinny/b0mb3r>b0mb3r</a>
    <br /><br />
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</p>


## 📍 Что это такое?
 > b0mb3r_cli - это «консольная утилита‎» или ‎«расширение» для работы с [b0mb3r](https://github.com/crinny/b0mb3r). Также вы можете использовать `b0mb3r_cli`, 
как класс (импортируя класс `Bomber` из модуля `b0mb3r_cli`). Примеры ниже 


## 🚀 Установка

1. **Установите Python** версии не ниже 3.7. Сделать это можно так:

    #### Для Windows

    Скачайте установщик с [официального сайта](https://www.python.org/downloads/) и запустите его. Убедитесь, что при установке отметили галочку ![Add Python to PATH](https://user-images.githubusercontent.com/42045258/69171091-557d2780-0b0c-11ea-8adf-7f819357f041.png)
    После установки `Python 3` установите [git](https://git-scm.com/download/win).

    #### Для Android

    Установите приложение [Termux](https://play.google.com/store/apps/details?id=com.termux), запустите его и введите следующую команду:
     ```sh
     pkg install python git clang make openssl -y
     ```
     #### Для Linux

     Скорее всего, у вас уже установлен Python 3. Если это не так, следуйте [инструкции](https://realpython.com/installing-python/#linux)
     Тоже самое с `git`, но если это не так, следуйте [инструкции](https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git)

    > Можно не устанавливать `git`, а просто  скачать архив, распокавать его и делать всё по инструкции (пропуская момент с `git clone...`).
     
2. **Установите b0mb3r_cli**, введя следующие команды в [командную строку](http://comp-profi.com/kak-vyzvat-komandnuyu-stroku-ili-konsol-windows/) (Windows), терминал (Linux) или Termux (Android):

```sh
git clone https://github.com/Moonquit/b0mb3r_cli.git
cd b0mb3r_cli
python setup.py install
```
> Если у вас ещё не был установлен [b0mb3r](https://github.com/crinny/b0mb3r), то он будет автоматически установлен!


## 🚩 Запуск

Всё просто! Введите команду `b0mb3r_cli` или `bomber_cli` и интерфейс бомбера будет запущен. Команда доступна из любой директории. Также, возможен запуск:
 ### Linux:
 ```sh
 cd b0mb3r
 python3 -m b0mb3r_cli
 ```

 ### Другие ОС:
 ```sh
 cd b0mb3r 
 python b0mb3r_cli
 ```


## 💻 Расширенное использование
Примеры использования класса `Bomber`:
```python
from b0mb3r_cli import Bomber

Bomber.start(phone="79995554433", cycles=150) # Запуск бомбера на номер `phone` с количеством повторов `cycles`
```
Или:
```python
bomber = Bomber()
bomber.start(phone="79995554433") # Запуск бомбера (по умолчанию cycles = 100)
```
Также доступны методы  «бысторого» и «кастомного‎» запуска (для настройки бомбера в терминале):
```python
from b0mb3r_cli import Bomber

bomber = Bomber()

bomber.quick_start()
# or
bomber.custom_start()
```

## 📝 Лицензия
Проект распространяется под лицензией [MIT](https://github.com/Moonquit/b0mb3r_cli/blob/master/LICENSE). Скачивая программное обеспечение из [этого](https://github.com/Moonquit/b0mb3r_cli) репозитория, вы соглашаетесь с ней. По условиям лицензии вы обязаны упоминать автора и лицензию в своей работе.

## Stargazers over time

[![Stargazers over time](https://starchart.cc/Moonquit/b0mb3r_cli.svg)](https://starchart.cc//Moonquit/b0mb3r_cli)
