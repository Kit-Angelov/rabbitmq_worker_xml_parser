"""
Пакет базовых универсальныйх функций
"""
import zipfile
import os
import shutil


# создание "временной" директории
def mk_temp_dir(path_zip):
    path_dir = str(path_zip).replace(".zip", "")
    try:
        os.mkdir(str(path_dir))
    except:
        print('Директория уже существует')
    finally:
        return path_dir


# удаление "временной" директории"
def rm_temp_dir(temp_path):
    try:
        shutil.rmtree(temp_path)
    except:
        print('Директории не существует')


# распаковка файла зип
def unzip(path_zip):
    path_dir = mk_temp_dir(path_zip)
    with zipfile.ZipFile(path_zip, "r") as zip_ref:
        file = zip_ref.namelist()
        zip_ref.extractall(path_dir)
    return file, path_dir