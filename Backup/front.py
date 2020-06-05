
import pandas as pd
from tkinter import *
from tkinter import Tk,Button,Label,ttk
from tkinter import filedialog
from tkinter import simpledialog
from Homepage import Summarize
from tkinter import messagebox as mb
def onclick():
    print("Button clicked")
class FrontEnd:
    def __init__(self,master):
        self.master=master
        master.title("Text summaraization")
        master.minsize (600, 400)
        master.configure (bg='sky blue')
        options = [
            "sports",
            "Education",
            "politics",
            "Health",
            "tech"
        ]
        Clicked = StringVar ()
        Clicked.set (options[0])

        label = Label (root, text="choose the fields", bg='sky blue', fg='black')
        label.pack ()
        label.place (x=120, y=80)
        fields = ttk.Combobox (root, value=options)
        fields.pack ()
        fields.place (x=220, y=80)



        #upload the file
        self.upload_file_button = Button (master, text="Upload files", command=self.fileDialog)
        self.upload_file_button.pack ()
        self.upload_file_button.place (x=380, y=80)


        # original file display
        self.display1_button = Button (master, text="Show Original File", command=self.a_w)
        self.display1_button.pack ()
        self.display1_button.place (x=380, y=115)

        # summary file display
        self.display2_button = Button (master, text="Show Summarized File", command=self.summary)
        self.display2_button.pack ()
        self.display2_button.place (x=380, y=180)


        #print the file
        self.print1 = Button (master, text="print")
        self.print1.pack ()
        self.print1.place (x=5, y=5)

        #generate the file
        self.pdf_button = Button (master, text="Generate pdf")
        self.pdf_button.pack ()
        self.pdf_button.place (x=50, y=5)


        #sumbit button conncet to backend button
        self.submit_button = Button (master, text="Submit", bg='gray', fg='black',command=self.back_end_calling)
        self.submit_button.pack ()
        self.submit_button.place (x=280, y=115)

        self.summay_button = Button (master, text="Text Summary", command=self.get_me, bg='gray', fg='black')
        self.summay_button.pack ()
        self.summay_button.place (x=260, y=180)


    #choose the files

    def fileDialog(self):
        try:
            self.filename = filedialog.askopenfilename (initialdir="/", title="Select A File", filetype=(("txt", "*.csv"), ("All files", "*.*")))
            self.label = Label (text="")
            self.label.pack ()
            self.label.place (x=380, y=60)
            self.label.configure (text=self.filename)
            self.text1 = pd.read_csv (self.filename, encoding='utf8')
        except:
            self.label.configure (text="File is not uploaded")



    #open another window

    def a_w(self):
        def Upload_file_prompt(self):
            u = mb.showerror("Upload File", "Sorry, Please Upload File")
            print(u)
        try:
            self.window = Toplevel ()
            self.window.minsize (600, 400)
            myframe_outer = ttk.Frame (self.window)
            mycanvas = Canvas (myframe_outer, height=400, width=800)
            # mycanvas1 = Canvas(myframe_outer, height=400, width=400)
            myframe_inner = ttk.Frame (mycanvas)
            myscroll = ttk.Scrollbar (myframe_outer, orient='horizontal', command=mycanvas.xview)
            myscrolla = ttk.Scrollbar (myframe_outer, orient='vertical', command=mycanvas.yview)
            mycanvas.configure (xscrollcommand=myscroll.set)
            mycanvas.configure (yscrollcommand=myscrolla.set)
            myframe_outer.grid ()
            mycanvas.grid (row=1, sticky='nesw')
            # mycanvas.grid(coulmn=1, sticky='nesw')
            myscroll.grid (row=2, sticky='ew')
            myscrolla.grid (column=2, sticky='ew')
            mycanvas.create_window (0, 0, window=myframe_inner, anchor='nw')
            ttk.Label (myframe_inner, text=self.text1).grid (sticky='w')
        except:
            print(Upload_file_prompt(self))
        return
    def get_me(self):
        s = simpledialog.askinteger ('input string', "Please Enter, How Many  lines You want to display")
        print(s)
        return
    def back_end_calling(self):
        return Summarize()
    def summary(self):
        top = Tk()
        text = Text(top)
        try:
            if(Summarize.summarized_data is None):
                print("not proceessed the data! please wait\n")
            else:
                for i in Summarize.summarized_data:
                    text.insert(INSERT, i)
                    top.resizable(True, True)
                    text.pack()
        except:
            print("Summary not Generated Yet! Please wait few minutes\n")
        return





if __name__ == "__main__":
    root = Tk ()
    front_end = FrontEnd (root)


    root.mainloop()

