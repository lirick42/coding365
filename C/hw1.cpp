#include <stdio.h>    
#include <stdlib.h>    

int main()    
{    
  char name;     
  int id,total,average;    
  double  chinese, compscience, programming,avg,to,avgint;     
  scanf("%c ",&name);      
  scanf("%d",&id);    
  scanf("%lf",&chinese);    
 scanf("%lf",&compscience);    
  scanf("%lf", &programming);    
  to = (programming + chinese + compscience);  
  total=to;    
  to=to/3;  
  avgint=floor(to);  
  if(to-avgint>0.5) avg=ceil(to);    
  else avg=to;  
  average=avg;  
           printf("Name:%c\n", name);    
           printf("Id:%d\n", id);    
           printf("Total:%d\n", total);    
           printf("Average:%d\n", average);    
  system("PAUSE");      
  return average;    
} 