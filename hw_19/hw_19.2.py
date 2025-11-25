import requests
from urllib.parse import quote

BASE_URL = "http://127.0.0.1:8080"

def upload_image(img_url: str, filename: str) -> str:


    img_data = requests.get(img_url).content
    files = {"image": (filename, img_data, "image/png")}
    response = requests.post(f"{BASE_URL}/upload", files=files)
    if response.status_code == 201:
        data = response.json()
        return data["image_url"]
    else:
        raise Exception(f"Помилка при завантаженні: {response.status_code}, {response.text}")

def get_image_url(filename: str) -> str:


    filename_encoded = quote(filename)
    response = requests.get(f"{BASE_URL}/image/{filename_encoded}", headers={"Content-Type": "text"})
    if response.status_code == 200:
        data = response.json()
        return data["image_url"]
    else:
        raise Exception(f"Помилка при отриманні зображення: {response.status_code}, {response.text}")

def delete_image(filename: str) -> str:


    filename_encoded = quote(filename)
    response = requests.delete(f"{BASE_URL}/delete/{filename_encoded}")
    if response.status_code == 200:
        data = response.json()
        return data.get("message", "")
    else:
        raise Exception(f"Помилка при видаленні зображення: {response.status_code}, {response.text}")



if __name__ == "__main__":
    img_url = "https://i.postimg.cc/02tGZx7r/Znimok-ekrana-2025-11-25-o-17-08-07.png"
    filename = "example.png"


    uploaded_url = upload_image(img_url, filename)
    print(f"Зображення завантажено: {uploaded_url}")


    image_url = get_image_url(filename)
    print(f"Отримано URL з сервера: {image_url}")

    message = delete_image(filename)
    print(f"Видалення пройшло успішно: {message}")
