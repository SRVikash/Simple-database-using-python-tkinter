# Simple-database-using-python-tkinter

Ive created a simple tkinter application with sqlite3 database
to collect the information:

#### 1.first name
#### 2.last name
#### 3.address
#### 4.city
#### 5.state
#### 6.pincode

from the user and it can 
##### show the records ,delete the record using id and update the record using ID

# SAMPLE:

![alt text](https://github.com/SRVikash/Simple-database-using-python-tkinter/blob/main/screenshots/recording.gif)

## Note must decomment this line to create a new record 
'''
c.execute(""" CREATE TABLE record (
firstname text,
lastname text,
address text,
city text,
state text,
pincode integer
)""")
'''
