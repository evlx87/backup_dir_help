import os
import shutil

SOURCE_TARGET = ""
DESTINATION_TARGET = ""


def copy_directory(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(destination_dir, item)

            if os.path.isfile(source_item):
                shutil.copy2(source_item, destination_item)
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)

        print("Директория успешно скопирована")
    except Exception as e:
        print("Ошибка при копировании директории: ", str(e))


copy_directory(SOURCE_TARGET, DESTINATION_TARGET)
