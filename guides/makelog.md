
# MakeLog

Здесь я веду  записи по установке ПО, модуле и прочие рабочие записи.

## Установка Virtual Evnironments for Brewed Python on Mac OS

 Установка python

```bash
$brew install python3
```

Установка virtualenv с помощью pip

```bash
$pip3 install virtualenv
```

Создание виртуального окружения

```bash
$virtualenv -p python3 <путь к папке>
```

Создаем папку Environments

```bash
$mkdir Environments
$cd !$
$virtualenv learn_proj
```

Где learn_proj - название окружения

Активация окружения

```bash
$source learn_proj/bin/activate
```

Посмотрим расположение

```bash
$which python
$which pip
$pip list # будут только   setuptools, pip и  wheel
```

Теперь можно устанавливать пакеты

```bash
pip install numpy
pip install numpy
```

Выйти из окружения:

```bash
deactivate
```

## Установка Virtual Evnironments на Windows

## Перенос проекта из Bitbucket to Github

$ git clone <https://lwmd@bitbucket.org/lwmd/pyline.git>

$ cd pyline/

$ git remote add upstream <https://github.com/lowmoode/pyline.git>

$ git push upstream master

$ git push --tags upstream
Everything up-to-date

$ vim .

$ git remote -v
origin  <https://lwmd@bitbucket.org/lwmd/pyline.git> (fetch)
origin  <https://lwmd@bitbucket.org/lwmd/pyline.git> (push)
upstream        <https://github.com/lowmoode/pyline.git> (fetch)
upstream        <https://github.com/lowmoode/pyline.git> (push)

$ git remote set-url origin <https://github.com/lowmoode/pyline.git>

$ git remote -v
origin  <https://github.com/lowmoode/pyline.git> (fetch)
origin  <https://github.com/lowmoode/pyline.git> (push)
upstream        <https://github.com/lowmoode/pyline.git> (fetch)
upstream        <https://github.com/lowmoode/pyline.git> (push)

$ git remote rm upstream

$ git remote -v
origin  <https://github.com/lowmoode/pyline.git> (fetch)
origin  <https://github.com/lowmoode/pyline.git> (push)
