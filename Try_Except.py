
# coding: utf-8

# Example of "Try_Except_Finally"

# In[1]:

try:
    val = int(raw_input("Enter the number:"))
except:
    print "The entered number is not an integer"
finally:
    print "The finally block is executed"


# In[2]:

try:
    val = int(raw_input("Enter the number:"))
except:
    print "The entered number is not an integer"
finally:
    print "The finally block is executed"


# In[5]:

try:
    print 2 + 5
except:
    print " There was a type error!"


# In[6]:

try:
    2 + s
except:
    print " There was a type error!"


# In[8]:

def askint():
    while True:
        try:
            val = int(raw_input("Enter an integer no:"))
        except :
            print "the entered number is not an integer"
            continue
        else:
            print "Correct! that is an integer"
            break
        finally:
            print"Finally block get executed each time"
        print val
        


# In[9]:

askint()


# In[ ]:



