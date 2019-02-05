my_list=[1,'a',3.5,4,'d','g',6.8,9]
intlist=[x for x in my_list if isinstance(x,int)]
floatlist=[x for x in my_list if isinstance(x,float)]
stlist=[x for x in my_list if isinstance(x,str)]
print(intlist)
print(floatlist)
print(stlist)

