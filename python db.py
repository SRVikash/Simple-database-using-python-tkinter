from tkinter import *
import sqlite3
root=Tk()
root.title("Database Tk")
root.geometry("400x600")
#create or connect database
con=sqlite3.connect("record.db")
#create cursor
c=con.cursor()
#create table
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
def edit():
    global editor
    editor=Tk()
    editor.title("Update record")
    editor.geometry("400x600")
    #create or connect database
    con=sqlite3.connect("record.db")

    #create cursor
    c=con.cursor()

    recordid=deletebox.get()

    #Query database
    c.execute("SELECT * FROM record WHERE oid = "+recordid)
    records=c.fetchall()

    #create global variable for textbox
    global fname_editor
    global lname_editor
    global address_editor
    global city_editor
    global state_editor
    global pincode_editor

    fnamelab_editor=Label(editor,text="Enter the First name:")
    fnamelab_editor.grid(row=0,column=0)
    fname_editor=Entry(editor,width=30)
    fname_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    lnamelab_editor=Label(editor,text="Enter the Last name:")
    lnamelab_editor.grid(row=1,column=0)
    lname_editor=Entry(editor,width=30)
    lname_editor.grid(row=1,column=1,pady=(10,0))
    addlab_editor=Label(editor,text="Enter the Address:")
    addlab_editor.grid(row=2,column=0)
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1,pady=(10,0))
    citylab_editor=Label(editor,text="Enter the name of the City:")
    citylab_editor.grid(row=3,column=0)
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=3,column=1,pady=(10,0))
    statelab_editor=Label(editor,text="Enter the name of the State:")
    statelab_editor.grid(row=4,column=0)
    state_editor=Entry(editor,width=30)
    state_editor.grid(row=4,column=1,pady=(10,0))
    fnamelab_editor=Label(editor,text="Enter the PINCODE")
    fnamelab_editor.grid(row=5,column=0)
    pincode_editor=Entry(editor,width=30)
    pincode_editor.grid(row=5,column=1,pady=(10,0))

    #loop through results
    for rec in records:
        fname_editor.insert(0,rec[0])
        lname_editor.insert(0,rec[1])
        address_editor.insert(0,rec[2])
        city_editor.insert(0,rec[3])
        state_editor.insert(0,rec[4])
        pincode_editor.insert(0,rec[5])

    #Save button
    sub_editor=Button(editor,text="Save",command=update)
    sub_editor.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=170)



    editor.mainloop()

def update():
    #create or connect database
    con=sqlite3.connect("record.db")

    #create cursor
    c=con.cursor()
    record_id=deletebox.get()
    #update
    c.execute(""" UPDATE record SET
    firstname = :first,
    lastname = :last,
    address = :address,
    city = :city,
    state = :state,
    pincode = :pincode

    WHERE oid = :oid""",
    {
     'first': fname_editor.get(),
     'last': lname_editor.get(),
     'address': address_editor.get(),
     'city': city_editor.get(),
     'state': state_editor.get(),
     'pincode': pincode_editor.get(),
     'oid':record_id

    }

    )

    #commit
    con.commit()
    #close the connection
    con.close
    editor.destroy()

def delete():
    #create or connect database
    con=sqlite3.connect("record.db")
    #create cursor
    c=con.cursor()
    #delete record
    c.execute("DELETE from record WHERE oid= " + deletebox.get())

    #commit
    con.commit()
    #close the connection
    con.close
    #clear the textbox

def submit():
    #create or connect database
    con=sqlite3.connect("record.db")
    #create cursor
    c=con.cursor()
    #insert into table
    c.execute("INSERT INTO record VALUES(:fname, :lname, :address, :city, :state, :pincode)",
    {
      'fname':fname.get(),
      'lname':lname.get(),
      'address':address.get(),
      'city':city.get(),
      'state':state.get(),
      'pincode':pincode.get()
    }
    )
    #commit
    con.commit()
    #close the connection
    con.close
    #clear the textbox
    fname.delete(0,END)
    lname.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)
def query():
    #create or connect database
    con=sqlite3.connect("record.db")

    #create cursor
    c=con.cursor ()

    #Query database
    c.execute("SELECT *, oid FROM record")
    records=c.fetchall()

    print_rec=''
    for rec in records:
        print_rec += str(rec[6])+ "\t" +str(rec[0])+ " " +str(rec[1])+ "\n"

    lab=Label(root,text=print_rec)
    lab.grid(row=12,column=0,columnspan=2)
    print(records)
    #commit
    con.commit()
    #close the connection
    con.close
fnamelab=Label(root,text="Enter the First name:")
fnamelab.grid(row=0,column=0)
fname=Entry(root,width=30)
fname.grid(row=0,column=1,padx=20,pady=(10,0))
lnamelab=Label(root,text="Enter the Last name:")
lnamelab.grid(row=1,column=0)
lname=Entry(root,width=30)
lname.grid(row=1,column=1,pady=(10,0))
addlab=Label(root,text="Enter the Address:")
addlab.grid(row=2,column=0)
address=Entry(root,width=30)
address.grid(row=2,column=1,pady=(10,0))
citylab=Label(root,text="Enter the name of the City:")
citylab.grid(row=3,column=0)
city=Entry(root,width=30)
city.grid(row=3,column=1,pady=(10,0))
statelab=Label(root,text="Enter the name of the State:")
statelab.grid(row=4,column=0)
state=Entry(root,width=30)
state.grid(row=4,column=1,pady=(10,0))
fnamelab=Label(root,text="Enter the PINCODE")
fnamelab.grid(row=5,column=0)
pincode=Entry(root,width=30)
pincode.grid(row=5,column=1,pady=(10,0))
deletebox=Entry(root,width=30)
deletebox.grid(row=8,column=1)
idlabel=Label(root,text="ID number")
idlabel.grid(row=8,column=0)
#Submit button
sub=Button(root,text="Add record to database",command=submit)
sub.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
#query button
quer=Button(root,text="Show records",command=query)
quer.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=129)
#delete button
dele=Button(root,text="Delete record",command=delete)
dele.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=133)
editbut=Button(root,text="Edit record",command=edit)
editbut.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=140)
#commit
con.commit()
#close the connection
con.close
root.mainloop()
