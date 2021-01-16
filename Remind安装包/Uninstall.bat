@echo off
rem 杀进程&删除服务及注册表
taskkill /F /IM remind.exe
net stop Remind
sc delete Remind
del /q C:\Users\Administrator\Desktop\remind.exe