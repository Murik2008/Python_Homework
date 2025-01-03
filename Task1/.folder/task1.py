"""
Задание 1. Логирование с использованием нескольких файлов 
Напишите скрипт, который логирует разные типы сообщений в разные файлы. 
Логи уровня DEBUG иINFOдолжнысохраняться вdebug_info.log, 
а логи уровня WARNINGивыше—вwarnings_errors.log.//
"""

import logging

logger = logging.getLogger("multi_file_logger")
logger.setLevel(logging.DEBUG)  

debug_info_handler = logging.FileHandler("debug_info.log")
debug_info_handler.setLevel(logging.DEBUG)

warnings_errors_handler = logging.FileHandler("warnings_errors.log")
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("Это сообщение уровня DEBUG.")
logger.info("Это сообщение уровня INFO.")
logger.warning("Это сообщение уровня WARNING.")
logger.error("Это сообщение уровня ERROR.")
logger.critical("Это сообщение уровня CRITICAL.")