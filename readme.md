##gRPC server
___

>##Инструкция по использованию

Клонирование репозитория
`-- git clone https://github.com/inTACdevelopers/Server.git`

>###Создание базы данных
> В своём проекте мы применили базу данных postgres.
> Внутри папки database можно найти файл dump.sql, его нужно импортировать в базу данных

>###Настройка окружения
> Если среда разработки не предполагает автоматическое создание виртуального окружения, его необходимо создать
>>Linux
>> 
>>`python -m venv venv`
>>
>>`source venv/bin/activate`
>>
>>Windows
>>
>>`python -m venv venv`
>>
>>`venv\Scripts\activate.bat`
>
> После включения виртуального окружения необходимо скачать пакеты python для работы с сервером
>+ `pip install certifi`
>+ `pip install charset-normalizer`
>+ `pip install grpcio`
>+ `pip install grpcio-tools`
> + `pip install protobuf`
> + `pip install psycopg2`
> + `pip install requests`
> + `pip install setuptools`



>###Работа с файлами
> В директории проекта `Server\database` необходимо создать директорию photos.
> 
> Также на уровне проекта необходимо создать файл conf.py
> ```python
> import os
> 
> HOST = "" #Ip адрес, на котором запущенн сервер postgreSQL
> PORT = 0000 #Порт, который слушает база данных (обычно 5432)
> USER = "" # Пользователь базы данных
> PASSWORD = "" #Пароль пользователя базы данных
> DB_NAME = "" #Имя базы данных
> 
> SERVER_IP = "" #Ip адрес удалённого сервера
> SERVER_PORT = 0000 #Порт, на котором запущен сервер 
> 
> # Данные для запуска сервера локально
> DEBAG_SERVER_IP = "localhost"
> DEBAG_SERVER_PORT = 8080
>
> #Константа состояния:
> #True - сервер запущен локально
> #False - сервер запущен удалённо 
> DEBAG = True
>
> #Путь до папки photos, созданной в прошлом шаге
> DEBAG_PHOTO_DIR = os.getcwd() + "/database/photos/"
> # Путь до папки photos, если сервер запускается НЕ локально
> PHOTO_DIR = ""
> ``` 
> Этот файл определяет необходимые для работы сервера константы.
> 

Теперь сервер готов к запуску :)

`python3 main.py`












