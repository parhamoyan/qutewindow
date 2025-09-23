import os
import platform

if platform.system() == "Darwin":
    pyside6_ui_path = r"venv/bin/pyside6-uic"
    pyside6_rcc_path = r"venv/bin/pyside6-rcc"
    pyside6_lrelease_path = r"venv/bin/pyside6-lrelease"
else:
    pyside6_ui_path = r"venv\Scripts\pyside6-uic.exe"
    pyside6_rcc_path = r"venv\Scripts\pyside6-rcc.exe"
    pyside6_lrelease_path = r"venv\Scripts\pyside6-lrelease.exe"


os.system(
    r"{} platforms/windows/title_bar/resources.qrc -o platforms/windows/title_bar/resources_rc.py".format(
        pyside6_rcc_path
    )
)
