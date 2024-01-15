import todo_app_functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todo_app_list.txt"):
    with open("todo_app_list.txt",'w') as file:
        pass
sg.theme('DarkAmber')
clock_lbl=sg.Text('',key='clock')
label=sg.Text("Enter to-do's here")
input_box=sg.InputText(tooltip="Enter todo",key='todo')
add_button=sg.Button("Add")
list_box=sg.Listbox(values=todo_app_functions.get_todos(),key="todos",enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_btn=sg.Button("Complete")
exit_btn=sg.Button("Exit")

window=sg.Window("My todo app", layout=[[clock_lbl],[label],[input_box,add_button],[list_box,edit_button,complete_btn],[exit_btn]], font=('Courier',22))
while True:
    event, values=window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos=todo_app_functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            todo_app_functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']
                todos=todo_app_functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                todo_app_functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select something",font=('Courier',22))
        case "Complete":
            try:
                todos=todo_app_functions.get_todos()
                todos.remove(values['todos'][0])
                todo_app_functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                break
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break



window.close()