"""
Пакет базовых универсальныйх функций
"""
import zipfile
import os
import shutil


# создание "временной" директории
def mk_temp_dir(path_zip, base_path):
    relative_path_zip = os.path.basename(path_zip)
    path_dir = os.path.join(base_path, (str(relative_path_zip).replace(".zip", "")))
    try:
        os.mkdir(path_dir)
    except Exception as e:
        print('Error: ', e)
    finally:
        return path_dir


# удаление "временной" директории"
def rm_temp_dir(path_dir):
    try:
        shutil.rmtree(path_dir)
    except Exception as e:
        print('Error: ', e)


# распаковка файла зип
def unzip(path_zip, base_path):
    path_dir = mk_temp_dir(path_zip, base_path)
    with zipfile.ZipFile(path_zip, "r") as zip_ref:
        file = zip_ref.namelist()
        zip_ref.extractall(path_dir)
    return file, path_dir
