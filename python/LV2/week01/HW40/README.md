# coding365 課後作業： (Python_LV02_wk01_hw07)

binary tree 

以data大小為依據，左子樹小於等於根，右子樹大於根，建立二元樹。 
//插入資料進二元樹 
(1)void Insert(); 
//中序巡訪印出：左中右 
(2)void Inorder(); 

--------------------- 
輸入說明： 

p function(2) 
i function(1) 
5 欲插入的數字 
p 
i 
6 
p 
i 
7 
p 
i 
3 
p 
i 
4 
p 
e 結束輸入 
------------------------------ 
輸出說明： 

p (印出): 
(1)沒有tree 印出 null 
(2)第一個插入的數字為 root 
(3)小於、等於 root 為左子樹 
(4)大於 root 為右子樹 
3 4 5 6 7 每個data中間有空白 

---------------------- 
Sample Input: 

p 
i 
5 
p 
i 
6 
p 
i 
7 
p 
i 
3 
p 
i 
4 
p 
i 
2 
p 
i 
6 
p 
e 

------------------- 
Sample Output: 

null 
5 
5 6 
5 6 7 
3 5 6 7 
3 4 5 6 7 
2 3 4 5 6 7 
2 3 4 5 6 6 7