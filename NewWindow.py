import tkinter as tk
class DeleteWindow:
  def __init__(self, root, info):
    self.info = info
    self.root = root
    self.canvas1 = tk.Canvas(root, width=200, height=100)


    def exit_application():
      self.info ='null'
      self.root.quit()
    
    def deletebook():
      self.root.quit()
    
    self.label1 = tk.Label(root, text='''Are you sure you wish
    to delete this book?''')
    self.label1.place(x=40, y=10)
    self.label2 = tk.Label(root, text=self.info)
    self.label2.place(x=35, y=45)
    self.button1 = tk.Button(root, text='Yes', command=deletebook, width=10).place(x=10, y=120)
    self.button2 = tk.Button(root, text="No", command=exit_application, width=10).place(x=115, y=120)
    self.root.deiconify()
    self.root.mainloop()
    self.root.withdraw()
    
  