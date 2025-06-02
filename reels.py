import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import subprocess

def download_reel(url):
    print(f"\nMemproses URL: {url}")

    # Setup Chrome options agar berjalan tanpa GUI
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    sleep(5)

    # Ambil URL asli setelah redirect
    actual_url = driver.current_url
    print(f"URL setelah redirect: {actual_url}")

    try:
        close_btn = driver.find_element(By.XPATH, "//div[@aria-label='Close']")
        close_btn.click()
    except:
        pass  # Abaikan kalau tidak ada popup

    driver.quit()

    # Jalankan yt-dlp hanya untuk URL redirect
    args = [
        "yt-dlp",
        "-f", "best",
        "--output", os.path.join("output", "%(id)s.%(ext)s"),
        actual_url
    ]

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in iter(lambda: process.stdout.readline(), b''):
        print(line.decode("utf-8"))

    process.wait()
    print("Download selesai.\n")

if __name__ == "__main__":
    print("=== Reels Downloader FB ===")
    while True:
        url = input("Masukan link reels atau video FB (atau ketik 'exit' untuk keluar): ").strip()
        if url.lower() == "exit":
            print("Keluar dari program.")
            break
        if not url.startswith("http"):
            print("Masukan link yang valid!")
            continue
        try:
            download_reel(url)
        except Exception as e:
            print(f"Terjadi kesalahan: {e}\nCoba lagi.\n")
