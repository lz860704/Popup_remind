@echo off
rem ���ע�������
set current_path=%cd%
%current_path%\instsrv.exe Remind %current_path%\srvany.exe
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /f
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /v Application /t REG_SZ /d "C:\\Users\\Administrator\\Desktop\\remind.exe" /f
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Remind\Parameters /v Description /t REG_SZ /d "���ѹ���" /f
sc start Remind