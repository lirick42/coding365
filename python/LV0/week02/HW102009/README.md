# coding365 課後作業： (Python_hw102009_lv00_wk2_hw09)

神奇寶貝進化計算器 

在pokemon go遊戲中，傳送一隻神奇寶貝給博士可以得到 1.5 公升進化藥水，每完成一隻神奇寶貝的進化也可以得到 1.5 公升進化藥水。 

現在玩家想要在最短時間內完成最多次的進化，請幫助玩家最多可以進化幾隻神奇寶貝 

已進化和未進化的神奇寶貝都可以被傳送走，傳送走該神奇寶貝即消失 

每隻神奇寶貝只能進化一次，已進化的神奇寶貝不能再進化，僅能留下來或被傳送，傳送一樣可以拿 1.5 公升進化藥水 

輸入說明 ： 

一次測試會輸入三個數字 
第一個數為神奇寶貝進化需要消耗的進化藥水 N (-100 < N < 0)，必須為負小數，顯示到小數點後一位，例如:-12.3或-99.0 
第二個數為玩家所擁有的進化藥水 C (0 ? C ? 30000)，必須為正小數，顯示到小數點後一位，例如:3255.6或553.0 
第三個數為玩家所擁有的神奇寶貝數量 W (0 ? W ? 10000)，必須為正整數，例如:5。 


不合法的輸入如下，遇到不合法輸入則輸出Error 
(1)當需輸入小數但小數格式輸入錯誤時，例如:1.-6或1.1.1 
(2)當需輸入正數，但使用者輸入負數時 
(3)當需輸入負數，但使用者輸入正數時 
(4)當需輸入小數，但使用者輸入的小數，小數點後超過一位，例如:-1.6667 
(5)當需輸入整數，但使用者輸入小數時 


輸出說明 ： 
輸出進化次數。 

--------------------- 

範例輸入1： 
-12.3 22.5 5 

範例輸出: 
2 

--------------------- 

範例輸入2： 
%56 22.5 5 

範例輸出: 
Error 

--------------------- 

範例輸入3： 
-12.3 -22.5 5 

範例輸出: 
Error 

--------------------- 

範例輸入1說明： 
1. 先進化1隻神奇寶貝，用掉 12.3 公升進化藥水，進化後再得1.5公升進化藥水，剩 11.7 公升進化藥水和 4 隻未進化神奇寶貝和 1 隻已進化神奇寶貝。 

2. 把 1 隻已進化神奇寶貝傳送給博士換取 1.5 公升進化藥水，剩 13.2 公升進化藥水和 4 隻未進化神奇寶貝。 

3. 再進化 1 隻神奇寶貝，得1.5公升進化藥水，最後剩 2.4 公升進化藥水及 3 隻未進化神奇寶貝和 1 隻已進化神奇寶貝。 

4. 因為剩下的 4 隻神奇寶貝即使傳送給博士，得到的進化藥水也不夠進化的量，所以總共只能進化2次。