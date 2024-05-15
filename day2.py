#list =[25,41,3,14,2.3,'hello',True]
#print(list[1:3])
# to change any value directly do this

#list[1]=500
#print(list)
#print(len(list)) #length of the list


#list.append(100)#to add one more item at last
#print(list)

#list.pop()
#print(list) #to remove last item 

#list.insert(1,'jecrc')
#print(list) #to insert any item in any place

#print(list[6][-1])
# to print o from hello
#list=[25,41,63,25.6,[100,200,300]]
#print(list[4][1]) #to get 200 from list in the list

#list[4][1]=1000#to replace 200 by 1000
#print(list)

#tuple = to store multiple items 
#it uses paranthesis()
#tpl =(10,20,30,40)
#print(tpl)
#print(type(tpl))

#lets enter multiple type of data in tuple
#tpl=(10,20,30,23.7,'ret',True)
#print(tpl)
#print(tpl[2])



#tpl[2]=60 #it is enble tp replace
#print(tpl)# it tells that agr ek baar tuple bna dya toh change nhi kr skte this is called immutable
# this is the only difference bt tuple and list

#ques= make tuple with only one item
#ans=
#college=('jecrc',)
#print(type(college)) #only if agr coma lagaye tohi yh isse tuple lega wrna output string aayega

#college ="ghar","tree","car"
#print(type(college)) # bina ()bhi tuple hi aayega kukyuki tuple k liye ()jaruri nhi h 
# college="jecrc",(this is also tuple)


#to remove any item from any place
#list =[12,14,15,45,62]
#list.remove(14)
#print(list)

# different types of concepts
#name="ana"
#print(name*2)

#name="jecrc"
#sur="foundation"
#print(name+sur)

# string aur no. ek saath pehle jese add nhi ho skte h 
#name="ana"
#sur=100
#print(name+sur)


# to print tuple multiple times
#tpl=(10,20,30)
#print(tpl*2)


# check this in list
#list=[1,23,34,4,]
#print(list*2)
# this process is called replication

#list1=[1,2,3,4,]
#list2=[5,6,7,8]
#list1.append(list2)
#print(list1)
#list1.extend(list2)
#print(list1)

#DICTIONARY
# isme hume key and values k form m store honge
dt = {"name":"rohit","branch":"it"}
#print(type(dt))
#print(dt["name"])# to access any value then write its key
#print(dt.keys())# to see all the keys of the dictionary
#print(dt.values())

# we can give any datatype of key and values
#dt = {0:"rohit",1:"rahul"}
#print(dt)

#to access the values of key if is list
#cls={"name":["a","b","c","d"],"marks":[1,2,3,4]}
#print(cls["name"])
