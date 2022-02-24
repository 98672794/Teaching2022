
# 如何將 Python 連接到 Google 表格


## [在Google API Console新增一個專案](https://console.developers.google.com/) <-- 點網址入 新增專案

    寫地區資料
    按選取專案
    新增專案 名隨意
    確定
    等 選取專案 轉為你專案名即OK
    
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/zcJe5Isfhng/0.jpg)](https://www.youtube.com/watch?v=zcJe5Isfhng)

-

## 搜尋並啟用 Google Sheets API

    在 Google Cloud Platform 的搜尋中
    Google Sheets API
    啟用

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/KObOPFWQoPk/0.jpg)](https://www.youtube.com/watch?v=KObOPFWQoPk)

-

## 建立憑證
    再次在 Google Cloud Platform 的搜尋中
    Google Sheets API    
    按 管理
    憑證
    建立憑證


## 服務帳戶
    服務帳戶名稱 (隨意,存取權授時顯示)
    服務帳戶說明 (隨意)
    建立並繼續
    擁有者
    完成

## Google金鑰
    憑證
    點剛建的服務帳戶的電子郵件
    金鑰
    新增金鑰
    建立新的金鑰
    JSON
    另存新檔 在您的工作文件夾中


-

    金鑰可用來存取您的雲端資源，因此請妥善保管
    
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/IWnQa3J5VRI/0.jpg)](https://www.youtube.com/watch?v=IWnQa3J5VRI)

-

## 授權Google Sheet給服務帳戶

  [Google Cloud Platform](https://console.developers.google.com/) 點 API 和服務
  
    憑證
    複製 剛建的服務帳戶的電子郵件 備用

    打開你要操作的Google試算表
    共用
    
    新增使用者中貼上
    剛建的服務帳戶的電子郵件
    選權限
    傳送

    複製 Google Sheet(試算表)網址 備用
    

[![授權Google Sheet給服務帳戶](https://img.youtube.com/vi/m0t8cA5MTbw/0.jpg)](https://www.youtube.com/watch?v=m0t8cA5MTbw)

-


## [Python連接到Google表格.py]()




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












---
---
---
--- 

[啟用Google Sheet API](https://www.learncodewithmike.com/2020/08/python-write-to-google-sheet.html)|[在 Google Sheet 裡面，授權給剛剛在 GCP 申請的服務帳號 ID](https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/)|
