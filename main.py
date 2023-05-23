import os
import shutil
import logging
import sys

SOURCE_TARGET = "C:\\test\\old"
DESTINATION_TARGET = "C:\\test\\new"
LOG_FILE = "backup_logs.log"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Обработчик для записи в лог-файл
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Обработчик для вывода в терминал
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)

# Форматтер для лог-сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def copy_directory(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(destination_dir, item)

            if os.path.isfile(source_item):
                if not os.path.exists(destination_item) or os.path.getmtime(source_item) != os.path.getmtime(destination_item):
                    shutil.copy2(source_item, destination_item)
                    logging.info(f"Копирование файла: {item} ({source_item})")
            elif os.path.isdir(source_item):
                if not os.path.exists(destination_item):
                    shutil.copytree(source_item, destination_item)
                    logging.info(f"Копирование директории: {item} ({source_item})")

        print("Директория успешно скопирована")
    except Exception as e:
        logging.info(f"Ошибка при копировании директории: {str(e)}")


copy_directory(SOURCE_TARGET, DESTINATION_TARGET)
