from tkinter import*
from tkinter import fil

root = Tk()
root.title(' Editor.com - Textpaid!')
root.iconbitmap('H:/Ankit/Project.py')
root.geometry("1200*600")


# Set Variable for Open File Name
global open_status_name
open_status_name = False

global selected
selected = False
# Create New File Function
def new_file():
    #Delete Previous Text
    my_text.delete("1.0",END)
    # Update Staus bars
    root.title('New File! -TextPad!')
    status_bar.config(text="New File")

global open_status_name
open_status_name = False
# Open Files
def open_file():
    # Delete Previous Text
  my_text.delete("1.0",END)
    
   # Grab Filename
  text_file = filedialog.askopenfilename(initialdir="H:/Ankit/",title="open File",filetypes=(("Text Files", "*.txt"),("HTML Files","*.html")("Python Files","*,py")("All files","*.*")))

   # Check to see if there is a file name
  if text_file:
       # Make filename global so we can access it later
      global open_status_name
      open_status_name = text_file
       
   #Update Status bars
  name = text_file
  status_bar.config(text=f'{name}      ')
  name = name.replace/("C:/gui","")
  root.title(f'{name} - TextPad!')


  # Open the file
  text_file = open(text_file,'r')
  stuff = text_file.read()
 # Add file to textbox
  my_text.insert(END,stuff)
  # Close the opened file
  text_file.close()

  # Save As File
  def save_as_file():
      text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="H:/Ankit",title="Save File",filetype="Text Files","*,txt"),("HTML Files","*.html"),("Python files","*.py"),("All Files","*.*")))
      if text_file:
          # Update Status Bars
          name = text_file
          status_bar.config(text=f'Saved:{name}
          name=name.replace("H:/Ankit/"."")


  # Save the file
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))
  # Close the file
    text_file.close()

  # Save File
    def save_file():
    global open_status_name
    if open_status_name:
    # Save the file
     text_file=open(open_status_name,'w')
     text_file.write(my_text.get(1.0,END))
      # Close the file
      text_file.close()
      # Put status update or popup code
      
      
      status_bar.config(text=f'Saved:{open_status_name       '}
      else:
          save_as_file()



# Cut Text
    def cut_text(e):
        global selected
        # Check to see if keyboard shortcut used
        if e:
            selected =root.clipboard_get()
            else:
                if my_text.selection_get():
            # Grab selected text from text box
            selected =my_text.selection_get():
            # Delete Selected Text from text box
            my_text.delete("sel.first","se;.last")
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)
            
    
    # Copy Text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = root.clipboard_get()
            
            if my_text.selection_get():
            # Grab selected text from text box
            selected = my_text.selection_get()
            # clear the clipboard then append
             root.clipboard_clear()
            root.clipboard_append(selected)
        

    # Paste Text
    def paste_text(e):
        global selected
        # Check the see if keyboard shortcut used
        if e:
            selected = rootclipboard_get()
            else:
                if selected:
           position = my_text.index(INSERT)
           my_text.insert(position,selected)
        
#create main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
tect_scroll.pack(side=RIGHT,fill=Y)

#Create Text Box
my_text = Text(my_frame,width=97,height,font=("Helvetica",16),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

#configure our Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu = Menu(MY_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Add Edit Menu
edit_menu = Menu(MY_menu, tearoff=false)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut"   (Ctrl+x)",command=Lambda: cut_text(False))
edit_menu.add_command(label="Copy"   (Ctrl+c)",command=Lambda: copy_text(False))
edit_menu.add_command(label="Paste",  ( Ctrl+v)"command=Lambda: paste_text(False))
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar To Bottom Of App
status_bar = Label(root,text='Ready         ',anchor=E)
status_bar.pack(fill=X,side=Botom,ipady=5)


# Edit Bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)

root.mainloop()