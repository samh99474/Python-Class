"""
import path 參考網站:
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/575640/
在涉及到相對匯入時，package所對應的資料夾必須正確的被python直譯器視作package，而不是普通資料夾。
否則由於不被視作package，無法利用package之間的巢狀關係實現python中包的相對匯入。
資料夾被python直譯器視作package需要滿足兩個條件：

　　1、資料夾中必須有__init__.py檔案，該檔案可以為空，但必須存在該檔案。

　　2、不能作為頂層模組來執行該資料夾中的py檔案（即不能作為主函式的入口）。
"""
