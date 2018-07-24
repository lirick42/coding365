# coding365 課後作業： (Python_LV02_wk01_hw01)

實作stack和circular queue 

------------------------- 
輸入說明: 
------------------------- 
先輸入要實作stack還是circular queue: 
1表示實作stack 
2表示實作circular queue 
接著輸入想要執行的功能: 
1表示新增整數數字到stack或circular queue 
2表示想要刪除stack或circular queue裡面的數字 
3表示印出目前stack或circular queue裡面的所有數字 

stack和circular queue的MAX為5 
如果沒有辦法新增數字到stack或circular queue則需顯示"FULL" 
如果stack或circular queue為空導致沒有辦法刪除數字，則需顯示"EMPTY" 

輸出說明: 
印出程式執行結果。 

--------------------------------------------------------------- 
input: 
1 
1 2 
1 6 
1 8 
1 5 
1 9 
1 7 

output: 
FULL 

input: 
1 
1 2 
1 6 
1 8 
1 5 
1 9 
2 
2 
2 
3 
output: 
2 6 

input: 
2 
1 2 
1 6 
1 8 
1 5 
1 9 
output: 
FULL 

input: 
2 
1 2 
1 6 
1 8 
1 5 
2 
2 
2 
1 3 
3 
output: 
5 3 

input: 
2 
1 2 
1 6 
1 8 
1 5 
2 
2 
2 
2 
2 
output: 
EMPTY 