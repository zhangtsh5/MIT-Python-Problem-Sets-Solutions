# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:36:02 2019

@author: zhangtieshan
"""

annual_salary=int(input("Enter the starting salary: "))
semi_annual_raise=0.07                 #涨薪比例
target=250000                          #存款目标金额

r=0.04                                  #年利率
inc=1+r/12                              #本金增加倍数
s=1+semi_annual_raise                       #每月工资增加倍数  
def func(x):
    money=annual_salary*(x/120000)           #每月存款金额,因为x放大了10000倍
    current_saving=money                     #一个月后存款
    i=2
    while i<37:
        temp=current_saving*inc
        if i%6==1:                          #每过6个月，工资增加
            money*=s
        current_saving=temp+money           #i月后拥有存款
        i=i+1
    return current_saving-target

left=0
right=10000

if func(right)<0:
    print("It is not possible to pay the down payment in three years.")
else:                                     #二分查找求最低rate
    counter=0
    while left<right:
            mid=int((left+right)/2)
            counter+=1                  #计算二分次数
            if func(mid)<0:
                left=mid+1
            if func(mid)>0:
                right=mid-1
    rate=left/10000                   
    print("Best savings rate: ",rate)
    print("Steps in bisection search: ",counter)

    
    
    



