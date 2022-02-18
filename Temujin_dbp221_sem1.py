#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Жагсаалтад 'python', 'php', 'java' гэсэн утгуудыг хадгал. Жагсаалт дахь байрлалыг ашиглан эдгээр утга бүрийг хэвлэ.
languages=['python', 'php', 'java']
for i in languages:
    print(i)


# In[5]:


#2. 10 гишүүн бүхий тоон жагсаалт үүсгэ. Жагсаалтын нийлбэрийг давталт ашиглан хэвлэ.
numbers=[7,3,4,6,7,8,4,3,10,9]
s=0
for i in numbers:
    s=s+i
print(s)


# In[37]:


#3. 5 гишүүн бүхий тоон жагсаалт үүсгэ. Жагсаалтын гишүүдийн үржвэрийг хэвлэх функц бич.Үр дүнг хэвлэ.
def urjver(a):
    b = 1
    for i in a:
        b = b * i
    return b

numbers=[7,8,4,3,11]
print(urjver(numbers))


# In[40]:


#4. Өгөгдсөн тоон жагсаалтын 3 дахь элементийг сүүлийн сүүлийн элементтэй үржүүлэн үр дүнг буцаадаг функц бич.
def urjverx(a):
    c=1
    for i in a:
        c=a[2]*a[-1]
    return c

numbers=[3,11,12,4,5,7,2]
print(urjverx(numbers))


# In[41]:


#5.Өгөгдсөн тоон жагсаалтаас хамгийн их болон хамгийн бага утгуудыг буцаах функц бич.Үр дүнг хэвлэ.
def maxim(a):
    x=max(a)
    return x
def minum(a):
    y=min(a)
    return y

numbers=[7,3,4,6,7,11,13,3,10,8]
print(maxim(numbers),minum(numbers))


# In[97]:


#6.Өгөгдсөн жагсаалтаас хоёроос дээш оронтой, эхний болон төгсгөлийн тэмдэгтүүд нь хоорондоо адилхан гишүүн хэд байгааг тоолох функц бич.
a=['abdba', 'abcd', '121']
s=0
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        s=s+1
print(s)


# In[45]:


#7.Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, хэвлэ
def dawhardsan(a):
    return list(dict.fromkeys(a))
mylist = dawhardsan(['aaaa', 'abcd', 122, 122, 'abcd'])
print(mylist) 


# In[57]:


#8.Жагсаалт хоосон эсэхийг шалгах функц бич. Үр дүнг хэвлэ.
def empty(a):
    if len(a):
        print('Хоосон биш')
    else:
        print('Хоосон')
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
empty(a)    


# In[74]:


#9.10 гишүүн бүхий жагсаалтын 4, 6, 8 дахь гишүүдийг устгаж, хэвлэ.
a=[100,200,300,400,500,600,700,800,900,1000]
del a[3:8:2]
print(a)


# In[75]:


#10.Тоон гишүүн бүхий tuple үүсгэ.
a=(33,14,55,18,29,98,9)


# In[76]:


#11.Tuple –д гишүүн нэмэх програм бич.
a=(33,14,55,18,29,98,9)
b=list(a)
b.append(2)
a=tuple(b)
print(a)


# In[77]:


#12.Tuple –ийн 2 дахь элемент болон араасаа 2 дахь элементийг хэвлэ.
a=(33,14,55,18,29,98,9)
b=list(a)
print(b[1],b[-2])


# In[78]:


#13.Tuple –д гараас оруулсан утга байгаа эсэхийг шалгах програм бич.
given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
char = input('Enter a character to find: ')
for ch in given_tuple:
    if ch == char:
        print('It is in the tuple')
        break
    else:
        print('It is not in the tuple')
        break


# In[16]:


#14.Өгөгдсөн Tuple –ийн бүх гишүүдийг давталт ашиглан хэвлэ.
given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
for ch in given_tuple:
    print(ch)


# In[20]:


#15. 2 төрлийн set үүсгэн хооронд нь нэгтгэх програм бич.
a={'a', 'b', 'c', 'd'}
b={'e', 'f', 'g', 'h'}
print(a.union(b))


# In[21]:


#16. 2 төрлийн set үүсгэн аль алинд байгаа утгыг олох програм бич.
a={'a', 'b', 'c', 'd'}
b={'e', 'a', 'c', 'h'}
print(a.intersection(b))


# In[22]:


#17. Өгөгдсөн set-ийн уртыг ол.
a={'a', 'b', 'c', 'd'}
print(len(a))


# In[24]:


#18.Өгөгдсөн set-ээс гараас оруулсан утгыг устга.
a={'a', 'b', 'c', 'e', 'f', 'g', 'h', 'd'}
given=input()
a.discard(given)
print(a)


# In[28]:


#19. Өгөгдсөн set-ийн бүх утгыг устга.
a={'a', 'b', 'c', 'e', 'f', 'g', 'h', 'd'}
a.clear()
print(a)


# In[33]:


#20. Өгөгдсөн set-ийг устга.
a={'a', 'b', 'c', 'e', 'f', 'g', 'h', 'd'}
del a


# In[79]:


#21.Key, value нь тоон утга бүхий dictionary үүсгэж өсөх болон буурахаар эрэмбэл.
dict1={
    '2':20,
    '3':30,
    '5':50,
    '4':40,
    '1':10}
a = sorted(dict1.items(), key=lambda x: x[1])    
print(a)


# In[80]:


#22.Өгөгдсөн key нь dictionary –д байгаа эсэхийг шалгах програм бич.
dicti={
    2:20,
    3:30,
    5:50,
    4:40,
    1:10}
x=int(input())
if x in dicti:
    print(x,' dict-д байна.')
else:
    print('Алга')


# In[104]:


#23. Өгөгдсөн value нь dictionary –д байгаа эсэхийг шалгах програм бич.
dict3 = { 
    '2':20,
    '3':30,
    '5':50,
    '4':40,
    '1':10 } 
x=int(input())
if x in dict3.values():
    print("Байна")
else:
    print("Алга")


# In[117]:


#24. For давталт ашиглан dictionary –ийн key, value –г хэвлэх програм бич.
dictx = { '2':20,
    '3':30,
    '5':50,
    '4':40,
    '1':10 } 
for i in dictx:
    print(i,dictx[i])


# In[116]:


#25.Хоёр dictionary үүсгэж хооронд нь нэгтгэ.
dicta= {
    '4':40,
    '1':10 } 
dictb = {
    'Model': '3', 
    'Year': 2021 } 
dicta.update(dictb)
print(dicta)


# In[106]:


#26. Dictionary –д байгаа value хооронд нь нэмэх програм бич. 
dicti = { '1':10,
    '2':20,
    '3':10,
    '4':30,
    '5':15,
    '6':25} 
sum = 0
for i in dict7:
    sum = sum + dicti[i]
print("Нийлбэр:",sum)


# In[ ]:




