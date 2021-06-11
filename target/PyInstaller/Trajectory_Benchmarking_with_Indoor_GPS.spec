# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/karthick/SEMESTER 2/SDP LAB/SDP_MAIN_FILE/FINAL/GUI_for_Trajectory_Benchmarking_with_Indoor_GPS/src/main/python/main.py'],
             pathex=['/home/karthick/SEMESTER 2/SDP LAB/SDP_MAIN_FILE/FINAL/GUI_for_Trajectory_Benchmarking_with_Indoor_GPS/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/karthick/.local/share/virtualenvs/GUI_for_Trajectory_Benchmarking_with_Indoo-424W1yGH/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/karthick/SEMESTER 2/SDP LAB/SDP_MAIN_FILE/FINAL/GUI_for_Trajectory_Benchmarking_with_Indoor_GPS/target/PyInstaller/fbs_pyinstaller_hook.py'],
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
          name='Trajectory_Benchmarking_with_Indoor_GPS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Trajectory_Benchmarking_with_Indoor_GPS')
