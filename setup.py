from setuptools import setup

APP = ['todo.py']
APP_NAME = "To-do"
DATA_FILES = ["daily.txt", "date.txt","day.txt", 'week.txt', 'month.txt']
OPTIONS = {'argv_emulation': True, 'iconfile': 'icon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
