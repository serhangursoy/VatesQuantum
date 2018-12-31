
from tkinter.ttk import *
from tkinter import *
import engine

# Global Window Obj
window = Tk()

# UI - Quantum Engine binding
def startQuantumComputing(realMachine,userHash,comb,infoLabel,btn,chk,chk_state):
    infoLabel["text"] = "RUNNING ALGORITHM... This might (and probably will) take a while.."
    chk.grid_remove()
    btn.grid_remove()
    window.update()
    # Call Quantum Engine
    infoLabel["text"] = engine.StartQuantum(not realMachine,userHash)
    btn.grid(row=5,column=0)
    btn["text"] = "Again?"
    btn["command"] = lambda: ResetAll(comb,infoLabel,btn,chk,chk_state)
    return

# Reset all UI Widgets
def ResetAll(comb,infoLabel,btn,chk,chk_state):
    infoLabel["text"]= "Pick one to get MD5 hash"
    comb['values']= engine.getAvailablePasswords()
    comb.current(1) #set the selected item
    comb.grid(row=3, column=1,sticky=W)
    btn["text"] = "Hash"
    btn["command"] = lambda: passSelected(comb,infoLabel,btn,chk,chk_state)
    return

# Grab User Selection from UI Combobox and asign new command to button
def passSelected(comb,infoLabel,btn,chk,chk_state):
    selection = comb.get()
    comb.grid_remove()
    btn.grid(row=5,column=0)
    chk.grid(row=4, column=0)
    someHash = engine.getSelectedHash(selection.strip() )
    print( "You have selected",selection, "and hash", someHash)
    infoLabel["text"] = "Great, you have selected " + str(selection) + "\n And it's hash is " + str(someHash) + "\nDo you want to test Quantum Searching?"
    btn["text"] = "Search"
    btn["command"] = lambda: startQuantumComputing(chk_state.get(),someHash,comb,infoLabel,btn,chk,chk_state)
    return

# --------------------------  STYLE START --------------------------------
combostyle = ttk.Style()
combostyle.theme_create('VatesStyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'transparent',
                                       'selectforeground': 'white',
                                       'fieldbackground': '#3b384a',
                                       'fieldforeground': '#41e9e1',
                                       'background': '#3b384a',
                                       'foreground': 'white'
                                       }}}
                         )
combostyle.theme_use('VatesStyle')
# -------------------------- STYLE END -----------------------------------
# Create window
window.title("Vates - Quantum Seer")
window.configure(background='#3b384a')
window.geometry("290x600")
window.wm_attributes('-alpha', 0.97)
window.resizable(False, False)

#Setting it up
img = PhotoImage(file="res/img/vates.png", height= 128, width=128)
imglabel = Label(window, image=img,  borderwidth=0, relief="flat").grid(row=0,column=0,pady=20, columnspan=100)
Label(window, text="Welcome to Vates!\n", background="#3b384a", foreground="white",font=("Arial", 24), justify="center").grid(row=1,columnspan=100)
Label(window, text="This is a really simple implementation of Grover's Algorithm. In it's current state, it looks too trivial and perhaps unnecessary. However, once we have more qubits on our hands, possibilities are infinite!", background="#3b384a", foreground="white",wraplength=280).grid(row=2,columnspan=80)
lbl = Label(window, text="Pick one to get MD5 hash",background='#3b384a', foreground="white", relief="flat", wraplength=290)
lbl.grid(row=3, column=0, sticky=W)
combo = Combobox(window)
combo['values']= engine.getAvailablePasswords()
combo.current(1) #set the selected item
combo.grid(row=3, column=1,sticky=W)
btn = Button(window,text="Hash", background="black", foreground="white", relief="flat", borderwidth=10)
btn.grid(row=4, column=0, columnspan=2, pady=10)
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Simulate?', var=chk_state,background='#3b384a', foreground="white",activebackground="#3b384a",highlightbackground="#3b384a",relief="flat",highlightthickness=0,selectcolor="#3b384a")
btn["command"] = lambda: passSelected(combo, lbl, btn, chk, chk_state)
# Loop
window.mainloop()
