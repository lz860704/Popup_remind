@echo off
rem 添加注册表及服务
set current_path=%cd%
%current_path%\instsrv.exe Remind %current_path%\srvany.exe
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /f
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /v Application /t REG_SZ /d "C:\\Users\\Administrator\\Desktop\\remind.exe" /f
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /v Description /t REG_SZ /d "提醒工具" /f
sc start Remind