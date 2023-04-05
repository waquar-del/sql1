#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
text = "Tomorrow we are going to watch movie and after that dinner. Rohan you will inform John, kartik and Manisha. Their numbers are +91 8124564397, +91 (755) 322 6754 and +1 (812)-654-6754. Please do't forget to call them. "
print(text)


# In[9]:


p1="\+\d{1,2}\s[(]\d{3}[)][\s-]\d{3}[\s-]\d{4}"
x=re.findall(p1,text)
print(x)


# In[10]:


text =  "05/3/2017  3/01/2017 1/6/17  34/11/937 may 21, 2017 21st mar 2017"
print(text)


# In[11]:


p1=r"(0?[1-9]|1?[0-9]|2?[0-9]|3?0[0,1]"


# In[16]:


date="\d{1,2}\/\d\/\d{4}|\d{1}\/\d{4}|\d{1}\/\d{1}\/\d{2}|\d{2}\|\d{2}\/\d{2}\/\d{3}"
x=re.findall(date,text)
print(x)


# In[35]:


date="(0?[0-9]|1?[0-9]2?[0-9]3?[0,1]"
month="(0?[0-9])|1?[0-2])"
year="(19?[0-9]{2}|20?[0-9]{2})"
sep="/"
pattern=date+sep+month+sep+year
print(pattern)


# In[34]:


p2=re.findall(pattern,text)
for i in p2:
    print(i)


# In[36]:


candidates = [
    'info@xcelvations.com',
    'nutan.xcelvations@gmail.com',
    'training@mail.xcelvations.com',
    'training123@xcelvations.in',
    'not-valid@example.zoo',
    'nutan@yahoo.com',
    'john_mathew@yahoo.xyz'
]


# In[38]:


gmail="\w[a-zA-Z0-9]"
x=re.findall(gmail,candidates)
print(x)


# In[43]:


mail=r"\w[a-zA-Z0-9_.]*@[\w\.]+(com|in)"
address=re.compile(mail)


# In[40]:


for i in candidates:
    match=address.search(mail)
    if match:
        print(match)
    else:
        print("no match")


# In[ ]:




