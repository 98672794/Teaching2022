
請先[建立開發環境](./1%20建立開發環境.md)
並[安裝好windows開發工具](./2%20windows開發工具下載安裝.md)

-

# 寫 program 流程簡介

    在任意位置新建文字檔
    
    將副檔名轉為 .py
    
    用VScode打開

-

# .py內容

    # -*- coding: UTF-8 -*-
    #!/usr/bin/python

    import os
    from copy import Error

    #######################################################################
    ##################################################### Start = 開始 
    def Start2022():

        try:
            print('寫在這裡')
            NowOK = 'Start2022() = OK'

            ##################### 寫在這裡 ################################




















            ##################### /寫在這裡 ################################


        except Exception as e:
            for 行 in _Error(e):
                print(行)
            NowOK = 'Start2022() = Error'
        # /
        return NowOK


    def _Error(e):
        異常內容 = [
            '========= _Error ===========',
            e,      # Error說明,
            e.__traceback__.tb_frame.f_globals["__file__"], # 位置
            e.__traceback__.tb_lineno,  # 行
            '========= \ ==========='
        ]
        return 異常內容


    if __name__ == "__main__":
        print(Start2022())
    
    


-

    import 函式庫
        os
        database
        Google docs
    debug
