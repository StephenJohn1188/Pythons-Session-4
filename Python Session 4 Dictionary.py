#!/usr/bin/env python
# coding: utf-8

# # Dictionary

# In[2]:


mydict={'EMPID':101,'Name':'Raja','Dept':'Staffing'}


# In[3]:


mydict


# In[4]:


mydict['EMPID']


# In[5]:


mydict['Name']


# In[6]:


mydict['Dept']


# In[7]:


mydict['Dept']='Human Resource'


# In[9]:


mydict


# In[10]:


mydict.keys()


# In[11]:


mydict.values()


# In[12]:


mydict.items()


# In[13]:


mydict.update({'Salary':10000})


# In[14]:


mydict


# In[15]:


print(mydict['EMPID'])


# In[16]:


print("EMPID: ", mydict['EMPID'])


# In[17]:


mydict['Salary']=25000


# In[18]:


mydict


# Exercise

# In[20]:


colourdict={'Rock':'Brown','Trees':'Green','Apple':'Red','Banana':'Yellow'}


# In[21]:


print(colourdict)


# In[22]:


colourdict.keys()


# In[23]:


colourdict.values()


# In[24]:


colourdict.items()


# Enhanced Operations in Dictionary

# In[25]:


del colourdict['Apple']


# In[27]:


colourdict


# In[28]:


colourdict.pop('Trees')


# Dictinary List Combination

# In[29]:


studentlist={'Enrollment Number':[101,102,103],'Name':['Kiran','Keerthi','Lavanya'],'Marks':[96,99,100]}


# In[30]:


studentlist


# In[31]:


studentlist.keys()


# In[32]:


studentlist.values()


# In[33]:


studentlist.items()


# In[34]:


studentlist.clear()


# In[35]:


del studentlist


# In[36]:


studentlist


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




