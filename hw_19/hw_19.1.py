import requests

API_KEY = "1Tm1tMpFdFQYiM0jfUvAwVNX6NGXCerO0fcDHvwo"
BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

CAMERAS = ["fhaz", "rhaz"]



def fetch_photos(sol: int, camera: str) -> list:
    params = {"sol": sol, "camera": camera, "api_key": API_KEY}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f" Помилка запиту для камери {camera}: {response.status_code}")
        return []

    data = response.json()
    return data.get("photos", [])


def download_photo(url: str, filename: str):
    resp = requests.get(url)
    resp.raise_for_status()
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"Збережено файл: {filename}")


def save_first_n_photos(photos: list, n: int = 2):
    for idx, photo in enumerate(photos[:n], start=1):
        download_photo(photo["img_src"], f"mars_photo{idx}.jpg")


def main():
    sol = 1000
    photos = []

    for camera in CAMERAS:
        photos = fetch_photos(sol, camera)
        if photos:
            print(f"Знайдено фото на sol={sol}, камера={camera}")
            break

    if not photos:
        print(f" Для sol={sol} немає фото жодною перевіреною камерою.")
        return

    print(f"Завантажуємо перші {min(2, len(photos))} фото...")
    save_first_n_photos(photos)


if __name__ == "__main__":
    main()
