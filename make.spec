from PyInstaller.building.build_main import Analysis
from PyInstaller.building.api import EXE, PYZ

analysis = Analysis(
    scripts=['./src/io/cli.py'],
    optimize=0
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    name='zBot_cli',
    upx=True,
    icon="./src/storage/images/icon.ico"
)
