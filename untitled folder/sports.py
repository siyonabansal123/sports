#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pillow


# In[2]:


from PIL import Image, ImageFont, ImageDraw


# In[3]:


my_image = Image.open("/Users/siyonabansal/Downloads/E-Certificate.jpeg")


# In[4]:


title_font = ImageFont.truetype('/Users/siyonabansal/Downloads/Oleo_Script_Swash_Caps/OleoScriptSwashCaps-Bold.ttf', 20)


# In[5]:


import pandas as pd

df = pd.read_csv(r'/Users/siyonabansal/Downloads/IITBSports.csv')
print (df)


# In[6]:


n= count_row = df.shape[0]  


# In[7]:


i=0
while i<n:
    Name=df.iloc[i,0]
    clg_name=df.iloc[i,1]
    img = my_image.copy()
    image_editable = ImageDraw.Draw(img)
    image_editable.text((140,440), Name , (0,0,0), font=title_font)
    image_editable.text((530,440), clg_name , (0,0,0), font=title_font)
    s= f'{i}'
    img.save("certi" + s +".jpg")
    i+=1


# In[ ]:




