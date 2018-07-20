# coding365 課後作業： (Python_hw102012_lv00_wk2_hw12)

求最大周長和面積 

寫一個 function 輸入 N 組矩形 XY 座標中的兩個點，輸出 N 組矩形中的最大的周長和最大的面積。 

程式中必須使用以下 function 定義，計算一個矩形的周長與面積。 

--------------------------------------- 
void compute(int x1, int y1, int x2, int y2, int *perimeter, int *area); 

第一個點 (x1, y1) 
第二個點 (x2, y2) 
計算周長結果 *perimeter 
計算面積結果 *area 

輸入幾組矩形的兩個點，輸入-1停止輸入。 
輸出最大的面積和最大的周長。 

------------------ 
輸入說明： 

分別輸入幾組矩形的兩個點， 
第一筆輸入第一個矩形兩個點，x1, y1, x2, y2， 

換行再輸入第一個矩形兩個點，直到輸入 -1 停止。 

輸出說明： 

輸出所有矩形中最大的面積和最大的周長。 

--------------------- 
輸入範例: 
-10 -10 20 60 
52 52 2 2 
85 8 5 38 
-1 

輸出範例: 
2500 
220