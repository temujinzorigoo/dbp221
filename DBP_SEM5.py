#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1. 50-100 хүртэл тоон утга бүхий нэг хэмжээст массив (вектор) үүсгэ. 
import numpy as np
arr1=np.arange(50,101)
print(arr1)


# In[13]:


#2. Арван ширхэг 1, арван ширхэг 0, арван ширхэг 6 тоо бүхий нэг хэмжээст массивууд(вектор) үүсгэ.
arr2=np.zeros(10)
print(arr2+1)
print(arr2)
print(arr2+6)


# In[14]:


#3. 20-32 хүртэл тоон утга бүхий 3x4 хэмжээтэй массив үүсгэ
arr3=np.arange(20,32).reshape(3,4)
print(arr3)


# In[15]:


#4. Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив үүсгэ.
arr4=np.identity(3)
print(arr4)


# In[16]:


#5. Диагональ нь 1-5 хүртэл тоо, бусад нь 0 байх 5х5 хэмжээтэй массив үүсгэ.
arr5=np.zeros(25).reshape(5,5)
np.fill_diagonal(arr5, (1,2,3,4,5))
print(arr5)


# In[17]:


#6.2 хэмжээст массив үүсгэж элементүүдийн нийлбэр,багана,мөрийн нийлбэрүүдийг хэвлэ.
arr6=np.arange(10).reshape(2,5)
result1=arr6.sum(axis=0)
result2=arr6.sum(axis=1)
result3=np.sum(arr6)
print(result1)
print(result2)
print(result3)


# In[3]:


#7.Тоглогчдийн статистик цуглуулах.
Seasons = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
Players = ['KevinDurant','PaulGeorge','ChrisPaul','LaMarcusAldridge','LebronJames','JamesHarden','StephenCurry','GiannisAntetokounmpo']

#Salary

KevinDurant_salaries=[17548838,18773176,19997513,21971850,26540100,25000000,30000000,37199000,40108950,42018900]
PaulGeorge_salaries=[2574120,3282003,15800000,16900000,18100000,19300000,30560700,33005556,35450412,39344970]
ChrisPaul_salaries=[17779457,18668431,20068563,21468695,22868827,24268959,35654150,38506482,41358814,30800000]
LaMarcusAldridge_salaries=[13000000,14100000,15200000,19689000,20575005,21461010,22347015,26000000,17628340,2641619]
LebronJames_salaries=[17545000,19067500,20644400,22970500,30963450,33285709,35654150,37436858,39219566,41180544]
JamesHarden_salaries=[5820416,13668750,14693906,15719062,26540100,28299399,30570000,38199000,41254920,44310840]
StephenCurry_salaries=[3958742,9887642,10629213,11370786,12112359,34682550,37457154,40231758,43006362,45780966]
GiannisAntetokounmpo_salaries=[0,1792560,1873200,1953960,2995420,22471911,24157304,25842697,27528088,39344900]
Salary=np.array([LebronJames_salaries,JamesHarden_salaries,StephenCurry_salaries,GiannisAntetokounmpo_salaries,KevinDurant_salaries,PaulGeorge_salaries,ChrisPaul_salaries,LaMarcusAldridge_salaries])

#Games

KevinDurant_games=[ 81,81,27,72,62,68,78,0,35,39]
PaulGeorge_games=[79,80,6,81,75,79,77,48,54,26]
ChrisPaul_games=[ 70,62,82,74,61,58,58,70,70,58]
LaMarcusAldridge_games=[74,69,71,74,72,75,81,53,26,45]
LebronJames_games=[76,77,69,76,74,82,55,67,45,47]
JamesHarden_games=[78,73,81,82,81,72,78,68,44,49]
StephenCurry_games=[78,78,80,79,79,51,69,5,63,60]
GiannisAntetokounmpo_games=[0,77,81,80,80,75,72,63,61,56]
Games=np.array([LebronJames_games,JamesHarden_games,StephenCurry_games,GiannisAntetokounmpo_games,KevinDurant_games,PaulGeorge_games,ChrisPaul_games,LaMarcusAldridge_games])

#Points

KevinDurant_points=[2280,2593,686,2029,1555,1792,2027,0,943,1135]
PaulGeorge_points=[1377,1737,53,1874,1775,1734,2159,1033,1259,641]
ChrisPaul_points=[1186,1185,1564,1446,1104,1081,906,1232,1149,866]
LaMarcusAldridge_points=[1560,1603,1661,1331,1243,1735,1727,1001,352,607]
LebronJames_points=[2036,2089,1743,1920,1954,2251,1505,1698,1126,1376]
JamesHarden_points=[2023,1851,2217,2376,2356,2191,2818,2335,1083,1113]
StephenCurry_points=[1786,1873,1900,2375,1999,1346,1881,104,2015,1538]
GiannisAntetokounmpo_points=[0,525,1030,1350,1832,2014,1994,1857,1717,1661]
Points=np.array([LebronJames_points, JamesHarden_points, StephenCurry_points, GiannisAntetokounmpo_points, KevinDurant_points, PaulGeorge_points, ChrisPaul_points, LaMarcusAldridge_points])


# In[10]:


#Мөрүүдийн нийлбэр
print('Тоглогч тус бүрийн 10 жил авсан нийт авсан цалин', Salary.sum(axis=1))
print('Тоглогч тус бүрийн 10 жил авсан нийт авсан оноо',Points.sum(axis=1))
print('Тоглогч тус бүрийн 10 жил тоглосон нийт тоглолт.',Games.sum(axis=1))


# In[9]:


#Багануудын нийлбэр
print('Улирал бүрийн сонгосон тоглогчдийн нийт цалин', Salary.sum(axis=0))
print('Улирал бүрийн сонгосон тоглогчдийн авсан нийт оноо',Points.sum(axis=0))
print('Улирал бүрийн сонгосон тоглогчдийн тоглосон тоглолтын нийт тоо.',Games.sum(axis=0))


# In[ ]:




