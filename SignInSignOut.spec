# SignInSignOut.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py', 'resources_rc.py'],  # Include the generated resource file
    pathex=['C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final'],
    binaries=[],
    datas=[
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\Database\\TimesRecord.db', 'Database'),
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\Windows\\AddAssociate.ui', 'Windows'),
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\Windows\\AdminWindow.ui', 'Windows'),
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\Windows\\CurrentView.ui', 'Windows'),
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\Windows\\PastWindow.ui', 'Windows'),
        ('C:\\Users\\SEXES\\PycharmProjects\\SDEV265Final\\IMGs', 'IMGs'),  # Add this line to include the IMGs folder
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SignInSignOut',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Ensure no console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
