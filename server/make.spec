from PyInstaller.building.build_main import Analysis
from PyInstaller.building.api import EXE, PYZ

analysis = Analysis(
    scripts=['./src/io/api.py'],
    optimize=0
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    name='zBotServer',
    upx=True,
    icon="./icon.ico"
)
