#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install meaningless


# In[2]:


import pyttsx3 
from meaningless import WebExtractor
import re


# In[3]:


engine = pyttsx3.init()
newVoiceRate = 140
#voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('rate',newVoiceRate)
#engine.setProperty('voice', voice_id)
known_numbers = [1,2,3]
f = open(r"C:\Users\ethic\Desktop\church\books.txt","r")
books = f.readlines()
new_books = []
for i in range(0,len(books)):
    #print(books[i].strip())
    new_books.append(books[i].strip())
#print(new_books)
#bible = WebExtractor(translation="ESV",show_passage_numbers=False)


# In[4]:


def say(text):
    engine.say(text)
    engine.runAndWait()


# In[5]:


def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    if len(array) ==5:
        array=array[1:]
        
    return array


# In[6]:


def extract_book_ref(verse):
    global numbers
    text_a=re.findall(r"[a-zA-z]+",verse)[0]
    if verse[0] in str(known_numbers):
        text= verse[0]+" "+text_a
        #print(len(text))
        numbers_ = verse[len(text)+1:]
        numbers = getNumbers(numbers_)
        #flag = True
    else:
        text= text_a
        numbers_ = verse[len(text)+1:]
        numbers = getNumbers(numbers_)
    
    #print(numbers)
    return(text)


# In[7]:


def final_text_reading1(book_,numbers,text,lesson):
    
    intro_text = lesson_check(lesson)
    
    if len(numbers) ==3:
        intro = intro_text +"is taken from the book of "+ book_ +", chapter "+numbers[0]+", verses "+numbers[1]+" to "+numbers[2]+ ". The book of "+ book_ +", chapter "+numbers[0]+", verses "+numbers[1]+" to "+numbers[2]+"."#exodus, chapter 1 , verses 1 to 10. The book of exodus, chapter 1 , verses 1 to 10. "
    else:
        intro = intro_text +"is taken from the book of "+ book_ +", chapter "+numbers[0]+" begining from verse "+numbers[1]+" to "+ book_ +", chapter "+numbers[2]+" and verse "+numbers[3]+". "+"The book of "+ book_ +", chapter "+numbers[0]+" begining from verse "+numbers[1]+" to "+ book_ +", chapter "+numbers[2]+" and verse "+numbers[3]+"."
        
    
    extro = "Here ends "+intro_text+", praise be to thee, O'christ."
    final_text = intro+" "+ text +" "+extro
    #print(final_text)
    
    return(final_text)


# In[8]:


def get_verse(book,numbers):
    bible = WebExtractor(translation="ESV",show_passage_numbers=False)
    chapter_from_ = int(numbers[0])
    verse_from_ = int(numbers[1])
    #chapter_to_ = input("upto which chpater? ")
    verse_to_ = int(numbers[2])
    #bible.get_passages()
    #print(book_,chapter_from_,verse_from_,verse_to_)
    #print()
    online = bible.get_passages(book_,chapter_from_,verse_from_,verse_to_)
    return(online)
def get_verse_double(book,numbers):
    bible = WebExtractor(translation="ESV",show_passage_numbers=False)
    chapter_from_ = int(numbers[0])
    verse_from_ = int(numbers[1])
    chapter_to_ = int(numbers[2])
    verse_to_ = int(numbers[3])
    #bible.get_passages()
    #print(book_,chapter_from_,verse_from_,verse_to_)
    #print()
    online = bible.get_passage_range(book_,chapter_from_,verse_from_,chapter_to_,verse_to_)
    return(online)


# In[9]:


def lesson_check(lesson):
    lessons = ["The first lesson ","The second lesson ","The responsive reading ","The gospal lesson "]
    if lesson == str(1) :
        intro_text = lessons[0]
    elif lesson == str(2):
        intro_text = lessons[1]
    elif lesson == "responsive":
        intro_text = lessons[2]
    elif lesson =="gospal":
        intro_text = lessons[3]
    else:
        intro_text = ""
     
    
    return(intro_text)


# In[10]:


def validation():
    global lesson
    print("Possible inputs ===> (1,2,responsive,gospal)")
    lesson = input("type of reading? ")
    while True:
        if lesson_check(lesson) != "":
            break
        else:
            print("please choose from possible inputs")
            print("Possible inputs ===> (1,2,responsive,gospal)")
            lesson = input("type of reading? ")
            continue

    


# In[11]:


def val_book(verse):
    
    text_val1=re.findall(r"[a-zA-z]+",verse)[0]
    text_val2 = verse[0:len(text_val1)]
    #print(text_val1 == text_val2)
    if  text_val1 != text_val2 :
        text_val2 = verse[0:len(text_val1)+2]
    #print(text_val2)
    for i in new_books:
        
        #print(text_val2 == i.lower())
        if text_val2 == i.lower():
            out = 'pass_'
            return(out)
            break
        else:
            out = 'nopass'
            continue

    #print(text_val1,text_val2)
    
    #print(out)
    


# In[12]:


def book_validate():
    global verse
    while True:
        verse = input("please give the ref                ")
        if val_book(verse.lower()) == "pass_":
            break
        else:
            print("the spelling seems to be wrong in the books name")
            continue
    


# In[14]:


while True:
  
   validation() 
   book_validate() 
   book_ = extract_book_ref(verse)

   if len(numbers) == 3:
       online = get_verse(book_,numbers)
       t=final_text_reading1(book_,numbers,online,lesson)
       print(t)
   else:
       online = get_verse_double(book_,numbers)
       t=final_text_reading1(book_,numbers,online,lesson)
       print(t)
   ready = input("Press 'Enter' when your ready ")
   if ready == "":
       #print("gg")
       say(final_text_reading1(book_,numbers,online,lesson))
   else:
       break
   again =input("once more?(y/n)")
   if again.lower() =='y':
       continue
   else:
       break

   
       
   


# In[ ]:





# In[ ]:





# In[ ]:




