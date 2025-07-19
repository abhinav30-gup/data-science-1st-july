# print("hello hii kase ho")
# a = "hello"
# num = 10
# 2= 2 not allowed
Age = 22
age = 24
print(Age)
print(age)
# break =22
# print =22
# print(print)


### string ......
name= "abhinav "
print(name)
print("my name is" ,name)
print("name dtypes:-",type(name))
print("len of name:- ", len(name))

### indexing ......
print(name[0])
print(name[2])
print (name[len(name)-1])
name="abhinav"
print(name[::-1])
print(name[::-2])
print(name[::-3])


### slicing in python ......
name="abhinav"
print(name[0:4])

# reverse in slicing .....
name = "abhinav"
print(name[0:4][::-1])
 
### operation .......
name ="abhinav"
last = "gupta"
upper_case = name.upper() ### upper function ka use upper case ke liye karte hai
print(upper_case)

lower_case = last.lower() ### lower function ka use lower case ke liye karte hai
print(lower_case)

print(name.count("a"))
name= "abhinav"
last= "gupta"
print(name.title())
print(name.capitalize())
print(name+" "+last) ## used to add space in string



# >>>>>>>>>>>>>.list.>>>>>>>>>>>>
# array or list>>>>>>>
# mutable
# duplicate values
# heterogeneous
# order
# array  >>>>>> list se greater hoti h 

lst= [1,2,2,3,4,5,6, 2.3,] ###>>>>>>>>>>>>>>list
# homogeneous
print("my first list:-" ,lst)
print("len of lst:-", len(lst))
print("type of list:-",type(lst))

print(lst[0])
print(lst[5])

print(lst[0:5])
lst.pop()
print(lst)

lst.append(100) ### last m agr kuch add krna ho
print(lst)

lst.insert(0,1000)### kisi specific jgh pe dalna ho to
print(lst)

copy_lst= lst.copy()
print(copy_lst) ### kisi list ko ek jgh se dushri jgh copy krte h
lst.reverse()
print(lst)
lst.remove(2)### agr kisi function ko remove krna ho
print(lst)

lst.sort() ### agr list sort krna ho
print(lst)

print(lst.count(4))### agr kisi perticular element ko count krna h 
print(lst)



# ...
# task
# make a list
# create a sub list inside that 
# now you have to access the element inside sublist
# ...
lst= [1,2,3,4,[5,6],7]
print(lst[4][0])


# >>>>>>>>>>>>>>>tuple<<<<<<<<<<<<
tpl=(1,2,3,5,585,5,"abhinav", 2.5)
print("my first tuple:-",tpl)
print("len of tuple:-",len(tpl))
print("type of tuple:-",type(tpl))

# indexing and slicing with tuple >>>>>
print(tpl[0])
print(tpl[2])
print(tpl[0:6])

a = 1,3,43,43,55,53,768,8 # by default tuple hi lega without paranthesis
print(a)
print(type(a))
print(len(a))
 
# tuple unpacking
a,b,c =( 1,2,3)
print(a)
print(b)
print(c)

a,b,c=1,2,3
print(a)
print(b)
print(c)

tpl = (1,2,3,4,5,6,7)
print("max of the tuple is ", max(tpl))
print("min of the tuple is ", min(tpl))
print("sum of the tuple is ", sum(tpl))

# # >>>>>>>>>>>>>dictionary<<<<<<<<<<<<
my_dict={
    "name":"abhinav",### name, class, roll number and address>>>>>>keys
    "class":"3rd year", ### abhinav, 3rd year , 23EJCIT005 ,jaipur >>>>>> values
    "roll number":"23EJCIT005",
    "address":"jaipur"  ###>>>> "name":"abhinav"item
}
print("my first dict:-",my_dict)
print("len of dict:-" ,len(my_dict))
print("type of dict:-", type(my_dict))
print(my_dict['name'])
print(my_dict['class'])
print(my_dict['roll number'])
print(my_dict['address'])
my_dict['address']="new jaipur"
print(my_dict)

my_dict['branch']="cse"
print(my_dict)


# task1 >>>>> using update function you need to update dictionary
my_dict={
    "name":"abhinav",
    "class":"3rd year",
"roll number":"23EJCIT005",
"address":"jaipur"
}
my_dict_2={
    "class":"2nd year",
    "branch":"IT"
}

my_dict.update(my_dict_2)
print(my_dict)

# task2 >>>>> using get function at least give 5 or using []square

my_dict={
    "name":"abhinav",
    "age":"20"
}
print(my_dict.get("name"))
print(my_dict.get("age"))

print(my_dict["name"])
print(my_dict["age"])


print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

copy_dict = my_dict.copy()
print(copy_dict)

my_dict.clear()
print(my_dict)

# a= input("enter a number")
# b= input ("enter second number")
# print(a*b)
# print(type(a))

# type casting

a= int(input("enter a number"))
b= int(input ("enter second number"))
print(a*b)

lst= [1,2,3,45,7,98]
print("this is my list:-", lst)
print("type of list:-", type(lst))
tpl =tuple(lst)
print("this is my tuple:-",tpl)
print("type of tuple:-", type(tpl))


# >>>>>>>>>>>>>>sets<<<<<<<<<<<<

my_set ={1,34,3,2,57,53,"abhinav"}
print("this is my set:-",my_set)
print("len of my set:-",len(my_set))
print("type of my set:-",type(my_set))

lst=(list(my_set))
lst.append(100)
print(set(lst))


# task >>>>>
my_set.union()
my_set1={1,332,42,23}
my_set2={5,64,88,9}
my_set =my_set1.union(my_set2)
print(my_set)

my_set.intersection()
my_set1={1,32,42,23,5,37,93,61}
my_set2={37,42,23,61}
my_set =my_set1.intersection(my_set2)
print(my_set)

my_set.difference()
my_set1={1,32,42,23,5,37,93,61}
my_set2={37,42,23,61}
my_set =my_set1.difference(my_set2)
print(my_set)

