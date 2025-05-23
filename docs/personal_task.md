# Отчет по индивидуальному кафедральному заданию
**Формулировка:** 

**Задачи:**

* Ознакомиться с существующим популярным ПО для автоматизации развертывания виртуальных машин и сред контейнеризации

* Более подробно изучить инструменты VMware, Vagrant, Virtualbox, VBoxManage, Docker, Docker Compose и их интерфейсы

* Получить навыки установки образов и настройки хостовых машин (вручную и с использованием Vagrant файлов) на ОС Linux, Windows

* Создать и настроить вручную Windows server 2016

---

## Оборудование и ПО

- **Хостовая ОС**: Windows 11 Pro; Kali Linuks 
- **Инструменты**: Windows 10, 11; PowerShell; Коммандная строка; Oracle Virtual Box; Docker; Docker Compose; Word; PDF; Telegram

---

## Ход работы:

### 1. 
Первым делом мы начали изучать всю предложенную теорию в вопросе виртуализации:
- популярное ПО виртуализации хостовых машин
- ПО для автоматизации развертывания виртуальных машин
- сред контейнеризации
Далее нашим наставником было принято использовать программу Virtualbox, так что мы углубились в изучение данного ПО для эффективной работы с ним (вся используемая литература предоставлена ниже)

### 2. 
Мы установили программу Oracle Virtual Box и с помощью нее скачали и успешно запустили свою первую Виртуальную Машину на ОС Linuks

![фото ВМ 2](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/pt_2.png)
![фото ВМ 1](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/pt_1.png)

### 3.
Далее на языке Python мы написали [скрипт](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/scrypt.py) для запуска, остановки, перезагрузки ВМ, а также вывода списка доступных ВМ
И успешно его протестировали
![фото ВМ 4](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/pt_4.png)

### 4.
Поработали с Docker, подняли docker-контейнер и написали свой [Dockerfile](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/Dockerfile) для активации и поднятия простого web-сервера 
После сборки образа запустили контейнер и проверили его работоспособность
![фото ВМ 3](https://github.com/Galaxy-1337/practice/blob/main/docs/media/personal_task/pt_3.png)


### 5.
Изучив Docker мы поработали с инструментальным средством Docker Compose и создали свое клиент-серверное приложение
Файлы, использованные для выполнения храняться в репозитории [по этой ссылке]()

---

## Итог

---

## Использованная литература:
### Первая тема

Инструменты для автоматизации развертывания ВМ:
1. [Существующие гипервизоры](https://servermall.ru/blog/kakoy-gipervizor-vybrat/)
2. [Terraform, официальный сайт](https://www.terraform.io/)
3. [Vagrant, официальный сайт](https://www.vagrantup.com/)
4. [Ansible, официальный сайт](https://www.ansible.com/)

Инструменты для контейнеризации:  
&nbsp;&nbsp;&nbsp;&nbsp;5. [Docker, официальный сайт](https://www.docker.com/)  
&nbsp;&nbsp;&nbsp;&nbsp;6. [Kubernetes, официальный сайт](https://kubernetes.io/)

### Вторая и третья тема:
&nbsp;&nbsp;&nbsp;&nbsp;7. [VirtualBox](https://ru.wikipedia.org/wiki/VirtualBox)  
&nbsp;&nbsp;&nbsp;&nbsp;8. [VBoxManage](https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud)  
&nbsp;&nbsp;&nbsp;&nbsp;9. [VMware](https://habr.com/ru/companies/kingston_technology/articles/484732/)  
&nbsp;&nbsp;&nbsp;&nbsp;10. [Литература по управлению ВМ с консоли](https://www.oracle.com/technical-resources/articles/it-infrastructure/admin-manage-vbox-cli.html)  

### Четвертая тема:
&nbsp;&nbsp;&nbsp;&nbsp;11. [официальный сайт Windows, для скачивания образа сервера](https://www.microsoft.com/en-us/evalcenter/download-windows-server-2016)
