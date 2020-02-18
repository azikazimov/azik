# made by g.shanin : 09.11.2019
# name : interactive desk
# user : school
# adm_pass : 1111
# ###############################################################################
# Функционал 
# [1] : Возможность узнать расписание уроков на неделю
# [2] : Возможность узнать расписание автобусов, проходящих через станцию Сосново
# [3] : Возможность узнать расписание электричек до Санкт - Петербурга
# [4] : Возможность добавить расписание уроков в виде таблицы в формате xlsx

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
import xlrd
import webbrowser as wb

# класс главного окна
# openAdminDialog -> вызывает класс topAdmin (класс окна для ввода пароля администратора)
# задача : открывать главное окно

# возвращенное значение имени файла
valuesFromXlsx = ''

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        infoCanvas = tk.Canvas(self, width=800, height=800)
        buttonCanvas = tk.Canvas(self, width=500, height=800)
        self.add_imageOne = tk.PhotoImage(file='images/knopka1.gif')
        self.add_imageTwo = tk.PhotoImage(file='images/knopka2.gif')
        self.add_imageThree = tk.PhotoImage(file='images/knopka3.gif')
        self.add_imageFour = tk.PhotoImage(file='images/knopka4.gif')
        buttonLessons = tk.Button(buttonCanvas, bd=0, compound=tk.TOP, image=self.add_imageOne, command=self.openTree)
        buttonBuses = tk.Button(buttonCanvas, bd=0, compound=tk.TOP, image=self.add_imageTwo, command=self.openBuses)
        buttonTrains = tk.Button(buttonCanvas, bd=0, compound=tk.TOP, image=self.add_imageThree, command=self.openTrains)
        buttonOpenAdmin = tk.Button(buttonCanvas, command=self.openAdminDialog, bd=0, compound=tk.TOP, image=self.add_imageFour)
        buttonCloseApp = tk.Button(buttonCanvas, command=self.openAdminExit, text='[x]', compound=tk.TOP, image='')

        buttonCanvas.create_window(120, 150, width=230, height=120, window=buttonLessons)
        buttonCanvas.create_window(120, 300, width=230, height=120, window=buttonBuses)
        buttonCanvas.create_window(120, 450, width=230, height=120, window=buttonTrains)
        buttonCanvas.create_window(120, 600, width=230, height=120, window=buttonOpenAdmin)
        buttonCanvas.create_window(20, 20, window=buttonCloseApp)

        buttonCanvas.pack(side=tk.LEFT, fill=tk.BOTH)
        infoCanvas.pack(side=tk.LEFT, fill=tk.BOTH)

    def openAdminDialog(self):
        topAdminLessons()

    def openTree(self):
        treeLessons()

    def openBuses(self):
        busList()

    def openTrains(self):
        trainList()

    def openAdminExit(self):
        topAdminExit(self)

# класс окна для ввода пароля
# showPanel -> создает окно для ввода пароля
# задача : открыть окно для ввода пароля по нажатию на кнопку

class topAdminLessons(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.showPanel()
        self.packWidgets()

    def showPanel(self):
        self.title('Admin')
        self.geometry('+400+100')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def packWidgets(self):
        self.labelGuess = ttk.Label(self, text='Введите пароль')
        self.entryPass = ttk.Entry(self, show='*')
        self.buttonEnter = ttk.Button(self, text='Подтвердить', command=self.askFile)
        self.buttonExit = ttk.Button(self, text='Отменить', command=self.destroy)

        self.labelGuess.grid(row=0, column=0, padx=5, pady=3)
        self.entryPass.grid(row=0, column=1, columnspan=2, padx=5, pady=3)
        self.buttonEnter.grid(row=1, column=0, padx=5, pady=3)
        self.buttonExit.grid(row=1, column=1, padx=5, pady=3)

    def askFile(self):
        global valuesFromXlsx

        try:
            if self.entryPass.get().lower() == '1111':
                asking = askopenfile()
                valuesFromXlsx = asking.name
                self.destroy()
            else:
                self.delete(0, tk.END)
        except AttributeError:
            pass

class topAdminExit(tk.Toplevel):
    def __init__(self, master):
        super().__init__(root)
        self.master = master
        self.showPanel()
        self.packWidgets()

    def showPanel(self):
        self.title('Admin')
        self.geometry('+400+100')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def packWidgets(self):
        self.labelGuess = ttk.Label(self, text='Введите пароль')
        self.entryPass = ttk.Entry(self, show='*')
        self.buttonEnter = ttk.Button(self, text='Подтвердить', command=self.destroyAll)
        self.buttonExit = ttk.Button(self, text='Отменить', command=self.destroy)

        self.labelGuess.grid(row=0, column=0, padx=5, pady=3)
        self.entryPass.grid(row=0, column=1, columnspan=2, padx=5, pady=3)
        self.buttonEnter.grid(row=1, column=0, padx=5, pady=3)
        self.buttonExit.grid(row=1, column=1, padx=5, pady=3)

    def destroyAll(self):
        if self.entryPass.get().lower() == '1111':
            self.destroy()
            self.master.quit()
        else:
            self.delete(0, tk.END)

class treeLessons(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.openTreeLessons()

    def openTreeLessons(self):
        setting = 100
        self.tree = ttk.Treeview(self, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'), height=10, show='headings')
        self.scroll = tk.Scrollbar(self.tree, orient='vertical')
        self.tree.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)
        self.scrollX = tk.Scrollbar(self.tree, orient='horizontal')
        self.tree.config(xscrollcommand=self.scrollX.set)
        self.scrollX.config(command=self.tree.xview)

        # [ИСПРАВИТЬ!] : вынужденная мера -> меняем размеры колонок
        self.tree.column("1", width=setting, anchor=tk.CENTER)
        self.tree.column("2", width=setting, anchor=tk.CENTER)
        self.tree.column("3", width=setting, anchor=tk.CENTER)
        self.tree.column("4", width=setting, anchor=tk.CENTER)
        self.tree.column("5", width=setting, anchor=tk.CENTER)
        self.tree.column("6", width=setting, anchor=tk.CENTER)
        self.tree.column("7", width=setting, anchor=tk.CENTER)
        self.tree.column("8", width=setting, anchor=tk.CENTER)
        self.tree.column("9", width=setting, anchor=tk.CENTER)
        self.tree.column("10", width=setting, anchor=tk.CENTER)
        self.tree.column("11", width=setting, anchor=tk.CENTER)

        self.tree.heading("1", text='1 класс')
        self.tree.heading("2", text='2 класс')
        self.tree.heading("3", text='3 класс')
        self.tree.heading("4", text='4 класс')
        self.tree.heading("5", text='5 класс')
        self.tree.heading("6", text='6 класс')
        self.tree.heading("7", text='7 класс')
        self.tree.heading("8", text='8 класс')
        self.tree.heading("9", text='9 класс')
        self.tree.heading("10", text='10 класс')
        self.tree.heading("11", text='11 класс')

        global valuesFromXlsx
        try:
            # [!] добавить сюда окно с вводом количества уроков (мкксимальное значение в неделю)
            wb = xlrd.open_workbook(valuesFromXlsx)
            sh = wb.sheet_by_index(0)

            for j in range(1, 48):
                self.tree.insert('', 'end', values=(sh.row_values(j)))

        except FileNotFoundError:
            # добавить сюда окно с предупреждением
            pass

        self.title('Расписание уроков')
        self.geometry('1200x500')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.tree.pack(fill='both', expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

class busList():
    def __init__(self):
        self.openBusList()

    def openBusList(self):
        urlBuses = 'https://rasp.yandex.ru/station/9813797'
        window = wb.open(urlBuses, 0, True)

class trainList():
    def __init__(self):
        self.openTrainList()

    def openTrainList(self):
        urlTrains = 'https://rasp.yandex.ru/suburban/sosnovo-train-station--sankt-peterburg-finlyandskiy/today'
        window = wb.open(urlTrains, 0, True)

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()

    root.attributes('-fullscreen', True) # open window on all display
    root.geometry('1920x1080')
    root.title('Интерактивная панель')
    root.mainloop()
