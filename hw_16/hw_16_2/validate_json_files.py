import os
import json
import logging

def validate_json_files(folder_path: str, log_filename: str):

    # Налаштування логера
    logging.basicConfig(
        filename=log_filename,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    for filename in os.listdir(folder_path):

        if not filename.lower().endswith(".json"):
            continue

        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"[OK] {filename} — валідний JSON")

        except Exception as e:
            print(f"[ERROR] {filename} — НЕВАЛІДНИЙ JSON")
            logging.error(f"{filename}: {e}")


if __name__ == "__main__":
    validate_json_files(
        folder_path=".",
        log_filename="json__Ivaniv.log"
    )
