# API Pet project.
Api для внутреннего пользования. Пользователи, вакансии, резюме для frontend'a. 

## Развертывание проекта на локальной машине
Все рекомендации написаны под **Ubuntu 22.04**, на **windows** не проверял.
По всем вопросам стучите https://t.me/Flopp

#### **Ubuntu**
1) Скопируйте репозиторий на локальный компьютер ```git clone *ssh ссылка на репо*```
2) Установите python 3.11 
    ``` 
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.11
    ```
3) Создайте виртуальное окружение в корне проекта ```python3 -m venv env``` 
4) Установите pip ```sudo apt install pip```
5) Загрузите зависимости ```pip3 install -r requirements.txt```
6) Создайте файл в корне проекте ```.env``` и перенесите в него переменные из файла ```.env.sample``` (за тем, что ставить на место значений - в тг)
7) Выполните миграции в базу данных ```python3 manage.py migrate```
8) Запустите DRF приложение ```python3 manage.py runserver``` (по умолчанию запускается 127.0.0.1:8000)


***Будет дополняться в процессе***

#### **Windows**
1) Скопируйте репозиторий на локальный компьютер ```git clone *ssh ссылка на репо*```
2) Установите python 3.11 https://www.python.org/downloads/
3) Создайте виртуальное окружение в корне проекта ```python -m venv env``` 
4) Проверьте, установлен ли pip (менеджер пакетов). Проверить командой ```pip --version```. Если нет - вот ссылка https://www.dataquest.io/blog/install-pip-windows/)
5) Загрузите зависимости ```pip install -r requirements.txt```
6) Создайте файл в корне проекте ```.env``` и перенесите в него переменные из файла ```.env.sample``` (за тем, что ставить на место значений - в тг)
7) Выполните миграции в базу данных ```python manage.py migrate```
8) Запустите DRF приложение ```python manage.py runserver``` (по умолчанию запускается 127.0.0.1:8000)

***Будет дополняться в процессе***


## Main back TODO
- [x] Создать приложение
- [x] Создать модель пользователя
- [x] Дополнить json тестовыми данными для пользователей (json/users.json)
- [x] Создать модель резюме
- [x] Создать модель вакансии
- [ ] Реализовать заполнение тестовыми данные
- [ ] Реализовать функционал авторизации
- [ ] Реализовать систему прав/ доступов
- [ ] Реализовать функционал авторизации через сторонние ресурсы? (уточнить у фронта / ресерч информации, как делается на стеке react + drf)
