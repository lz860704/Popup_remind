#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lz

import PySimpleGUI as sg
import time


# 每日进行提醒
while True:
    time_now = time.strftime("%H:%M:%S",time.localtime())
    # TODO：此处可以添加try和except进行问题排查
    if time_now == "08:29:00":
        sg.popup('上班你打卡了么?',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    elif time_now == "10:15:00":
        sg.popup('补充水分~ 起来活动一下~',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')    
    elif time_now == "11:00:00":
        sg.popup('上午的【测试开始】你发了么?',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    elif time_now == "14:00:00":
        sg.popup('邮件记得当天回复呀~~!',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    elif time_now == "15:15:00":
        sg.popup('补充水分~ 起来活动一下~',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ') 
    elif time_now == "17:00:00":
        sg.popup('别忘了申请今天的工作量昂~~满满的绩效分',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ') 
    elif time_now == "17:30:00":
        sg.popup('下班记得打卡哦~~',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    elif time_now == "19:00:00":
        sg.popup('辛苦你了~ 但也要记得发送日报哈~~',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    else:
        pass

# 每周四进行提醒
while True:
    time_wednesday = time.strftime("%w:%H:%M:%S",time.localtime())
    if time_now == "4:16:00:00":
        sg.popup('周四了,记得发本周任务汇报昂~~!',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    else:
        pass

# 每周五进行提醒
while True:
    time_friday = time.strftime("%w:%H:%M:%S",time.localtime())
    if time_now == "5:18:00:00":
        sg.popup('周五了,记得提交SR昂~~!',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    elif time_now == "6:14:30:00":
        sg.popup('周六了,SR你真的提交了么？^ ^',auto_close=True,auto_close_duration=180,title='提醒',font=("微软雅黑",16),custom_text=' 收到 ')
    else:
        pass