#!/usr/bin/env python
# coding: utf-8

# In[1]:


##here i am coding python

print("hello python programming")
character_name= "Nayeem"
charcater_age = 55
charcater_sex="male"
phrase="helloo"

print(character_name+" is "+str(charcater_age)+" years old and is "+charcater_sex)
print(phrase.upper().isupper())


# In[20]:


##replace theory

name = "Giraffe Academy"
print(name.replace("Giraffe","Nayeem's"))

name1= "Liam Neeson is a very tallented and thriller actor,i like him most"
print(name1.replace("Liam Neeson","Tom Cruise"))
print(name1.replace("tallented","active"))


# In[26]:


##math operations 
num,num1,num2
print("Working with addition")
num1=input("Enter number 1 : ")
num2=input("Enter number 2 : ")
num=float(num1)+float(num2)
print("Sum of num1 and num2 is : "+str(num))

##subtraction of input numbers
print("Working with subtraction")
num1=input("Enter number 1 : ")
num2=input("Enter number 2 : ")
num=float(num1)-float(num2)
print("subtraction of num1 and num2 is : "+str(num))

##multiplication of given numbers
print("Working with multiplication")
num1=input("Enter number 1 : ")
num2=input("Enter number 2 : ")
num=float(num1)*float(num2)
print("multiplication of num1 and num2 is : "+str(num))

##division of given numbers
print("Working with division")
num1=input("Enter number 1 : ")
num2=input("Enter number 2 : ")
num=float(num1)/float(num2)
print("Division of num1 and num2 is : "+str(num))


# In[24]:


##math operations

print(4/7+8)
##first modulus, division then multiplication subtraction then addition


# 

# In[30]:


num1=2
num2=5
num=num1**num2
print("2 to the power 5 is : "+str(num))


# In[6]:


print(10%3/5)
num=6
print(str(num))
print(str(num)+" is my favourite number")
print(abs(num))
num1=-66
print(abs(num1))
num2=88
print("This is 3 to the power 25: "+str(pow(3,25)))  ##that means 3^2


print("This is greater between the 55 and 78 : "+str(max(55,78)))  ##this will print out which number is big between these two
print("This is the smaller between 55 and 78 : "+str(min(55,78)))  ##this will print out which number is smaller between these two


# In[7]:


##working with input

name = input("Enter your name : ")
print("Hi, "+name)
age = input("Enter your age ")
print("Your age is : "+str(age))


# In[8]:


##working with lots of input in jupiter
namee= input("Enter the name : ")
age = input("Enter your age : ")
print("Hello, "+namee+" your age is "+age)


# In[9]:


namee= input("Enter the name : ")
age = input("Enter your age : ")
sex = input("Enter your sex : ")
prof = input("Enter your profession : ")
print("hello")
print("Hi there ! i am cortana,welcome "+namee+".You are a "+sex+" guy,i see.A "+prof+" working her entire life of age "+str(age)+" years.Congratulations on your success and thanks for your service ")


# In[10]:


from math import *
my_num=66  
##this will find out the closest full form number 
print("This is round of 3.4 :"+str(round(3.4))) 
print("floor  of 3.6 is : "+str(floor(3.6)))
print("ceil  of 55.3 is : "+str(ceil(55.3)))
print("square root of 49 is : "+str(sqrt(49)))


# In[11]:


color = input("Hello,please input any colour you want : ")
plural_noun= input("Input any plural nour : ")
celebrity = input("Enter celebrity name : ")

print("This is "+color+","+celebrity+" and "+plural_noun+" you have selected")


# In[13]:


hobby = input("Hello,please input any Hobby you want to share : ")
play= input("Input any Play you like : ")
food = input("Enter Food name you think delicios : ")

print(f"Your favourite food is {food},hobby is {hobby} and fav play {play} - that you have selected")


# In[38]:


##working with lists 
friends=["nayem","dipu","Kaosar","Aqib","araf"]
print("The total list is : "+str(friends))
print(str(friends[1])+" and "+str(friends[2])+ "is my best friends")


# In[ ]:





# In[ ]:




