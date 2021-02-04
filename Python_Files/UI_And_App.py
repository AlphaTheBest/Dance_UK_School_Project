import tkinter as tk
from tkinter import font as tkfont

import os

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

        self.Label_Show_Number_Of_Couples = tk.Label(self, text = "Number of Couples")
        self.Label_Show_Number_Of_Couples.pack()

        self.Couples_Registered_So_Far = 0
        self.Text_For_Couple_Number_Label = tk.StringVar()
        
        self.Label_Number_Of_Couples_So_Far = tk.Label(self, textvariable = self.Text_For_Couple_Number_Label)
        self.Label_Number_Of_Couples_So_Far.pack()

        self.Text_For_Couple_Number_Label.set(str(self.Couples_Registered_So_Far))
        
        self.Input_Label_Round_Name = tk.Label(self, text = "Round_Name")
        self.Input_Label_Round_Name.pack()

        self.Input_Box_Round_Name = tk.Entry(self)
        self.Input_Box_Round_Name.pack()
        
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
        
        self.Test_Button = tk.Button(self, text = "Total & Save", command = lambda: self.Calculate_Couple_Total_Score(self.Get_Judge_Entries()))
        self.Test_Button.pack()


    def Get_Judge_Entries(self):

        self.Couples_Registered_So_Far = self.Couples_Registered_So_Far + 1
        self.Text_For_Couple_Number_Label.set(str(self.Couples_Registered_So_Far))
      
        Judge_1_Entry = int(self.Input_Box_Judge_1.get())
        Judge_2_Entry = int(self.Input_Box_Judge_2.get())
        Judge_3_Entry = int(self.Input_Box_Judge_3.get())
        Judge_4_Entry = int(self.Input_Box_Judge_4.get())
        Judge_5_Entry = int(self.Input_Box_Judge_5.get())

        self.Input_Box_Judge_1.delete(0, "end")
        self.Input_Box_Judge_2.delete(0, "end")
        self.Input_Box_Judge_3.delete(0, "end")
        self.Input_Box_Judge_4.delete(0, "end")
        self.Input_Box_Judge_5.delete(0, "end")

        return [Judge_1_Entry, Judge_2_Entry, Judge_3_Entry, Judge_4_Entry, Judge_5_Entry]

    def Calculate_Couple_Total_Score(self, Couple_Results):
        
        Local_Scores = Couple_Results
        print(Local_Scores)
        #This is here to save ALL  results, including the minimum and maximum.
        Save_All_Scores = Local_Scores.copy()

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

        Couple_Name = self.Input_Box_Couple_Name.get()
        Round_Name = self.Input_Box_Round_Name.get()

        print(Couple_Name)

        self.Local_Results_Cache(Round_Name, Couple_Name, Total)
        self.Save_Couple_Scores_And_Total(Save_All_Scores, Total, Couple_Name, Round_Name)

        self.Input_Box_Couple_Name.delete(0, "end")

    def Save_Couple_Scores_And_Total(self, scores, total, couple_name, round_name):

        path = os.path.abspath(os.getcwd())

        try:
            New_File = open(path + "\\" + couple_name + "\\" + round_name + ".txt", "w")

        except IOError:
            os.mkdir(path + "\\" + couple_name)
            New_File = open(path + "\\" + couple_name + "\\" + round_name + ".txt", "w")

        Score_Holder = scores

        for i in Score_Holder:
            New_File.write(str(i)+"*")

        New_File.write(str(total))
        New_File.close()

    def Local_Results_Cache(self, Round_Name, Couple_Name, Total):

        path = os.path.abspath(os.getcwd())

        try:
            Open_File = open(path + "\\events\\" + Round_Name + ".txt", "a")

        except IOError:
            os.mkdir(path + "\\events")
            Open_File = open(path + "\\events\\" + Round_Name + ".txt", "a")
        
        File_Name = Round_Name
        
        File_Cache_Contents = "{" + Couple_Name + "," + str(Total) + "}\n"
        
        Open_File.write(File_Cache_Contents)
        Open_File.close()


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





