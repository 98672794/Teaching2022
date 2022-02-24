



##################### Start_2022PyT ################################
'''
注釋
'''
# 注釋


# .py必要
# -*- coding: UTF-8 -*-
#!/usr/bin/python


# 引用庫
import os
from copy import Error
try:

    ######################################################################
    ##################### import 寫在這裡 ################################
    ######################################################################

    # Python 連接到 Google 表格
    import pygsheets    # import 這次會使用到的 pygsheets庫

    OK = '_ATWImportThis = OK'
except ImportError:     # 如不能 import , install pygsheets庫
    ######################################################################
    ##################### import 寫在這裡同上一樣 #########################
    ######################################################################
    os.system('pip install pygsheets')  # install pygsheets庫
    import pygsheets

    OK = '_ATWImportThis = Error'


# Start = 加內容在這 
def Start2022():
    # try = 嚐試執行以下代碼, 如錯誤執行except
    try:
        print('寫在這裡')
        NowOK = 'Start2022() = OK'
        ######################################################################
        ####################### Code 寫在這裡 ################################
        ######################################################################

        # Python 連接到 Google 表格 
        Your金鑰json = 'key.json'   # 轉成您的
        YourGoogleSheetUrl = 'https://docs.google.com/spreadsheets/d/134Njkg1FaTOjVPxq_clDwKEK1_nPIPVrMpAPfcPJldU/' # 轉成您的

        gc = pygsheets.authorize(service_file=Your金鑰json)     # gc 這邊是告訴 Python 我們的授權金鑰 json 放置的位子
        sht = gc.open_by_url(YourGoogleSheetUrl)        # 利用 Python 開啟 GoogleSheet
        print('取得此GoogleSheet內的工作表')
        print(sht.worksheets())     # 取得此GoogleSheet內的工作表


    # 返回 _Error function 的內容
    except Exception as e:
        for 行 in _Error(e):
            print(行)
        NowOK = 'Start2022() = Error'
    # 返回 NowOK
    return NowOK



# 錯誤時顯示文件位置及行數
def _Error(e):
    異常內容 = [
        '========= _Error ===========',
        e,      # Error說明,
        e.__traceback__.tb_frame.f_globals["__file__"], # 位置
        e.__traceback__.tb_lineno,  # 行
        '========= \ ==========='
    ]
    return 異常內容


'''
程式入口 = if __name__ == "__main__":

    py文件有2個用法

    1=直接打開

    2=引用(import)

    使用程式入口,當直接打開便會執行程式入口內的內容

    主要目的是引用時不用執行到無用的程式碼
'''
if __name__ == "__main__":
    print(Start2022())
    os.system("pause") 
    
##################### / Start_2022PyT ################################




