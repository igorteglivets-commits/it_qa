import xml.etree.ElementTree as ET
import logging
import os

logging.basicConfig(level=logging.INFO)

def get_incoming_from_group(xml_file, group_number):
    if not os.path.exists(xml_file):
        logging.warning(f"Файл {xml_file} не знайдено!")
        return None

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError as e:
        logging.error(f"Помилка парсингу {xml_file}: {e}")
        return None

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")
            if incoming is not None:
                logging.info(f"Значення incoming для групи {group_number}: {incoming.text}")
                return incoming.text
            logging.info(f"Група {group_number} знайдена, але <timingExbytes>/<incoming> відсутній")
            return None

    logging.info(f"Групу {group_number} не знайдено")
    return None

def check_files_for_group(group_number, files=["login.xml", "groups.xml"]):

    results = {}
    for f in files:
        results[f] = get_incoming_from_group(f, group_number)
    return results

group_num = 0
incoming_values = check_files_for_group(group_num)
print(incoming_values)
