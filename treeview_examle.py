import datetime
from matplotlib import style
import ttkthemes
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('1020x600')
root.wm_title('Awesome Tree view')
root.update()
style=ttkthemes.ThemedStyle(root)
#print(style.get_themes())
style.theme_use('clam')
style.configure('Treeview',font=('Verdana',10),foreground='#2b2b2b',cellpadding=16)
style.configure('Treeview.Heading',font=('Verdana',10,'bold'),foreground='#444',background='silver')
style.map('Treeview',background=[('selected','darkgreen')],foreground=[('selected','orange')])

scrollbar=ttk.Scrollbar(root,orient='vertical')
scrollbar.pack(side='right',fill='y')

treeview=ttk.Treeview(root,columns=('ID','FNAME','SNAME','DEPARTMENT','SALARY'),show='headings',
                        selectmode='browse')
                        
treeview.pack(side='left',fill='both',expand=True)
treeview.heading('#1',text='ID',anchor=tk.CENTER)
treeview.heading('#2',text='FNAME',anchor=tk.CENTER)
treeview.heading('#3',text='SNAME',anchor=tk.CENTER)
treeview.heading('#4',text='DEPARTMENT',anchor=tk.CENTER)
treeview.heading('#5',text='SALARY',anchor=tk.CENTER)

treeview.column('#1',anchor=tk.CENTER)
treeview.column('#2',anchor=tk.CENTER)
treeview.column('#3',anchor=tk.CENTER)
treeview.column('#4',anchor=tk.CENTER)
treeview.column('#5',anchor=tk.CENTER)

treeview.tag_configure('odd',background='#eee')
treeview.tag_configure('even',background='#ddd')
treeview.configure(yscrollcommand=scrollbar.set)


def postPopUpMenu(event):
    row_id=treeview.identify_row(event.y)
    treeview.selection_set(row_id)
    row_values=treeview.item(row_id)['values']
    print(row_values)
    popUpMenu=tk.Menu(treeview,tearoff=0,font=('Verdana',11))
    popUpMenu.add_command(label='Edit/Update',accelerator='Ctrl+E')
    popUpMenu.add_command(label='Delete',accelerator='Delete',command=lambda:treeview.delete(row_id))
    popUpMenu.add_command(label='View',accelerator='Ctrl+P')
    popUpMenu.add_separator()
    popUpMenu.add_command(label='Send Email',accelerator='Alt+L')
    popUpMenu.add_command(label='Remove from Payroll',accelerator='Alt+Q')
    popUpMenu.post(event.x_root,event.y_root)


treeview.tag_bind('row','<Button-3>',lambda event:postPopUpMenu(event))
for i in range(1,101):
    if i%2==0:
        treeview.insert('','end',
                        values=(i,'Alfonce' +str(i),'Micah'+str(i),'Manager-Marketing',datetime.datetime.now()),
                        tags=('even','row'))


    else:
        treeview.insert('','end',
                        values=(i,'Brian' +str(i),'Yano'+str(i),'Director',datetime.datetime.now()),
                        tags=('odd','row'))
root.mainloop()