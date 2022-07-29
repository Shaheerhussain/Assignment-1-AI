#!/usr/bin/env python
# coding: utf-8

# # NAME: SHAHEER HUSSAIN 
# # Roll No: PIAIC127980

# # 1.Assign a message to a variable and then print that message

# In[2]:


greetings = "Hello to programming world"
print(greetings)


# # 2.Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

# In[3]:


name="Albert Einstein once said,"
quote="A person who never made a mistake never tried anything new."
print(name,'"',quote,'"') 


# # 3.Calculate Area of a Circle: Write a Python program which accepts the radius of a circle from the user and compute the area.

# In[13]:


radius = float(input(" Enter radius of the circle : "))

print(" Input Radius:",radius)
print ("Area of Circle with radius " + str(radius) + " is: " + str(3.141 * radius**2))


# # 4.Check Number either positive, negative or zero:: Write a Python program to check if a number is positive,

# In[19]:


num = float(input("Enter a number: "))
if num > 0:
    print("Positive Number Entered")
elif num == 0:
    print("Zero Entered")
else:
    print("Negative number Entered")


# # 5. Vowel Tester Write a Python program to test whether a passed letter is a vowel or not

# In[21]:


vowel = input(" Enter a character:")
if vowel == 'A' or vowel == "a" or vowel == 'E' or vowel == 'e' or vowel == 'I' or vowel == 'i' or vowel == 'O' or vowel == 'o' or vowel == 'U' or vowel == 'u':
    print('Letter',vowel,"is Vowel")
else:
    print("Letter",vowel,"is not vowel")


# 
# # 6. BMI Calculator Write a Python program to calculate body mass index Program

# In[25]:


height = float(input("Enter Height in Cm: "))
weight = float(input("Enter Weight in Kg:: "))
height_m = height / 100
print("Your body mass index is: ", weight / (height_m * height_m) )


# # 7. Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
# 
# 

# In[27]:


name = ['Arshad' , 'Rahil' ,  'Awais' , 'Rabeet' , 'Ahsan' , 'Mubashir']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# # Start with the list you used in Question 4, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# In[29]:


for friend in name:
    print(friend,"is a nice guy ")


# # Make a python program that conatains your nine favourite dishes in a list called foods. Print the message, The first three items in the list are:
# 
# Then use a slice to print the first three items from that program’s list.
# 
# Print the message, Three items from the middle of the list are:
# 
# Use a slice to print three items from the middle of the list.
# 
# Print the message, The last three items in the list are:
# 
# Use a slice to print the last three items in the list.
# 

# In[34]:


foods = ['biryani','burger','pizza','pasta','macroni','spheghetti','nuggets','corn','mommos']
print('The first three items in the list are',foods[0:3])
print('Three items from the middle of the list are',foods[3:6])
print('The last three items in the list are',foods[6:])


# # Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods. Then, do the following:
# 
# Add a new dish to the original list.
# 
# Add a different dish to the list friend_foods.
# 
# Prove that you have two separate lists.
# 
# Print the message, My favorite pizzas are: and then use a for loop to print the first list.
# 
# Print the message,
# 
# My friend’s favorite foods are:, and then use a for loop to print the second list.
# 
# NOTE: Make sure each new dish is stored in the appropriate list.
# 
# 

# In[35]:


friends_food = foods[0:9]
foods.append("tikka")
friends_food.append("chargha")
print(foods)
print(friends_food)


# In[38]:


print("My favorite pizzas are : ")
for items in foods:
    print(items)


# In[39]:


print("My friends favorite foods are : ")
for item in friends_food:
    print(item)


# In[ ]:




