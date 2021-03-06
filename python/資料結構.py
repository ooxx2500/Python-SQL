# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:23:25 2020

@author: ASUS
"""


'''

1.串列:List(資料容器) 由一連串資料組成(等同於陣列)，可存放不同型態的資料，
      以中誇號前後誇住資料[]，可以建構為多維串列(一維,二維....)
  一維串列:串列資料取得:串列名稱[索引值(從0開始)]
         串列名稱[起始:終止]:起始列終止-1的元素 
    建立:[元素1,元素2......]元素建立後即有所引值，索引值從0開始
     
  len()函式:求串列的長度(元素個數)
  append(value):加入元素，將value加入串列尾端，元素可以為一般的資料(也可以是串列)
  extend(value):加入元素，但只能放入串列      
  insert(index,value):加入元素在指定的索引處        
  pop():移除串列最後一個元素，可以用變數取出來
  pop(index):移除串列指定所引值得元素，可以用變數取出來
  remove(value):移除第一個指定值
  count(value):求串列值出現的次數
  index(value):求串列值所在的索引位置，只顯示出現第一次的
  sort():串列排序，由小到大
  reverse():串列元素反轉
  sum():求串列元素總合
  max():求串列元素最大值
  min():求串列元素最小值
  in / not in判斷元素是否在或不在串列中
  + :連結串列
  * :複製串列
  
    
2.元祖(數組):
    建立:元祖名稱=(元素1,元素2....)，元素個數元素名稱不可以改變，其他與串列相同
        所以不能使用append(),insert()
 
    ----元祖VS串列-----
    串列功能比元強大
    元組比串列安全，不能更改
    元組執行數度快
    -----------------
    應用:串列與元祖互相轉換 
    元組轉串列 tuple1 = (1,2,3)  
             list1 = [tuple1]     
    串列轉元祖 list2 = [3,2,1]
             tuple2 = (list2)
      
    tuple 與串列LIST相似，不同如下
    1.tuple內元素值不可改變
    2.無法刪除個別元素、無法取代個別元素
    3.以小()建立元祖
    4.可以刪除整個數組
    5.del tuple
    6.max()
    7.min()
    8.tuple()
    9.list()
    10.lem()

3.集合:set 以大誇號{}建立，集合不會有重複資料
    add(x):將x加入集合  
    remove(x):將x資料移除 
    聯集:union(集合)        或是用 集合1 | 集合2
    交集:intersection(集合) 或是用 集合1 & 集合2
    差集:difference(集合)   或是用 集合1 - 集合2(集合1減掉和集合2相交的部分)
    ==:比較兩個集合是否相等
    =!:比較兩個集合是否不相等 
    
    

4.字典:dict 
    以大誇號{:}建立，資料鍵值(key)及值(value)組成 
    格式 {key:value , key2:value2......}   中間用冒號隔開
    字典元素無一定的順序排列(串列元素則依序排列)--記憶體位置
    字典取值得方式:字典名稱[key] 會出來value,字典以key為索引取得value
    Key值必須唯一，value可以重複
    如果加入重複的key不會出現錯誤，會以後面新增的覆蓋過去
    如果KEY不存在會產生錯誤，所以可以用get()，若無KEY則得到None
    
    3種建立方式
    字典名稱 = {key1:value1 , key2:value2.......}
    字典名稱 = dict([key1:value1],[key2:value2].......)
    字典名稱 = dict(key1=value2,key2=value2........)---此方法KEY不能是數字
    
    
    del 刪除資料 del 字典[key]
    clear() 刪除字典所有元素 字典名稱.clear()
    del 字典名稱  直接刪除整個字典
    keys()列出該字典所有的key值
    values()列出所有的Values值
    items()列出項目值
    tuple(dict1.items()) 不會出現原本的名稱
    copy()複製
    update()合併字典，若有相同的key值只取一個key(合併的那個欄位)
    get(key) 傳回值，如果無KEY不會產生錯誤
    setdefault(key,value) 若沒有Key建立一組key:value,若已經有KEY則回傳原本的值

'''
---------------------------------------------------------
#一維串列，串列資料取得:串列名稱[索引值(從0開始)]

list1 = []
list2 = [1,2,3,4,5]
list3 = ['apple','banana','orange']
list4 = [1,35,16,78,'pineapple']


list1.append(10)#尾端加入10
list1.append(20) #尾端加入20
list1.insert(1,30) #在位置1插入30
list1.append(40) #尾端加入40
list1.sort() #排序由小到大
list1.reverse() #反轉串列
30 in list1
80 not in list1
print(sum(list1),max(list1),min(list1),list1)
a=list2.pop() #丟掉尾端的元素用A取出
print(list2 , a)
b=list2.pop(1) #丟掉位置1的元素用B取出
print(list2,b)
list2.remove(3) #移除第一個3
print(list2)
list3.append('apple') #尾端加入apple
list3.count('apple')
list3.index('apple') #取出apple的位置
list3.index('banana') #取出banana的位置
list3.index('orange') #取出orange的位置


print(list1,list2)
list1+list2 #兩個串列相加
2*list2 #list2變兩倍

list1[-1] #取出list1最後的元素
list1[-3:-1] #取出list1 -3~-1的元素
list1[-4:4]

-------------------------------------------------
list3 = ['apple','banana','orange','kiwi'] #用迴圈印出串列
for i in range(len(list3)):
    print('list3[%d]=%s'  % (i,list3[i]))

--------------------------------------------------------------------

#樂透
import random

lotto = []   #建立空的串列
for i in range(6):  
    a = random.randint(1,49)#產生亂數1-49
    lotto.append(a)
print("樂透號碼是")
for i in range(len(lotto)):
    print(lotto[i],end=" ")

#練習數字不重複(老師版)
import random
lotto = []
checkNum = []

for i in range(0,50): #checknum加入50個0元素[0,0,0........,0,0,0,0]
    checkNum.append(0)
count = 1
while count <=6: #重複執行值到超過6次才停止
    randNum = random.randint(1,49)
    if checkNum[randNum] == 0: #隨機數是0才加入該串列
        lotto.append(randNum)
        count += 1
        checkNum[randNum] = 1 #並將該串列位置數值改為1
print("樂透號碼是: \n" , end ="")
for i in lotto:
    print(i,end=" ")  
print() 
         
#樂透不重複地2板(老師)
import random
lotto = []
n=1
while n <=6:
    randNum = random.randint(1,49)
    if randNum not in lotto:
        lotto.append(randNum)
        n+=1
print("樂透號碼是:\n" , end="")
for i in lotto:
    print("%2d" %i , end = " ")
print()

#樂透不重複地3板順便排序
import random
lotto = []
n=1
while n <=6:
    randNum = random.randint(1,49)
    if randNum not in lotto:
        lotto.append(randNum)
        n+=1
print("樂透號碼是:\n" , end="")
for i in lotto:
    print("%2d" %i , end = " ")
print()
lotto.sort()
print("號碼排序後:")
for i in lotto:
    print("%2d" % i, end=" ")
print()



   
#練習不重複(DIY板)    
import random
lotto = []  
while len(lotto)!=6:   #一值加到6格元素就停止
    a = random.randint(1,49)
    if a in lotto:     
        continue
    else:
        lotto.append(a)      
        
print("樂透號碼是")
for i in range(len(lotto)):
    print("%2d" % lotto[i],end=" ")
print()
lotto.sort()
print("排序後號碼是")
for i in lotto:
    print("%2d"%i ,end = " ")
print()

'''
二維串列:視為多個一維串列組成，如五位學生每位學生3科成績

'''
#五位學生每位學生3科成績
st=[[50,60,70],[50,80,90],[80,60,80],[70,60,80],[20,100,30]]

----------------------------------------------------------

#抓出來算總合

list5 = [[1,2,3],[4,5,6]]

total = 0
for i in range(len(list5)):
    for ii in range(len(list5[0])):
        total=total+list5[i][ii]
print("總和為%d" %total)









-----------------------------
#輸入二維元素數量後，隨機產生該數量的1-50數值

import random
row = eval(input("輸入隨機列數"))
column = eval(input("輸入隨機欄數"))
lis=[]
for i in range(row):
    lis.append([])  #建立二維串列 lis=[[],[].....]
    for j in range(column):
        lis[i].append(random.randint(1,50))     
print(lis)
print()
for i in range(len(lis)):
    for j in range(len(lis[0])):
        print("lis[%d][%d]=%2d" % (i,j, lis[i][j]),end=" " )
    print()


----------------------------------------------

#輸入二維元素數量後，隨機產生該數量的1-50數值 算出總合
#算行的總數
import random
rows = eval(input("輸入隨機列數"))
columns = eval(input("輸入隨機欄數"))
lis=[]
for i in range(rows):
    lis.append([])  #建立二維串列 lis=[[],[].....]
    for j in range(columns):
        lis[i].append(random.randint(1,50))     
print(lis)
print()
for column in range(len(lis[0])):
    total = 0
    for row in range(len(lis)):
        total +=lis[row][column]      
    print("第%d行的總和 = %d" %(column , total))
    
#算欄的總數 
import random
rows = eval(input("輸入隨機列數"))
columns = eval(input("輸入隨機欄數"))
lis=[]
for i in range(rows):
    lis.append([])  #建立二維串列 lis=[[],[].....]
    for j in range(columns):
        lis[i].append(random.randint(1,50))     
print(lis)
print()
for row in range(len(lis)):
    total = 0
    for column in range(len(lis[0])):
        total+=lis[row][column]
    print("第%d欄的總和 = %d" %(row , total))    
    
    
    
 '''
資料結構:
    
    元祖(數組):tuple 與串列LIST相似，不同如下
    1.tuple內元素值不可改變
    2.無法刪除個別元素、無法取代個別元素
    3.以小()建立元祖
    4.可以刪除整個數組
     
 '''   
    
tu1 = (1,2,3,4,5)
tu1
tu2 = ()    
tu3 = tuple([x for x in range(1,6)])  #中間為串列中誇號  
tu3    
tu4 = tuple('python')    
tu4    
tu1+=(6,7)
tu1[2]
tu1[3:6]
tup3=2*tu1    
tup3



tu1 = (1,2,3,4,5)

for i in range(len(tu1)):
    print(tu1[i])

del tu1
tu1
print(tu1)

'''
資料結構:
    集合:set 以大誇號{}建立，集合不會有重複資料
    add(x):將x加入集合  
    remove(x):將x資料移除 
    聯集:union(集合)        或是用 集合1 | 集合2
    交集:intersection(集合) 或是用 集合1 & 集合2
    差集:difference(集合)   或是用 集合1 - 集合2(集合1減掉和集合2相交的部分)
    ==:比較兩個集合是否相等
    =!:比較兩個集合是否不相等
'''
s1 ={1,2,3}
s2 = set()  #建立空集合 不能用S2 = {}
s3 = set([x for x in range(1,6)])
s3
s4 = set((1,2,3))
s4
s5 = set((1,1,2,2,3)) #集合的資料不能有重複
s5
s10= {1,3,6} 
s10.add(20) #將20加入到S10後面
s10
s10.remove(3) #將3移除
----------------------------------------
set20 = {1,6,8,10,20}
set25 = {1,3,8,10}
set20.union(set25)
set20|set25
set20&set25
set20-set25

'''
資料結構:
    字典:dict 以大誇號{:}建立，資料鍵值(key)及值(value)組成 
    格式 {key:value , key2:value2......}   中間用冒號隔開
    刪除資料 del 字典[key]
    keys()列出該字典所有的key值
    values()列出所有的Values值
    items()列出項目值
    tuple(dict1.items()) 不會出現原本的名稱
    copy()複製
    update()合併字典，若有相同的key值只取一個key(合併的那個欄位)
    
'''
dict1 = {'Taipei':'101' , 'paris':'Tour Eiffel' , 'London':'Big bean'  }

dict1
dict1['berlin'] = 'wall'  #所以值用中誇號
dict1
dict1['Taipei']


for key in dict1:     #只能抓到鍵KEY
    print("%s:%s" % (key,dict1[key]) )

del dict1['Taipei']   #刪除台北的資料

dict1.keys()
dict1.values()
dict1.items()
tuple(dict1.items())

----------------------------------------------------------
dict2 = {1:'red',2:'yello',3:'green'}
dict3 = {4:'blue', 1:'red222222'}
dict4 = dict2.copy()  #複製
dict4
dict4.update(dict3)  #合併
dict4

---------------------------------------------
#get()
fruit = {'蘋果':15 , '香蕉':10,'番茄':12}
print(fruit.get('蘋果'))
print(fruit.get('鳳梨'))

-----------------------------------------------
#字典找血型

dict1 = {'A':'內向穩重','B':'外向樂觀','D':'堅強自信','AB':'聰明自然'}
name = input("輸入血型")
blood = dict1.get(name)
if blood==None:
    print("沒有%s血型"%name)
else:
    print("%s血型的個性為%s" %(name, str(dict1[name])))

















-----------------------------------------------------------
題目:宣告一整數串列(大小為5 5個元素)
傳遞給output(aList)函式
函式由輸入初始化後
回傳給主程式並輸出該串列
再由主程式將該串列傳給max(aList)及min(aList)函式
輸出aList之最大值及最小值
(不可用系統內建函式)　



import random

a = [random.randint(1,100) for x in range(5)]

print(a)


def output(alist):
    maxnum = alist[0]
    minnum = alist[0]
    for i in alist:
        if i >= maxnum:
            maxnum = i
            
    for i in alist:
        if i <= minnum:
            minnum = i
    return print("最大值是:%2d 最小值是:%2d" %(maxnum, minnum) )
            
output(a)
--------------------------------------------------

dict1 = {"林美麗":85,"王大同":93,"李大年":67}
name = input("請輸入姓名")      
#name =input("請輸入姓名")
if name in dict1:
    print( name+"的成績為"+str(dict1[name]))
    
else:
    score = input("請輸入成績:")
    dict1[name]=score
    print('字典內容'+str(dict1))







