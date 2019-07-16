# CircusCharlieNeat
## jupyter notebook
https://github.com/AmigoManuel/CircusCharlieNeat/blob/master/CircusCharlieNeatJup.ipynb
## Python implementation
https://github.com/AmigoManuel/CircusCharlieNeat/blob/master/main.py
## Neat Config file
https://github.com/AmigoManuel/CircusCharlieNeat/blob/master/config-feedforward

# Importante
## Para obtener variables del entorno
copiar carpeta CircusCharlie-Nes en 
```
...\Anaconda3\Lib\site-packages\retro\data\stable\
```
## Tranformación a video
1. Instalar Chocolatey desde la CMD de Windows
```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
2. Reiniciar CMD
3. Instalar ffmpeg
```
choco install ffmpeg
```
4. Reiniciar CMD
5. Sobre la carpeta de ficheros bk2 ejecutar
```
python -m retro.scripts.playback_movie nombre_de_partida.bk2
```
