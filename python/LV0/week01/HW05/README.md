# 測試案例(Test Case)資料： (Python_hw05)

>請輸入五個數字，分別計算出平均數、變異數、標準差， 
並精確到小數點後第二位(註，之後的小數捨去)。 


***平均數參考公式***

	μ=Σ(Xi)/N  
***變異數參考公式*** 

	Σ(Xi-μ)^2/N  
***標準差參考公式*** 

	(Σ(Xi-μ)^2/N)^(0.5) 


例如：

		1  
        2  
        8  
        9  
        10  

平均值：

		6.00 (1+2+8+9+10)/5.0 = 6.00  
變異數：

        14.00 Σ(Xi-μ)^2 =  
        (1-6)^2+(2-6)^2+(8-6)^2+(9-6)^2+(10-6)^2 =  
        25+16+4+9+16= 70  
        700./5.0= 14.00  

標準差：

		14^(0.5) = 3.74165  
		取兩位小數 = 3.74 


輸入說明 
---------------- 
- 輸入五個整數 


輸出說明 
--------------- 


- 平均值
- 變異數  
- 標準差  

輸出到 
**小數點第二位**
測試案例 (Test Case) 資料：

**input**

        1  
        2  
        8  
        9  
        10  
        
**output**

        6.00  
        14.00  
        3.74  