@echo off
rem ɱ����&ɾ������ע���
taskkill /F /IM remind.exe
net stop Remind
sc delete Remind
del /q C:\Users\Administrator\Desktop\remind.exe