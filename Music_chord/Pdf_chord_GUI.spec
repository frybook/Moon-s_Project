import sys 
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

added_files = [
    ('pdf_chord_extraction_functionalization.py', '.'),
    ('roman.py', '.'),
    ('line_filter.py', '.')
]

a = Analysis(['Pdf_chord_GUI.py'],
             pathex=['path_to_your_script_directory'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
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
          name='Pdf_chord_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)  # Changed to False

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Pdf_chord_GUI')