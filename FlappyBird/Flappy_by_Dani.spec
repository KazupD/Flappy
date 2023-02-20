from kivy_deps import sdl2, glew
import pkg_resources.py2_warn
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\Acer1\\Desktop\\Flappy\\game.py'],
             pathex=['C:\\Users\\Acer1\\Desktop\\FlappyBird'],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Flappy_by_Dani',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Acer1\\Desktop\\Flappy\\myicon.ico')
coll = COLLECT(exe, Tree('C:\\Users\\Acer1\\Desktop\\Flappy\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Flappy_by_Dani')
