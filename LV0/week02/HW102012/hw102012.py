max_a = 0
max_b = 0
while(True):
    n = [int(i) for i in input().split(" ")]
    if(n[0]==-1):
        print(max_b) 
        print(max_a)
        break
    else:
        x = abs(n[0]-n[2])       
        y = abs(n[1]-n[3])         
        Perimeter = 2*(x + y)     
        a = x * y
        if(Perimeter>max_a):        
            max_a = Perimeter
        if(a>max_b):
            max_b = a