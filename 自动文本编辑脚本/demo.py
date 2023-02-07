# -*- encoding:utf-8 -*-
import os,sys
import win32gui
import win32con
import win32api
import win32clipboard
import time

from_pos_x = 100
from_pos_y = 50

def do_key_input(msg, clip_board_mode = True, key_sleep = 0):
    if clip_board_mode:  # 剪贴板方式
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(msg)
        win32clipboard.CloseClipboard()
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(ord('V'), 0, 0, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)
    else:  # 按键输入方式
        for c in msg:
            time.sleep(key_sleep)
            if c == '!':
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                win32api.keybd_event(49, 0, 0, 0)
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(49, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif c == ':':
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                win32api.keybd_event(186, 0, 0, 0)
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(186, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif c == ',':
                win32api.keybd_event(188, 0, 0, 0)
                win32api.keybd_event(188, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif c == '.':
                win32api.keybd_event(190, 0, 0, 0)
                win32api.keybd_event(190, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif c == '/':
                win32api.keybd_event(191, 0, 0, 0)
                win32api.keybd_event(191, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif c == '\\':
                win32api.keybd_event(220, 0, 0, 0)
                win32api.keybd_event(220, 0, win32con.KEYEVENTF_KEYUP, 0)
            else:
                code = ord(c)
                if code >= 97 and code <= 122:
                    code -= 32
                    win32api.keybd_event(code,0,0,0)
                    win32api.keybd_event(code,0,win32con.KEYEVENTF_KEYUP,0)
                elif code >= 65 and code<=90:
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    win32api.keybd_event(code, 0, 0, 0)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)
                else:
                    win32api.keybd_event(code, 0, 0, 0)
                    win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)

def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def wait_for_window(targetTitle, max_time=5):
    t = time.time()
    while time.time() - t < max_time:
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        for hwnd in hWndList:
            try:
                clsname = win32gui.GetClassName(hwnd)
                title = win32gui.GetWindowText(hwnd)
                if (title.find(targetTitle) >= 0):
                    return hwnd
            except Exception as ex:
                print(ex)
        time.sleep(0.2)
    return None

os.startfile('notepad')
hwnd = wait_for_window("记事本", max_time=3)  # 最多等3秒钟
if hwnd is None: sys.exit(0)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, from_pos_x, from_pos_y, 600, 400, win32con.SWP_SHOWWINDOW)
time.sleep(0.5)
mouse_click(from_pos_x+130, from_pos_y+40)
time.sleep(1)
mouse_click(from_pos_x+140, from_pos_y+80)
time.sleep(1)
hwnd2 = wait_for_window("字体", max_time=3)  # 最多等3秒钟
if hwnd2 is None: sys.exit(0)
win32gui.SetWindowPos(hwnd2, win32con.HWND_TOPMOST, from_pos_x, from_pos_y, 600, 600, win32con.SWP_SHOWWINDOW)
for i in range(30): mouse_click(from_pos_x+420, from_pos_y+190)
time.sleep(1)
mouse_click(from_pos_x+420, from_pos_y+120)
time.sleep(0.2)
mouse_click(from_pos_x+420, from_pos_y+120)
time.sleep(0.2)
# mouse_click(from_pos_x+380, from_pos_y+90)
mouse_click(from_pos_x+380, from_pos_y+150)
time.sleep(1)
mouse_click(from_pos_x+260, from_pos_y+120)
time.sleep(1)
mouse_click(from_pos_x+300, from_pos_y+470)
time.sleep(1)

win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)

do_key_input("Hello,win32api!", clip_board_mode=False, key_sleep=0.2)
win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
do_key_input("你好啊,win32api!", clip_board_mode=True)

mouse_click(from_pos_x+30, from_pos_y+40)
time.sleep(1)
mouse_click(from_pos_x+30, from_pos_y+140)
time.sleep(1)
hwnd3 = wait_for_window("另存为", max_time=2)  # 最多等2秒钟
if hwnd3 is None:
    sys.exit(0)
mouse_click(from_pos_x+200, from_pos_y+370)
win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
win32api.keybd_event(65, 0, 0, 0)
win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
do_key_input('d:\win32api_test.txt', clip_board_mode=True)
mouse_click(from_pos_x+590, from_pos_y+450)
time.sleep(1)
hwnd4 = wait_for_window("确认另存为", max_time=2)  # 最多等2秒钟
if hwnd4 is not None:
    win32gui.SetWindowPos(hwnd4, win32con.HWND_TOPMOST, from_pos_x, from_pos_y, 200, 100, win32con.SWP_SHOWWINDOW)
    mouse_click(from_pos_x + 240, from_pos_y + 110)
    time.sleep(1)

mouse_click(from_pos_x+570, from_pos_y+10)