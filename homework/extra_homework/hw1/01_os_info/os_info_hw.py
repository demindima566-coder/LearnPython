#пользовался дополнительным источником с хабра
#https://habr.com/ru/articles/864830/
import platform
import sys

with open ("OS info.txt", "w", encoding="utf-8") as f:

    f.write(f"System: {platform.system()}\n")
    f.write(f"Release: {platform.release()}\n")
    f.write(f"Platform: {platform.platform()}\n")
    f.write(f"Python version  is {sys.version}\n")


