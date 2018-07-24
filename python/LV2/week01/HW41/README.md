# coding365 課後作業： (Python_LV02_wk01_hw08)

Depth-first search for Binary Tree 

//s為樹的敘述，第一個字元為Root 
//(1)例如ACBE，則Root為A，left為C，mid為B，right為E 
//(2.1)若先輸入DE，則Root為D，left為E 
//(2.2)再輸入DF，則此時Root為D，left為E，mid為F 
(1)void BuildTree(); 
//利用Depth-first search，尋訪規則為Root先拜訪，再由children中字元最小的開始尋訪 
(2)void DFS(); 

--------------------- 
輸入說明： 

i, 樹的敘述: function(1) 
p: function(2) 
e: 程式結束 

輸出說明： 

p (印出): 
(1)沒有tree 印出 null 
(2)每個data中間沒空白 
--------------------- 
Sample Input: 
p 
i 
ACBE 
i 
CD 
i 
DH 
i 
EF 
p 
i 
HJ 
i 
HG 
i 
GI 
p 
e 

Sample Output: 
null 
ABCDHEF 
ABCDHGIJEF
