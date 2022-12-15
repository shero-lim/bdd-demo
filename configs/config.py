import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

config = {
    "user_data_dir_of_chrome": os.environ["user_data_dir_of_chrome"],
    "user_data_dir_of_electron": os.environ["user_data_dir_of_electron"],
    "electron_binary": os.environ["electron_binary"],
    "site_url": os.environ["site_url"],
    "selenium_server": os.environ["selenium_server"] or "http://127.0.0.1:4444/wd/hub",
    "concurrency": int(os.environ["concurrency"]) or 1,
    "default_browser": os.environ["default_browser"] or "chrome",
}