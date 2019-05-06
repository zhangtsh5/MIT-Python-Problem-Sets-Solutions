# -*- coding: utf-8 -*-

annual_salary=int(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save,as a decimal: "))
total_cost=int(input("Enter the cost of your dream home: "))

money=(annual_salary*portion_saved)/12  #每月存款金额
target=total_cost*0.25                  #存款目标金额

current_saving=money                    #一个月后存款
r=0.04
s=1+r/12                                #每月存款增加倍数
i=2                                     #从第2个月开始赚利息  
while 1>0:
    temp=current_saving*s
    current_saving=temp+money           #i月后拥有存款
    if current_saving<target:           #没存够，继续存
        i=i+1
        continue
    else:                               #存够了，跳出循环
        months=i
        break
print("Number of months: ",months)      #输出结果

