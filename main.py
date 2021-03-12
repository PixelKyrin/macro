import tkinter as tk

key = ""
selected = -1
ListBox_index = 0

#키보드 추가 함수
def Add_Keyboard():
    def key_down(e):
        global key
        key = e.keysym
        print("키 입력 : " + str(key))

    def main_proc():
        AddKey_Text["text"] = key
        win_AddKey.after(100, main_proc)

    def Add_ListBox():
        global ListBox_index
        ListBox_index += 1
        listBox.insert(ListBox_index, key)
        win_AddKey.destroy()

    win_AddKey = tk.Tk()
    win_AddKey.title("키보드 설정")
    win_AddKey.geometry("200x160")
    win_AddKey.attributes('-toolwindow', True)
    win_AddKey.bind("<KeyPress>", key_down) #키보드 입력 받기

    AddKey_Label = tk.Label(master=win_AddKey, text='추가할 키를 입력해 주세요.')
    AddKey_Label.place(x=23, y=10)

    AddKey_Text = tk.Label(master=win_AddKey, text=' ', font=("System", 5), relief='sunken')
    AddKey_Text.config(bg='LightGray')
    AddKey_Text.place(x=25, y=33, width=150, height=32)

    main_proc() #키보드 입력 받기

    Add_Btn = tk.Button(master=win_AddKey, text="완료", command=Add_ListBox)
    Add_Btn.place(x=75, y=120, width=60, height=25)

    win_AddKey.mainloop()

#ListBox 내용 삭제 함수
def Delete_ListBox():
    global selected
    if selected >= 0:  # Check this still isn't -1
        listBox.delete(selected)
        selected = -1
    else:
        print("Error", "Can't delete the selected item if you haven't selected anything!")


#ListBox seleted 함수
def list_clicked(e):
    print(e)
    global selected
    selected = int(listBox.curselection()[0])  # item number selected in list
    item = listBox.get(selected)  # text of selected item
    print(f"You have clicked item {selected} which is {item}")


#tk 기본 설정
win = tk.Tk()
win.title("Py Macro")
win.geometry("250x190")

#listbox 생성
listBox = tk.Listbox(win)
listBox.place(x=13, y=17, width=130, height=140)

#selected is ListBox element
listBox.bind('<<ListboxSelect>>', list_clicked)

#키보드 추가 박스 생성
Key_Box = tk.Button(win, text="키보드", borderwidth=2, command=Add_Keyboard)
Key_Box.place(x=155, y=17, width=70, height=30)

#마우스 추가 박스 생성
Mouse_Box = tk.Button(win, text="마우스", borderwidth=2)
Mouse_Box.place(x=155, y=52, width=70, height=30)

#시간 추가 박스 생성
Mouse_Box = tk.Button(win, text="시간", borderwidth=2)
Mouse_Box.place(x=155, y=87, width=70, height=30)

#지우기 박스 생성
Mouse_Box = tk.Button(win, text="지우기", borderwidth=2, command=Delete_ListBox)
Mouse_Box.place(x=155, y=122, width=70, height=30)

tk.mainloop()