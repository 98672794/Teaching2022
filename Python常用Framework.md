
# 什麼是 Python 框架？

    Python Web 框架是一組模塊或包，可幫助開發人員用 Python 編程語言編寫 Web 應用程序。
    當他們選擇 Python 進行快速開發時，他們不必擔心使用低級事實，如多協議、線程管理或套接字。
    框架使基本解決方案的性能自動化，為開發人員提供了專注於網站而不是一般常規流程的適應性。
    
    Web 框架為網站開發人員、Web 設計人員、系統管理員和 Linux 操作員提供了開發結構的自由，
    方法是為應用程序結構提供快速、一致且易於維護的默認模型。
    
    由於同時進行命令行 (CL)處理和強類型化，這些 Web 框架還減少了編碼時間並使開發人員更加專注。
    Python 後端框架具有更高的源順序抽象和元編程潛力，可以開發大型和復雜的代碼系統，
    並具有用於獨特功能的各種庫。


# python常用框架及第三方庫



## 一、Web框架

1.[Django](https://www.djangoproject.com/):

        開源web開發框架，它鼓勵快速開發，並遵循MVC設計，比較龐大，開發週期短。 
        Django的文檔最完善、市場佔有率最高、招聘職位最多。
        全套的解決方案，Django象Rails一樣，提供全套的解決方案（full-stack framework   batteries included），
        基本要什麼有什麼（比如：cache、session、feed、orm、geo、auth），而且全部Django自己造，開發網 站應手的工具Django基本都給你做好了，
        因此開發效率是不用說的，出了問題也算好找，不在你的代碼裡就在Django的源碼裡。

2.[web.py](https://webpy.org/): 

        輕量級Web框架，雖然簡單但是功能強大。

3.[Tornado](https://www.tornadoweb.org/en/stable/):

        Web服務器框架。 Tornado即是一個Web server，同時又是一個類web.py的micro-framework，作為框架，
        Tornado的思想主要來源於Web.py，沒有好的ORM，沒有session支持(雖然官方做法是用cookie代替)，WSGI支持不完整。
        但好處就是它用非阻塞的事件驅動開發，性能不錯。
        並且自帶WEB服務器，拿來學習一個非阻塞方式WEB服務器工作原理很適合。
        因為不用再去讀nginx源碼了。

4.[Zope](https://www.zope.dev/): 

    開源的Web應用服務器。

5.ActiveGrid: 

    企業級的Web2.0解決方案。

6.Karrigell: 

    簡單的Web框架，自身包含了Web服務，py腳本引擎和純python的數據庫PyDBLite。

7.CherryPy: 

    基於Python的Web應用程序開發框架。

8.Pylons: 

    基於Python的一個極其高效和可靠的Web開發框架。

9.TurboGears: 

    基於Python的MVC風格的Web應用程序框架。

10.Twisted: 

    流行的網絡編程庫，大型Web框架。

 11.Quixote:
 
    Web開發框架。

 

## 二、科學計算

1.Matplotlib: 

    用Python實現的類matlab的第三方庫，用以繪製一些高質量的數學二維圖形。

2.Scipy: 

    基於Python的matlab實現，旨在實現matlab的所有功能。

3.Numpy: 

    基於Python的科學計算第三方庫，提供了許多高級的數值編程工具，如：矩陣數據類型、矢量處理，線性代數，傅立葉變換，以及精密的運算庫。
    專為進行嚴格的數字處理而產生。



## 三、網頁爬蟲框架

scrapy: 

    Python開發的一個快速,高層次的屏幕抓取和web抓取框架，用於抓取web站點並從頁面中提取結構化的數據。 
    Scrapy用途廣泛，可以用於數據挖掘、監測和自動化測試。 Scrapy吸引人的地方在於它是一個框架，任何人都可以根據需求方便的修改。
    它也提供了多種類型爬蟲的基類，如BaseSpider、sitemap爬蟲等，最新版本又提供了web2.0爬蟲的支持。
    是一個為遍歷爬行網站、分解獲取數據而設計的應用程序框架，它可以應用在廣泛領域：數據挖掘、信息處理和或者歷史片（歷史記錄）打包等等。
 

## 四、分佈式網絡框架

Twisted: 

    使用Python編寫，強壯的、面向對象的解釋性語言。 
    Python使它的愛好者充滿熱情。使用Python編程是一種樂趣，易於編寫、易於閱讀、易於運行。
    因為Python是跨平台的，所以可以運行Twisted程序在Linux、Windows、Unix和MAC等等系統上。
    Twisted包括大量的功能。 Email、WEB、news、chat、DNS、SSH、Telnet、RPC、數據庫存取或者更多。

 

## 五、遊戲框架

Pygame: 

    基於Python的多媒體開發和遊戲軟件開發模塊。
    跨平台 Python模塊，專為電子遊戲設計。包含圖像、聲音。建立在SDL基礎上，允許實時電子遊戲研發而無需被低級語言（如機器語言和彙編語言）束縛。
    基於這樣一個設想，所有需要的遊戲功能和理念都（主要是圖像方面）都完全簡化為遊戲邏輯本身，所有的資源結構都可以由高級語言提供，如Python。

 

## 六、GUI

1.Tkinter: 

    Python下標準的界面編程包，因此不算是第三方庫了。

2.PyGtk: 

    基於Python的GUI程序開發GTK 庫。

3.PyQt: 

    用於Python的QT開發庫。

4.WxPython: 

    Python下的GUI編程框架，與MFC的架構相似。

 

## 七、其他

1.BeautifulSoup: 

    基於Python的HTML/XML解析器，簡單易用。

2.MySQLdb: 

    用於連接MySQL數據庫。

3.Py2exe: 

    將python腳本轉換為windows上可以獨立運行的可執行程序。

4.pefile: 

    Windows PE文件解析器。

5.PIL:

    基於Python的圖像處理庫，功能強大，對圖形文件的格式支持廣泛。

6.cElementTree: 

    高性能XML解析庫，Py2.5應該已經包含了該模塊，因此不算一個第三方庫了。


