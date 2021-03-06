import os

from colorama import Fore

from plugin import Platform, plugin, require


@require(platform=Platform.LINUX, native='ims')
@plugin('movies')
def movies(jarvis, s):
    """Jarvis will find a good movie for you"""
    movie_name = jarvis.input("What do you want to watch?\n", Fore.RED)
    os.system("ims " + movie_name)
