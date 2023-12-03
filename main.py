import tkinter as tk

#Создаем окно
win = tk.Tk()

#Создаем логотип
photo = tk.PhotoImage(file='8744146.png')
win.iconphoto(False, photo)

# Создаем заголовок и размеры окна, а так же параметры окна его цвет и прочее
win.config(bg ='#2DFF00') #Цвета можно указывать через код RGB
win.title('Графическое приложение')
win.geometry("500x600+10+10")
win.resizable(True, False) # изменение параметров окна программы
#Так же есть minsize and maxsize, что бы прописать допустимые границы растягивания приложения
# Создание виджетов
# Виджет Label
label_1 = tk.Label(win, text='Hello!',
                   bg='red',
                   fg='white',
                   font=('Arail', 20, 'bold'),
                   padx=10, #отступы
                   pady=20,
                   relief=tk.RAISED, #делаем кнопку более объемной, границы
                   bd= 5,
                   justify=tk.LEFT # выравнивание текста
                   )

label_1.pack()
# Виджет Button
def say_hello():
    print('Пора отдохнуть')
btn1 = tk.Button(win, text='Hello',
                 command=say_hello
                 )
btn1.pack()
def add_label():
    label = tk.Label(win,text='new')
    label.pack()
btn2 = tk.Button(win, text='Add new_label',
                 command=add_label
                 )
btn2.pack()
def counter():
    global count
    count += 1
    btn3['text'] = f' Счетчик: {count}'

count = 0
btn3 = tk.Button(win, text=f'Счетчик: {count}',
                 command=counter,
                 bg = 'red'
                 )
btn3.pack()



win.mainloop()
