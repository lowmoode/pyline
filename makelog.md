
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
