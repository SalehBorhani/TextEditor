from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Text Editor")
root.geometry("800x500")
root.resizable(False , False)
# Set variable for filename
global open_status_name
open_status_name = False

global selected
selected = False

# Creat new file function
def new_file():
    my_text.delete(1.0, END)
    root.title("New File")
    status_bar.config(text="New File      ")

    global open_status_name
    open_status_name = False


# Open Files   
def open_file():
    # Delete Previous Text
    my_text.delete(1.0, END)
    # Grab Filename
    text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    # Check if there is a filename
    if text_file:
        global open_status_name
        open_status_name = text_file

    # Update Status bars
    name = text_file
    status_bar.config(text=f"{name}        ")
    root.title(f"{name}")

    # Open The Files
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    text_file.close()
    my_text.insert(END, stuff)

# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update Status Bar
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        root.title(f"{name}")

        # Save The Files
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save The Files
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f"Saved: {open_status_name}        ")

    else:
        save_as_file()

# Cutting Text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copying Text
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
        

# Pasting Text
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)



# Creat Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Creat Scroollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizantial Scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Creat Text Box
my_text = Text(my_frame, width=97, height=25, font=("Courier", 10, "italic"), selectforeground="blue", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Creat Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As",  command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda:cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda:copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda:paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")


# Add Status Bar To Bottom Of App
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Search Bar
Label(my_frame,text='Search: ').pack(side=LEFT)
modify = Entry(my_frame)

modify.pack(side=LEFT, fill=BOTH, expand=1)

modify.focus_set()

buttn = Button(my_frame, text='Find')
buttn.pack(side=RIGHT)
my_frame.pack(side=TOP)

def find():
	
	my_text.tag_remove('found', '1.0', END)
	ser = modify.get()
	if ser:
		idx = '1.0'
		while 1:
			idx = my_text.search(ser, idx, nocase=1,
							stopindex=END)
			if not idx: break
			lastidx = '%s+%dc' % (idx, len(ser))
			
			my_text.tag_add('found', idx, lastidx)
			idx = lastidx
		my_text.tag_config('found', foreground='blue')
	modify.focus_set()
buttn.config(command=find)



# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-p>', paste_text)

root.mainloop()
