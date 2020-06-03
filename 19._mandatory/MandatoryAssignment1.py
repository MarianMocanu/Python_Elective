# # Mandatory Assignment 1 - "Introduction to Python" Spring 2020
# 
# **The following assignments should be done in this Notebook, and Handed in as a .ipynp on fronter in the hand in folder.**
# 
# **Choose to do the tasks you find the easiest fist and do as much as you find possible.**
# 
# **You have one hour for all 3 assignments.**

# ## Springer Books

# On this link you can see a list of books from the publishing house "Springer".
# 
# https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview#gid=793911758
# 
# You can see the same data in [this csv file](springer.csv).
# 
# 
# 
# In this assignment you should download all pdf files off books belonging to the "English Package Name = Computer Science" category.







# ## Ceasar encryption

# In a Caesar encryption one moves all characters in a string N positions “forward” in the alphabet. So if the encryption N is 4,
# 
#     'a' becomes 'e' and
#     'm' becomes 'q'.
# 
# If the “forward move” exits the alphabet (like 'z' + 20) it wraps around.
# 
# 
# ### Task:
# 
#     Code a Caesar encryption algorithm.
#     Code a decryption algorithm.







# ### Test:
# 
# Encrypt and afterwards decrypt
# 
#     'thequickbrownfoxjumpsoverthelazydog', N=4.
#     'It all started 6 weeks ago. A truck, loaded with stripped gun parts got jack'd outside of Queens', N = 5
#     'Æbletærte er et lækkert alternative til rød grød med fløde', N=6
# 







# ## Library code

# > Create the library code for this client code output. 
# 
# As it is now, it is not pythonic.   
# Some parts of the code would reveal that it is a Java programmer that have written the code.   
# When you create the library code you should fix these mistakes and make it pythonic.                       
>>> bar = Bar() 
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'

>>> bar = Bar('Hello', 'World')
Traceback (most recent call last):
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
File "property_client.py", line 5, in __init__
    self.set_x(x)
File "property_client.py", line 29, in set_x
    raise TypeError('x has to be an "int"')
TypeError: x has to be an "int"

>>> bar = Bar(12, 'There')
>>> bar.y = 123 
>>> bar.set_x(1024)
>>> bar.get_x()
1024

>>> bar
{'_Bar__x': 12, 'y': 'There'}

>>> str(bar)
'x = 12, y = There'





