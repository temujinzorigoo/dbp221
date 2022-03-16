#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг мөр бүрд хэвлэх функц бич. 
def od(n):
    a=1
    while a<n+1:
        print('*'*a)
        a+=1
od(int(input()))


# In[6]:


#2.
def od_list(n):
    a=1
    while a<n+1:
        print(['*'*a])
        a+=1
od_list(int(input()))


# In[9]:


#3.
def max_min(students):
    a= max(students, key=students.get)
    b= min(students, key=students.get)
    return a,b
students = {'Bat': 434,
            'Oyun': 997,
            'Dulam': 219,
            'Suren':192}
max_min(students)


# In[19]:


#4.np.arange(1-1000) массив үүсгэ. Тухайн массиваас 3 эсвэл 7 –д хуваагдах тоонуудын нийлбэрийг ол.
import numpy as np
a=np.arange(1000)
b=0
for i in a:
    if i%3==0 or i%7==0:
        b=b+i
print(b)


# In[ ]:




