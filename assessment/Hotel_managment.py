import tkinter  as Tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *


class HotelManagment:
    # t=ttk.Window(themename='solar')
    def __init__(self,root):
        
    
        self.root=root
        self.root.title('HotelManagment software')
        self.root.geometry('950x620')
        try:
            with open('file.txt','r') as f:
                theme=f.read()
                # print(theme)
                self.root.style.theme_use(str(theme))
                
        except Exception as e:
            print(e)

    
       
        

        
        # Variable
        self.select_theme_value=Tk.StringVar() 
        


        l1=ttk.Label(self.root, text='Hotel Manager',bootstyle="white",font=("Arial", 15, "bold")).place(x=20,y=30)
        hr=ttk.Separator(self.root,bootstyle="gray",orient='horizontal')
        hr.place(x=20, y=80,relwidth=0.95)
        select_theme_lb=ttk.Label(self.root, text='Select a theme:',bootstyle="white",font=("Arial", 10)).place(relx = 1, x =-250, y = 30, anchor = NE)

        select_theme_combo=ttk.Combobox(self.root,bootstyle='secondary',font=("Arial", 10),textvariable =self.select_theme_value,state='readonly')
        fk=select_theme_combo['value']=('superhero','solar','darkly','cyborg','vapor','cosmo','flatly','journal','litera','lumen',
                                        'minty','pulse','sandstone','united','yeti','morph','simplex','cerculean')
        select_theme_combo.current(fk.index(theme))
        select_theme_combo.place(relx = 1, x =-40, y = 25, anchor = NE, width=200)
        select_theme_combo.bind("<<ComboboxSelected>>",self.color_change)
        
        # LabelFrame
        LabelFrame1=ttk.LabelFrame(self.root,text='MENU')
        LabelFrame1.place(x=20,y=103,width=700,height=80)
        LabelFrame2=ttk.LabelFrame(self.root,text='GUEST MENU')
        LabelFrame2.place(relx = 1, x =-25, y = 103, anchor = NE, width=190,height=370)
        LabelFrame3=ttk.LabelFrame(self.root,text='STAF LIST')
        LabelFrame3.place( x =20, y = 220,  width=345,height=120)
        LabelFrame4=ttk.LabelFrame(self.root,text='PREBOOK LIST')
        LabelFrame4.place( x =373, y = 220, width=345,height=120)
        LabelFrame5=ttk.LabelFrame(self.root,text='PREBOOK LIST')
        LabelFrame5.place( x =20, y = 350, width=345,height=250)
        LabelFrame6=ttk.LabelFrame(self.root,text='STATUS')
        LabelFrame6.place(relx = 1, x =-25, y = 480, anchor = NE, width=190,height=120)
        # Button GUEST MENU
        ch_in_btn=ttk.Button(LabelFrame2,bootstyle="primary",text='CHECK INN')
        ch_in_btn.place(x=10, y=20,width=170,height=60)

        sh_gs_btn=ttk.Button(LabelFrame2,bootstyle="warning",text='SHOW GUEST LIST')
        sh_gs_btn.place(x=10, y=85,width=170,height=60)

        ch_out_btn=ttk.Button(LabelFrame2,bootstyle="success",text='CHECK OUT')
        ch_out_btn.place(x=10, y=150,width=170,height=60)

        gt_info_btn=ttk.Button(LabelFrame2,bootstyle="info",text='GET GUEST INFO')
        gt_info_btn.place(x=10, y=215,width=170,height=60)

        ex_btn=ttk.Button(LabelFrame2,bootstyle="danger",text='EXIT',command=self.ext)
        ex_btn.place(x=10, y=280,width=170,height=60)

        # Button Menu 
        my_style=ttk.Style()
        my_style.configure('success.TButton',font=("time new roman", 6, "bold"))
        avlb_rom_btn=ttk.Button(LabelFrame1,bootstyle="success",text='AVAILABLE ROOM',style='success.TButton',command=self.AVAILABLE_Room)
        avlb_rom_btn.place(x=10, y=5,width=125,height=40)

        my_style1=ttk.Style()
        my_style1.configure('primary.TButton',font=("time new roman", 6, "bold"))
        fd_list_btn=ttk.Button(LabelFrame1,bootstyle="primary",text='FOOD LIST',style='primary.TButton')
        fd_list_btn.place(x=148, y=5,width=125,height=40)

        my_style2=ttk.Style()
        my_style2.configure('danger.TButton',font=("time new roman", 6, "bold"))
        ord_fd_btn=ttk.Button(LabelFrame1,bootstyle="danger",text='FOOD ORDER',style='danger.TButton')
        ord_fd_btn.place(x=284, y=5,width=125,height=40)

        my_style3=ttk.Style()
        my_style3.configure('info.TButton',font=("time new roman", 6, "bold"))
        event_pln=ttk.Button(LabelFrame1,bootstyle="info",text='EVENT PLAN',style='info.TButton')
        event_pln.place(x=422, y=5,width=125,height=40)

        my_style4=ttk.Style()
        my_style4.configure('warning.TButton',font=("time new roman", 6, "bold"))
        bill=ttk.Button(LabelFrame1,bootstyle="warning",text='Billing',style='warning.TButton')
        bill.place(x=560, y=5,width=125,height=40)


        M=ttk.Meter(self.root,bootstyle="success", subtextstyle="warning",textright='%',metertype='full',stripethickness=10,interactive=True)
        M.place( x =430, y = 350)



    def AVAILABLE_Room(self):
        self.top=Tk.Toplevel(self.root)
        self.top.geometry("800x500")
        self.top.title("Chick Inn")
        self.top.configure(bg='#d9e3f1')
        # self.top.style.theme_use('yeti')
        
        coldata = [
            {"text": "Room No.", "stretch": False},
            "Category",
            "Room size",
            {"text": "Status", "stretch": False},

        ]

        rowdata = [
            ('A123', 'Ac room',"single", 'Book'),
            ('A136', 'Non ac room.',"duble", 'AVAILABLE'),
            ('A158', 'Ac room',"duble",  'AVAILABLE')
        ]

        dt = Tableview(
            self.top,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            # stripecolor=(colors.light, None),
        )
        dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)


        
        
    def color_change(self,e):
        
        try:
            
            with open('file.txt','w') as f:
                f.write(self.select_theme_value.get())
            self.__init__(root)    
                
        except Exception as e:
            print(e)

    
    def ext(self):
        
        msg = messagebox.askquestion("que", "Do you want to exit ?")
        if msg == "yes":
            self.root.destroy()
        else:
            pass

        
        
    

root=ttk.Window()

hotel=HotelManagment(root)

root.mainloop()