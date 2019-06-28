from tkinter import *


from practice import *

def onClickSubmit():

    cRef = customer(None, None, None)
    cRef.name = entry_name.get()
    cRef.phone = entry_phone.get()
    cRef.email = entry_email.get()
    cRef.showCustomerDetails()

    db= dbHelper()
    db.saveCustomerInDB(cRef)


def onClickUpdate():

    cRef = customer(None, None, None)

    cRef.cid = entry_ID.get()
    cRef.name = entry_Updated_name.get()
    cRef.phone = entry_Updated_phone.get()
    cRef.email = entry_Updated_email.get()

    db = dbHelper()
    db.updateCustomerInDB(cRef)


def onClickDelete():
    cid = entry_Delete_ID.get()
    db = dbHelper()
    db.deleteCustomerInDB(cid)

def showData():
    sql = "select * from Customer order by name desc"

    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="dark_c_oder")

    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        txt.insert (0.0,row)
        txt.insert (0.0," ")


window = Tk()
window.title("DATABASE")
window.configure(background = "black")

#=========================== ADDING ================================================================================

addTitle = Label(window, text=" Add details of Customer Here!!!!!", bg = "black", font = "Times 20 bold underline italic", fg = "White")
addTitle.grid(row = "0", columnspan = "2")


label_space = Label(window, text="", bg = "black")
label_space.grid(row="1", column="0")

label_Name = Label(window, text="Name:", bg= "black", font =" Times 16 bold italic", fg="white")
label_Name.grid(row="2", column = "0", sticky="e")
label_phone = Label(window, text="Phone:", bg= "black", font =" Times 16 bold italic",fg="white")
label_phone.grid(row="3", column = "0", sticky="e")
label_Email = Label(window, text="Email:", bg= "black", font =" Times 16 bold italic",fg="white")
label_Email.grid(row="4", column = "0", sticky="e")

entry_name = Entry(window,bg = "light blue")
entry_name.grid(row="2", column = "1")
entry_phone = Entry(window,bg = "light blue")
entry_phone.grid(row="3", column = "1")
entry_email = Entry(window, bg = "light blue")
entry_email.grid(row="4", column = "1")

add_button = Button(window, text = "   Submit   ", font = "bold", command = onClickSubmit)
add_button.grid(row="5", columnspan = "2")

#==================================Update details===================================================================================

label_space = Label(window, text="", bg = "black")
label_space.grid(row="6", column="0")

addTitle2 = Label(window, text=" Update details of Customer Here!!!!!", bg = "black", font = "Times 20 bold underline italic", fg = "White")
addTitle2.grid(row = "7", columnspan = "2")

label_space = Label(window, text="", bg = "black")
label_space.grid(row="8", column="0")



label_ID = Label(window, text="Customer ID:", bg= "black", font =" Times 16 bold italic", fg="white")
label_ID.grid(row="9", column = "0", sticky="e")
label_Name = Label(window, text="Name:", bg= "black", font =" Times 16 bold italic", fg="white")
label_Name.grid(row="10", column = "0", sticky="e")
label_phone = Label(window, text="Phone:", bg= "black", font =" Times 16 bold italic",fg="white")
label_phone.grid(row="11", column = "0", sticky="e")
label_Email = Label(window, text="Email:", bg= "black", font =" Times 16 bold italic",fg="white")
label_Email.grid(row="12", column = "0", sticky="e")

entry_ID = Entry(window,bg = "light blue")
entry_ID.grid(row="9", column = "1")
entry_Updated_name = Entry(window,bg = "light blue")
entry_Updated_name.grid(row="10", column = "1")
entry_Updated_phone = Entry(window,bg = "light blue")
entry_Updated_phone.grid(row="11", column = "1")
entry_Updated_email = Entry(window, bg = "light blue")
entry_Updated_email.grid(row="12", column = "1")

update_button = Button(window, text = "   Update   ", font = "bold", command = onClickUpdate)
update_button.grid(row="13", columnspan = "2")



#==================================Delete details===================================================================================



addTitle3 = Label(window, text=" Delete details of Customer Here!!!!!", bg = "black", font = "Times 20 bold underline italic", fg = "White")
addTitle3.grid(row = "0", column = "4", columnspan = "2")

label_space = Label(window, text="", bg = "black")
label_space.grid(row="1", column="4")

label_ID = Label(window, text="Customer ID:", bg= "black", font =" Times 16 bold italic", fg="white")
label_ID.grid(row="2", column = "4", sticky="e")

entry_Delete_ID = Entry(window,bg = "light blue")
entry_Delete_ID.grid(row="2", column = "5")

Delete_button = Button(window, text = "   Delete   ", font = "bold", command = onClickDelete)
Delete_button.grid(row="3",column = "5", columnspan = "2")


#================================== Show Data ===================================================================================



addTitle4 = Label(window, text="Click Here ro Retrieve data", bg = "black", font = "Times 20 bold underline italic", fg = "White")
addTitle4.grid(row = "7", column = "4", columnspan = "2")

Delete_button = Button(window, text="   Show   ", font="bold", command = showData)
Delete_button.grid(row="9",column = "4")

txt = Text(window,width=48, height=10, wrap=WORD)
txt.grid(row="11", column="4", columnspan = "2", rowspan="8")

window.geometry("1200x700+0+0")
window.mainloop()