


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter
import tkinter.messagebox

from pymongo import MongoClient
client = MongoClient('localhost', 27017, username='prjUser',password='123456')


mydb=client["database_for_python"]

movies=mydb.movies_project


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\nourd\OneDrive\Desktop\presentation-mongodb-python-todoapp-application-main\python_project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1137x665")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 665,
    width = 1137,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    568.0,
    332.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    906.0,
    160.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    337.0,
    150.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#85BCAD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=135.0,
    y=134.0,
    width=404.0,
    height=30.0
)

canvas.create_rectangle(
    113.0,
    336.0,
    993.005126953125,
    338.0,
    fill="#007E05",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))










def update_listbox():

    clear_listbox()

    
    for task in movies.find():
        lb_tasks.insert("end", task['name'])
    


def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task(event=None):
    task = entry_1.get()
    try :
        if task !="":
            movies.insert_one({'name':task})
            update_listbox()
        else:
            tkinter.messagebox.showwarning("Note!", "Please enter your movies")
        entry_1.delete(0, "end")
    except :
        tkinter.messagebox.showerror("ERROR!", "YOU DON'T HAVE THAT PERMETION YOU SHOLD BE ADMIN")

window.bind('<Return>', add_task)





def num_tasks():
    num_tasks = len(list(movies.find()))
    tkinter.messagebox.showinfo("INFORMATION","You have  {} Movies in List".format(num_tasks))
def delete_task():

 
    task = lb_tasks.get("active")


    confirm_del = tkinter.messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete task:   ** {} ** ?".format(task))
    if confirm_del:
        try :
            movies.delete_one({'name':task})
        except :
            tkinter.messagebox.showerror("ERROR!", "YOU DON'T HAVE THAT PERMETION YOU SHOLD BE ADMIN")
    update_listbox()



def update_task():


    oldtask = lb_tasks.get("active")
    newtask = entry_1.get()
    




    try :
        if newtask !="":
            confirm_del = tkinter.messagebox.askyesno("Confirm update", "Are you sure you want to update movie:   " +oldtask+ " to movie "+ newtask + " ?")
            if confirm_del:
                movies.update_one({'name':oldtask},{"$set":{'name':newtask}})
            update_listbox()
        else:
            tkinter.messagebox.showwarning("Note!", "Please enter your new movies")
    except :
            tkinter.messagebox.showerror("ERROR!", "YOU DON'T HAVE THAT PERMETION YOU SHOLD BE ADMIN")


def delete_all():

    confirm_del = tkinter.messagebox.askyesno("Delete All Confirmation", "Are you sure you want to delete all tasks?")
    try :
        if confirm_del:
            movies.delete_many({})
    except :
        tkinter.messagebox.showerror("ERROR!", "YOU DON'T HAVE THAT PERMETION YOU SHOLD BE ADMIN")

    update_listbox()

def exit():
    quit()

window.bind('<Return>', add_task)














button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=delete_all,
    relief="flat"
)
button_1.place(
    x=239.0,
    y=428.0,
    width=200.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
   command=num_tasks,
    relief="flat"
)
button_2.place(
    x=239.0,
    y=486.0,
    width=200.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=update_task,
    relief="flat"
)
button_3.place(
    x=239.0,
    y=543.0,
    width=200.0,
    height=32.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
   command=exit,
    relief="flat"
)
button_4.place(
    x=906.0,
    y=604.0,
    width=200.0,
    height=32.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=delete_task,
    relief="flat"
)
button_5.place(
    x=239.0,
    y=372.0,
    width=200.0,
    height=32.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=add_task,
    relief="flat"
)
button_6.place(
    x=222.0,
    y=216.0,
    width=234.0,
    height=35.0
)

lb_tasks = tkinter.Listbox(window)
lb_tasks.place(
    x=500.0,
    y=370.0,
    width=300,
    height=200,

)



def show_listbox():
    


    for task in movies.find():
        lb_tasks.insert("end", task['name'])
        

show_listbox()



window.resizable(False, False)
window.mainloop()
