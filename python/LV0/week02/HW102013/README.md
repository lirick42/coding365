# coding365 課後作業： (Python_hw102013_lv00_wk2_hw13)

分數計算 
(此題不使用陣列) 

程式碼必須使用以下 function 定義，計算兩個分數的相加。 

void add(int n1, int d1, int n2, int d2, int *numerator, int *denominator); 

n1: 第一個數的分子 
n1: 第一個數的分母 
n1: 第二個數的分子 
n1: 第二個數的分母 
*numerator: 相加結果的分子 
*deniminator: 相加結果的分母 

程式碼必須使用以下 function 定義，計算兩個分數的相乘。 

void mul(); 

int multiply(int n1, int d1, int n2, int d2, int *numerator, int *denominator); 

n1: 第一個數的分子 
n1: 第一個數的分母 
n1: 第二個數的分子 
n1: 第二個數的分母 
*numerator: 相乘結果的分子 
*deniminator: 相乘結果的分母 

-------------------- 

輸入說明: 

輸入二行，每一行代表一個分數 

---------------- 
輸出說明: 

輸出分數相加結果 
輸出分數相乘結果 

若有輸入分數的分母或分子為0，則輸出ERROR。 
若分數大於1，則分數部分要加括號。 
若為負數，負號在最前面。 

---------------- 
範例輸入: 
1/2 
2/3 

範例輸出: 
1(1/6) 
1/3 

---------------- 
範例輸入: 
0/2 
2/3 

範例輸出: 
ERROR 
ERROR