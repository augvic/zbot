from PyInstaller.building.build_main import Analysis
from PyInstaller.building.api import EXE, PYZ
import os

analysis = Analysis(
    scripts=['main.py'],
    pathex=[os.path.abspath('.')],
    datas=[('.env', '.')],
    optimize=0,
    hiddenimports=[
        'engineio.async_drivers.threading',
        'socketio',
        'flask_socketio'
    ]
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    name='zBot',
    upx=True,
    icon="icon.ico"
)
