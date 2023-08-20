import socket
import random
import pathlib
import subprocess


def get_private_ip() -> str:
    return socket.gethostbyname(socket.gethostname())


def random_wallpaper() -> None:
    path = pathlib.Path.home() / 'wallpapers'
    wallpaper = [i for i in path.iterdir()]
    subprocess.run(['feh', '--bg-fill', '--no-fehbg', wallpaper[random.randint(0, len(wallpaper)-1)]], check=True)
