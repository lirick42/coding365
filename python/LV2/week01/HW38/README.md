# coding365 課後作業： (Python_LV２_wk01_hw05)

同學要選老師做專題 (project)， 
N 位學生 (N student)，M 位老師 (M teacher) ， 
配對方式，優先根據學生填寫志願， 
如有相沖突，則考慮老師志願序。 

測試案例一： 
學生有4位分別為W、X、Y、Z 
老師有4位分別為A、B、C、D 
學生志願序： 
W：A、B、C、D 
X：A、C、B、D 
Y：D、B、C、A 
Z：B、C、A、D 
老師志願序： 
A：W、X、Y、Z 
B：X、W、Y、Z 
C：Y、Z、W、X 
D：X、W、Z、Y 
結果： 
W->A 
X->C 
Y->D 
Z->B 


測試案例二： 
學生志願序： 
W：A、B、C、D 
X：A、C、B、D 
Y：D、B、C、A 
Z：B、C、A、D 


老師志願序： 
A：X、W、Y、Z 
B：X、W、Y、Z 
C：Y、Z、W、X 
D：X、W、Z、Y 
結果： 
W->C 
X->A 
Y->D 
Z->B 


範例輸入 
A,B,C,D 
A,C,B,D 
D,B,C,A 
B,C,A,D 
W,X,Y,Z 
X,W,Y,Z 
Y,Z,W,X 
X,W,Z,Y 
範例輸出 
W->A 
X->C 
Y->D 
Z->B 