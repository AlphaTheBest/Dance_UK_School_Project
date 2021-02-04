import tkinter as tk
from tkinter import font as tkfont

class Sample_APP(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.title_font = tkfont.Font(family = 'Helvetica', size = 18, weight = 'bold', slant = 'italic')

        container = tk.Frame(self)
        container.pack(side= 'top', fill = 'both', expand = True)
        container.grid_rowconfigure


class Entry_Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.create_widgets()

    def create_widgets(self):

        self.Judges = tk.Button(self, text = "Judges", command = self.Judges_Menu)
        self.Judges.pack(side="top")

        self.Couples = tk.Button(self, text = "Couples", command = self.Couple_Menu)
        self.Couples.pack(side = "top")

        self.quit = tk.Button(self, text="QUIT", fg="red",  command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def Judges_Menu(self):
        self.destroy()
        Temporary_Master_Container = self.master
        
        Judge_Menu(Temporary_Master_Container)

    def Couple_Menu(self):
        self.destroy()
        Temporary_Master_Container = self.master
        
        Couple_Menu(Temporary_Master_Container)
        

class Judge_Menu(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.Input_Label_Couple_Name = tk.Label(self, text = "Couple_Name")
        self.Input_Label_Couple_Name.pack()

        self.Input_Box_Couple_Name = tk.Entry(self)
        self.Input_Box_Couple_Name.pack()
        
        self.Input_Label_Judge_1 = tk.Label(self, text = "Judge 1")
        self.Input_Label_Judge_1.pack()

        self.Input_Box_Judge_1 = tk.Entry(self)
        self.Input_Box_Judge_1.pack()

        self.Input_Label_Judge_2 = tk.Label(self, text = "Judge 2")
        self.Input_Label_Judge_2.pack()

        self.Input_Box_Judge_2 = tk.Entry(self)
        self.Input_Box_Judge_2.pack()

        self.Input_Label_Judge_3 = tk.Label(self, text = "Judge 3")
        self.Input_Label_Judge_3.pack()

        self.Input_Box_Judge_3 = tk.Entry(self)
        self.Input_Box_Judge_3.pack()

        self.Input_Label_Judge_4 = tk.Label(self, text = "Judge 4")
        self.Input_Label_Judge_4.pack()

        self.Input_Box_Judge_4 = tk.Entry(self)
        self.Input_Box_Judge_4.pack()

        self.Input_Label_Judge_5 = tk.Label(self, text = "Judge 5")
        self.Input_Label_Judge_5.pack()

        self.Input_Box_Judge_5 = tk.Entry(self)
        self.Input_Box_Judge_5.pack()
        
        self.Test_Button = tk.Button(self, text = "Test_1", command = lambda: self.Calculate_Couple_Total_Score(self.Get_Judge_Entries()))
        self.Test_Button.pack()


    def Get_Judge_Entries(self):
        
        Judge_1_Entry = int(self.Input_Box_Judge_1.get())
        Judge_2_Entry = int(self.Input_Box_Judge_2.get())
        Judge_3_Entry = int(self.Input_Box_Judge_3.get())
        Judge_4_Entry = int(self.Input_Box_Judge_4.get())
        Judge_5_Entry = int(self.Input_Box_Judge_5.get())

        return [Judge_1_Entry, Judge_2_Entry, Judge_3_Entry, Judge_4_Entry, Judge_5_Entry]

    def Calculate_Couple_Total_Score(self, Couple_Results):
        
        Local_Scores = Couple_Results
        print(Local_Scores)

        True_Min = min(Local_Scores)
        True_Max = max(Local_Scores)

        Min_Found = False
        Max_Found = False

        counter = 0

        for i in Local_Scores:
            if Local_Scores[counter] == True_Min and Min_Found == False:
                Local_Scores.pop(counter)
                Min_Found = True

            if Local_Scores[counter] == True_Max and Max_Found == False:
                Local_Scores.pop(counter)
                Max_Found = True

            counter = counter + 1

        Total = 0

        for i in Local_Scores:
            Total = Total + i

        print(Total)
    


class Couple_Menu(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.Couple_Test_Button = tk.Button(self, text = "Test_2", command = self.Test_Button)
        self.Couple_Test_Button.pack()

    def Test_Button(self):
        print("This works too!")
        

root = tk.Tk()
app = Entry_Menu(master=root)
app.mainloop()


