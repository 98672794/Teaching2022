
請先[建立開發環境](./1%20建立開發環境.md)
並[安裝好windows開發工具](./2%20windows開發工具下載安裝.md)

-

# 寫 program 流程簡介

    在任意位置新建文字檔
    
    將副檔名轉為 .py
    
    用VScode打開

-

# [.py內容](https://raw.githubusercontent.com/98672794/Teaching2022/main/Start_2022PyT.py)



 





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

        #import _000

        OK = '_ATWImportThis = OK'
    except ImportError: # 如不能 import install
        ######################################################################
        ##################### import 寫在這裡同上一樣 #########################
        ######################################################################

        #os.system('pip install _000 ')
        #import _000

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









# 執行python程序

    點兩下.py文件即可


# debug

    # 寫在這裡
    內的代碼如錯誤會用 _Error 顯示

    
    


-

[4 python windows桌面應用程序](./4%20python%20windows桌面應用程序.md)

